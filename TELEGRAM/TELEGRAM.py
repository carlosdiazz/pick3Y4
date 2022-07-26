TELEGRAM_TOKEN_PADRE = '5348496240:AAHvkD64i5AveuGv3v_5K1y5AyPn74MOqVg'


import telebot

#Instanciamos el Bot
bot = telebot.TeleBot(TELEGRAM_TOKEN_PADRE)

#Responde el comando Start
@bot.message_handler(commands=['start', 'ayuda', 'help'])
def cmd_start(message):
    print("Entro en la fun cion Start")
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
        bot.send_message(message.chat.id, message_a_enviar, parse_mode='html')


# MAIN ------------------
if __name__ == '__main__':
    print("INICIO EL BOT PADRE")
    bot.infinity_polling()
    print("QLOQ")