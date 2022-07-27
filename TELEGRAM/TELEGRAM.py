from ..config import BOT_TELEGRAM_PADRE
TOKEN = BOT_TELEGRAM_PADRE['TOKEN']


import telebot, time
import threading

#Instanciamos el Bot
bot = telebot.TeleBot(TOKEN)

#Responde el comando Start
@bot.message_handler(commands=['start', 'ayuda', 'help'])
def cmd_start(message):
    print("Entro en la funcion Start")
    bot.reply_to(message, 'HOLA QLOQ')


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
        time.sleep(1)
        bot.send_message(message.chat.id, message_a_enviar, parse_mode='html')

def recibir_mensajes():
    bot.infinity_polling()

# MAIN ------------------
if __name__ == '__main__':
    bot.set_my_commands([
        telebot.types.BotCommand('/start', 'Da la Bienvenida'),
        telebot.types.BotCommand('/start2', 'Da la Bienvenida'),
        telebot.types.BotCommand('/start3', 'Da la Bienvenida')
    ])
    print("INICIO EL BOT PADRE")
    hilo_bot = threading.Thread(name='hilo_bot', target=recibir_mensajes)
    hilo_bot.start()
    print("QLOQ")