
from telegram_bot_calendar import DetailedTelegramCalendar, LSTEP
from email import header
import telebot, time
import threading
from telebot.types import ReplyKeyboardMarkup #Para crear botones
from telebot.types import ForceReply #Para citar un mensaje
from telebot.types import ReplyKeyboardRemove #Para eliminar botones

from telebot.types import InlineKeyboardMarkup
from telebot.types import InlineKeyboardButton

from Funciones_BOT import *
import requests
from bs4 import BeautifulSoup
from VARIABLES_ENTORNO_TELEGRAM import TOKEN_TELEGRAM

#Instanciamos el Bot
bot = telebot.TeleBot(TOKEN_TELEGRAM)

#Responde el comando Start
@bot.message_handler(commands=['start', 'ayuda', 'help', 'info'])
def cmd_start(message):
    print("Entro en la funcion START DEL BOT")
    bot.send_chat_action(message.chat.id, 'typing') # AQUI AGREGO QUE ESTE ESCRIBIENDO
    userName    = message.from_user.first_name
    userId      = str(message.from_user.id)
    print(AGREGAR_USER_MONGO(userId))
    message_send = Mensaje_start(userName)
    markup = ReplyKeyboardRemove()
    bot.send_message(message.chat.id, message_send, reply_markup=markup, parse_mode='html')

@bot.message_handler(commands=['fecha'])
def start(m):
    calendar, step = DetailedTelegramCalendar().build()
    bot.send_message(m.chat.id,
                     f"Select {LSTEP[step]}",
                     reply_markup=calendar, )

@bot.callback_query_handler(func=DetailedTelegramCalendar.func())
def cal(c):
    result, key, step = DetailedTelegramCalendar().process(c.data)
    if not result and key:
        bot.edit_message_text(f"Select {LSTEP[step]}",
                              c.message.chat.id,
                              c.message.message_id,
                              reply_markup=key)
    elif result:
        bot.edit_message_text(f"{result}",
                              c.message.chat.id,
                              c.message.message_id)


def recibir_mensajes():
    bot.infinity_polling()

# MAIN ------------------
if __name__ == '__main__':
    bot.set_my_commands([
        telebot.types.BotCommand('/start', 'Informacion Bot'),
        telebot.types.BotCommand('/resultados', 'Para ver los Numeros ganadores'),
        #telebot.types.BotCommand('/start3', 'Da la Bienvenida')
    ])
    print("INICIO EL BOT PADRE")
    hilo_bot = threading.Thread(name='hilo_bot', target=recibir_mensajes)
    hilo_bot.start()
    print("QLOQ")