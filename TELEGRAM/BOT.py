from VARIABLES_ENTORNO_TELEGRAM import *
from Funciones_BOT import *
import time
import threading

import telebot                                      #Importo el bot
from telebot.types import ReplyKeyboardMarkup       #Crear Botones
from telebot.types import ForceReply                #Para citar un mensaje
from telebot.types import ReplyKeyboardRemove       #Quitar botones

from telebot.types import InlineKeyboardMarkup      #Crear botones
from telebot.types import InlineKeyboardButton      #Definir Botones


#Aqui Instancio MI BOT
bot = telebot.TeleBot(TOKEN_TELEGRAM)

#Responde el comando /START
@bot.message_handler(commands=['start','ayuda','help','info'])
def cmd_start(message):
    #Dar la Bienvenida al Usuario
    markup = ReplyKeyboardRemove()
    mensaje_a_eliminar = bot.reply_to(message, "Este mensaje se eliminara, al completar de cargar")
    message_enviar = Mensaje_start(message.chat.first_name)
    bot.send_chat_action(message.chat.id, 'typing') #PARA PONER QUE ESTA ESCRIBIENDO
    bot.send_message(message.chat.id, message_enviar, parse_mode='html', reply_markup=markup);time.sleep(3)
    bot.delete_message(message.chat.id, mensaje_a_eliminar.message_id)

#Funcion para buscar los Premios #!TENGO QUE CREAR DIFERENTES FUNCIONES PARA VALIDAR DATO INGRESADo
@bot.message_handler(commands=['resultados','resultado'])
def cmd_resultados(message):
    markup = ForceReply()
    msg = bot.send_message(message.chat.id, "Cual Loteria deseas consultar?", reply_markup=markup)
    bot.register_next_step_handler(msg, preguntar_sorteo)

def preguntar_sorteo(message):
    loteria = message.text
    arr = {'LOTERIA':loteria}
    markup = ForceReply()
    msg = bot.send_message(message.chat.id, "Cual Sorteo deseas consultar?", reply_markup=markup)
    bot.register_next_step_handler(msg, preguntar_fecha, arr )

def preguntar_fecha(message, arr):
    sorteo = message.text
    arr['SORTEO']=sorteo
    markup = ForceReply()
    msg = bot.send_message(message.chat.id, "Cual Fecha deseas consultar?", reply_markup=markup)
    bot.register_next_step_handler(msg, Consultar_Datos,arr )

def Consultar_Datos(message,arr ):
    fecha = message.text
    arr['FECHA']=fecha
    markup = ReplyKeyboardMarkup(
        one_time_keyboard=True,                         # Para que aparezca el mensaje
        input_field_placeholder='Elige una opcion',     # Mensaje
        resize_keyboard=True,                           # Con esto ajusto el tamano de los botones
        #row_width=5                                     #Con esto ajusto la fila que se van a genereada
    )
    #markup.add('SI','NO')                               #Aqui se distribuyen solo los botones
    markup.row('SI')                                    #Aqui especifico qeu en la primera fila solo saldra SI
    markup.row('NO')
    msg = bot.send_message(message.chat.id, "Esta seguro?" , reply_markup=markup)
    bot.register_next_step_handler(msg, Validar_Datos, arr)

def Validar_Datos(message, arr):
    markup = ReplyKeyboardRemove()
    if message.text != 'SI' and message.text != 'NO':
        msg = bot.send_message(message.chat.id, "Error: Datos Invalidos")
        bot.register_next_step_handler(msg, Validar_Datos, arr)
        bot.send_message(message.chat.id, "Solo puedes elegir SI o NO", reply_markup=markup)
    else:
        print(arr)
        bot.send_message(message.chat.id, "OK", reply_markup=markup)
        del arr

#Funcion para Buscar Premios con BOTONES en Pantalla
@bot.message_handler(commands=['premios','premio'])
def cmd_premios(message):
    markup = InlineKeyboardMarkup()
    b1 = InlineKeyboardButton('DOMINICANA'  , callback_data = 'DOMINICANA')
    b2 = InlineKeyboardButton('AMERICANA'   , callback_data = 'AMERICANA')
    markup.add(b1,b2)
    bot.send_message(message.chat.id, "Cual es el tipo de loteria a consultar", reply_markup=markup)

@bot.callback_query_handler(func=lambda x : True)
def respuesta_botones_inline(call):
    #Esto gestiona las acciones de los botones de CALLBACK_DATA
    cid = call.from_user.id
    mid = call.message.id

    if call.data == 'DOMINICANA':
        bot.delete_message(cid,mid)
    else:
        bot.delete_message(cid,mid)



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
        telebot.types.BotCommand('/resultados', 'Para consultar los premios'),
        telebot.types.BotCommand('/premios', 'Para consultar los premios')
    ])
    HILO_BOT = threading.Thread(name='HILO_BOT', target=recibir_mensaje)
    HILO_BOT.start()
    bot.send_message(MI_CHAT_ID, "INICIO EL BOT")