from VARIABLES_ENTORNO_TELEGRAM import *
from Funciones_BOT import *
import time
import threading

import telebot                                      #Importo el bot
from telebot.types import ReplyKeyboardMarkup       #Crear Botones
from telebot.types import ForceReply                #Para citar un mensaje

#Aqui Instancio MI BOT
bot = telebot.TeleBot(TOKEN_TELEGRAM)

#Responde el comando /START
@bot.message_handler(commands=['start','ayuda','help'])
def cmd_start(message):
    #Dar la Bienvenida al Usuario
    mensaje_a_eliminar = bot.reply_to(message, "Este mensaje se eliminara, al completar de cargar")
    message_enviar = Mensaje_start(message.chat.first_name)
    bot.send_chat_action(message.chat.id, 'typing') #PARA PONER QUE ESTA ESCRIBIENDO
    bot.send_message(message.chat.id, message_enviar, parse_mode='html');time.sleep(3)
    bot.delete_message(message.chat.id, mensaje_a_eliminar.message_id)


#Funcion para buscar los Premios
@bot.message_handler(commands=['resultados','premios'])
def cmd_resultados(message):
    markup = ForceReply()
    msg = bot.send_message(message.chat.id, "Cual Loteria deseas consultar?", reply_markup=markup)
    bot.register_next_step_handler(msg, preguntar_sorteo)

def preguntar_sorteo(message):
    loteria = message.text
    markup = ForceReply()
    msg = bot.send_message(message.chat.id, "Cual Sorteo deseas consultar?", reply_markup=markup)
    bot.register_next_step_handler(msg, preguntar_fecha )

def preguntar_fecha(message):
    sorteo = message.text
    markup = ForceReply()
    msg = bot.send_message(message.chat.id, "Cual Fecha deseas consultar?", reply_markup=markup)
    bot.register_next_step_handler(msg, Consultar_Datos)

def Consultar_Datos(message):
    datos = message.text
    markup = ReplyKeyboardMarkup(
        one_time_keyboard=True,                         # Para que aparezca el mensaje
        input_field_placeholder='Elige una opcion',     # Mensaje
        resize_keyboard=True                            # Con esto ajusto el tamano de los botones
    )
    msg = bot.send_message(message.chat.id, "Esta seguro?" , reply_markup=markup)
    markup.add('SI','NO')
    bot.register_next_step_handler(msg, Validar_Datos)

def Validar_Datos(message):

    if message.text != 'SI' and message.text != 'NO':
        msg = bot.send_message(message.chat.id, "Error: Datos Invalidos")
        bot.register_next_step_handler(msg, Consultar_Datos)
        bot.send_message(message.chat.id, "Solo puedes elegir SI o NO" )
    else:
        print("d")







#Responderia todo los Texto
@bot.message_handler(content_types=['text'])
def cmd_mensaje(message):
    #Responde los mensajes RECIBIDOS
    if message.text.startswith('/'):
        bot.send_message(message.chat.id, "COMANDO NO DISPONIBLE")
    else:
        bot.send_message(message.chat.id, "ENTRA A MI CANAL")




#FUNCION PARA QUE EL BOT ESTE PENDIENTE SIEMPRE A UN NUEVO MENSAJE
def recibir_mensaje():
    bot.infinity_polling()







if __name__ == '__main__':
    print("INICIANDO EL BOT")
    bot.set_my_commands([
        telebot.types.BotCommand('/start', 'Da la Bienvenida'),
        telebot.types.BotCommand('/resultados', 'Para consultar los premios')
    ])
    HILO_BOT = threading.Thread(name='HILO_BOT', target=recibir_mensaje)
    HILO_BOT.start()
    bot.send_message(MI_CHAT_ID, "INICIO EL BOT")