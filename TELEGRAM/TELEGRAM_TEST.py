#from PICK.config import BOT_TELEGRAM_PADRE
#TOKEN = BOT_TELEGRAM_PADRE['TOKEN']
TOKEN ='5348496240:AAHvkD64i5AveuGv3v_5K1y5AyPn74MOqVg'
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

#Instanciamos el Bot
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['resultados'],)
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



@bot.message_handler(commands=['resultados'])
def cmd_botones(message):
    markup = InlineKeyboardMarkup()
    b1 = InlineKeyboardButton('BOTON 1', url='HTTP://YOUTUBE.com')
    b2 = InlineKeyboardButton('BOTON 2', url='HTTP://YOUTUBE.com')
    b3 = InlineKeyboardButton('BOTON 3', url='HTTP://YOUTUBE.com')
    b4 = InlineKeyboardButton('BOTON 4', url='HTTP://YOUTUBE.com')
    b5 = InlineKeyboardButton('BOTON 5', url='HTTP://YOUTUBE.com')
    b_cerrar = InlineKeyboardButton('cerrar', callback_data='cerrar')
    markup.add(b1,b2,b3,b4,b5,b_cerrar)
    bot.send_message(message.chat.id, 'Mis enlances', reply_markup=markup)

@bot.message_handler(commands=['botones'])
def cmd_botones(message):
    markup = InlineKeyboardMarkup()
    b1 = InlineKeyboardButton('BOTON 1', url='HTTP://YOUTUBE.com')
    b2 = InlineKeyboardButton('BOTON 2', url='HTTP://YOUTUBE.com')
    b3 = InlineKeyboardButton('BOTON 3', url='HTTP://YOUTUBE.com')
    b4 = InlineKeyboardButton('BOTON 4', url='HTTP://YOUTUBE.com')
    b5 = InlineKeyboardButton('BOTON 5', url='HTTP://YOUTUBE.com')
    b_cerrar = InlineKeyboardButton('cerrar', callback_data='cerrar')
    markup.add(b1,b2,b3,b4,b5,b_cerrar)
    bot.send_message(message.chat.id, 'Mis enlances', reply_markup=markup)

@bot.callback_query_handler(func=lambda x: True)
def respuesta_botones_inline(call):
    cid = call.from_user.id
    mid = call.message.id
    if call.data == 'cerrar':
        bot.delete_message(cid, mid)

USUARIOS = {}
#Responde el comando Start
@bot.message_handler(commands=['start', 'ayuda', 'help', 'info'])
def cmd_start(message):
    print("Entro en la funcion START DEL BOT")
    name = message.from_user.first_name
    message_send = Mensaje_start(name)
    print(name)
    markup = ReplyKeyboardRemove()
    #bot.reply_to(message, 'HOLA QLOQ',)
    bot.send_message(message.chat.id, message_send, reply_markup=markup, parse_mode='html')

@bot.message_handler(commands=['buscar'])
def cmd_buscar(message):
    print("ENtro en el buscador ")
    texto_buscar = ' '.join(message.text.split()[1:])
    if not texto_buscar:
        texto  = "Debes de introducir una busqueda\n\n"
        texto += 'Ejemplo: \n\n'
        texto += f'<code>{message.text} Perro</code>'
        bot.send_message(message.chat.id, texto, parse_mode='html')
        return 1
    else:
        print("Buscando en google")
        texto_buscar = texto_buscar.replace(" ", "+")
        url = f'https://www.google.com/search?q={texto_buscar}&num=100'
        user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.106 Safari/537.36 OPR/38.0.2220.41'
        headers = {'user-agent':user_agent}
        res = requests.get(url, headers=headers, timeout=10)
        if res.status_code != 200:
            print(f'Error al buscar: {res.status_code} {res.reason}')
            bot.send_message(message.chat.id, "Se ha producido  UN ERROR")
        print(url)

@bot.message_handler(commands=['alta'])
def cmd_alta(message):
    markup = ForceReply()
    msg = bot.send_message(message.chat.id, "DIME TU NOMBRE?", reply_markup=markup)
    bot.register_next_step_handler(msg, preguntar_Edad)

def preguntar_Edad(message):
    name = message.text
    USUARIOS[message.chat.id] = {}
    USUARIOS[message.chat.id]['NAME'] = message.text
    markup = ForceReply()
    msg = bot.send_message(message.chat.id, 'QUE EDAD TIENES', reply_markup=markup )
    bot.register_next_step_handler(msg,preguntar_SEXO)

def preguntar_SEXO(message):

    if not message.text.isdigit():
        markup = ForceReply()
        msg = bot.send_message(message.chat.id, 'QUE EDAD TIENES??', reply_markup=markup )
        bot.register_next_step_handler(msg,preguntar_SEXO)
    else:
        USUARIOS[message.chat.id]['EDAD'] = int(message.text)
        markup = ReplyKeyboardMarkup(
            one_time_keyboard=True,
            input_field_placeholder='PULSA EL BOTON',
            resize_keyboard=True,
            #AQUI INDICO CUANTA FILA PUEDO TEENER PUEDO TENER HASTA 12 -- row_width=1 
            )
        markup.add('HOMBRE', 'MUJER')
        msg = bot.send_message(message.chat.id, 'CUAL ES TU SEXO?', reply_markup=markup )
        bot.register_next_step_handler(msg,guardar_datos)

def guardar_datos(message):
    if message.text != 'HOMBRE' and message.text != 'MUJER':
        markup = ForceReply()
        msg = bot.send_message(message.chat.id, 'QUE EDAD TIENES??', reply_markup=markup )
        bot.register_next_step_handler(msg,preguntar_SEXO)
    else:
        markup =ReplyKeyboardRemove()
        bot.send_message(message.chat.id, 'SE REGISTRO BIEN', reply_markup=markup)
        USUARIOS[message.chat.id]['SEXO'] = message.text
        print(USUARIOS)

@bot.message_handler(content_types=['text'])
def bot_mensajes_texto(message):
    print("Entro en la funcion de responder mensaje")

    message_a_enviar     =      '<code>BOT LOTERIAS</code>\n\n'
    message_a_enviar     +=     '<b><u>CARLOS</u></b>\n'
    message_a_enviar     +=     '<b>LOTERIA: </b> <i> GANAMAS </i>\n'
    message_a_enviar     +=     '<b>SORTEO: </b> <i> GANAMAS </i>\n'
    message_a_enviar     +=     '<b>FECHA: </b> <i> 12/12/2022 </i>\n'
    message_a_enviar     +=     '<b>Numeros Ganadores: </b> <i> 12-12-34 </i>'

    if message.text.startswith('/'):
        bot.send_message(message.chat.id, 'Comando No Disponible')
    else:
        bot.send_chat_action(message.chat.id, 'typing') # AQUI AGREGO QUE ESTE ESCRIBIENDO
        #time.sleep(1)
        bot.send_message(message.chat.id, message_a_enviar, parse_mode='html')

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