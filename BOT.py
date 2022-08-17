from unittest import result
from config import *
from Funciones_BOT import *
from Funciones_Especiales import fecha
import time
import threading

import telebot                                      #Importo el bot
from telebot.types import ReplyKeyboardMarkup       #Crear Botones
from telebot.types import ForceReply                #Para citar un mensaje
from telebot.types import ReplyKeyboardRemove       #Quitar botones

from telebot.types import InlineKeyboardMarkup      #Crear botones
from telebot.types import InlineKeyboardButton      #Definir Botones

from flask import Flask, request                    # Para crear el servidor Web Local
from pyngrok import ngrok, conf                     # Para crear un tunel entre nuestro servidor local y nuestra app

from telegram_bot_calendar import DetailedTelegramCalendar, LSTEP

from waitress import serve

#Aqui Instancio MI BOT
bot = telebot.TeleBot(TOKEN_TELEGRAM)

#Este dicionario apra guardar el ID por el momento del user para saber la fecha que elegio
FECHAS = {}
#Aqui isntancio el servidor Web de Flask
web_server = Flask(__name__)

#Gestiona las peticiones POST enviadas al servidor WEB
@web_server.route('/', methods=['POST'])
def webhook():
    #Si el POST RECIBE UN JSON
    if request.headers.get('content-type') == 'application/json':
        update = telebot.types.Update.de_json(request.stream.read().decode('utf-8'))
        bot.process_new_updates([update])
        return 'OK', 200
    else:
        return 'NO',404

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
    #print(message)

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

#! PONER UNA OPCION PARA ELEGIR LA FECHA DE HOY DIRECTO O CONSULTAR OTRA FECHA
def start(m):
    calendar, step = DetailedTelegramCalendar().build()
    bot.send_message(m.chat.id,
                    f"Select {LSTEP[step]}",
                    reply_markup=calendar,)

@bot.callback_query_handler(func=DetailedTelegramCalendar.func())
def cal(c):
    result, key, step = DetailedTelegramCalendar().process(c.data)
    if not result and key:
        bot.edit_message_text(f"Select {LSTEP[step]}",
                              c.message.chat.id,
                              c.message.message_id,
                              reply_markup=key)
    elif result:
        msg=bot.edit_message_text(f"{result}",
                              c.message.chat.id,
                              c.message.message_id)
        #FECHAS[c.from_user.id]=result
        bot.register_next_step_handler(msg,cmd_premios(msg))

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

    markup = InlineKeyboardMarkup()
    if call.data == 'DOMINICANA':
        bot.delete_message(cid,mid)
        PRIMERA     = InlineKeyboardButton('PRIMERA'        , callback_data = 'PRIMERA')
        KING        = InlineKeyboardButton('KING LOTTERY'   , callback_data = 'KING')
        LA_SUERTE   = InlineKeyboardButton('LA SUERTE'      , callback_data = 'LASUERTE')
        REAL        = InlineKeyboardButton('REAL'           , callback_data = 'REAL')
        markup.add(PRIMERA,KING,LA_SUERTE,REAL)
        bot.send_message(cid, "Elige la loteria a Buscar.", reply_markup=markup)
    elif call.data =='AMERICANA':
        bot.delete_message(cid,mid)
        FLORIDA         = InlineKeyboardButton('FLORIDA'        , callback_data = 'FLORIDA-USA')
        NEW_YORK        = InlineKeyboardButton('NEW YORK'        , callback_data = 'NEW_YORK-USA')
        markup.add(FLORIDA,NEW_YORK)
        bot.send_message(cid, "Elige la loteria a Buscar.", reply_markup=markup)

    elif call.data == 'PRIMERA':
        bot.delete_message(cid,mid)
        bot.send_message(cid, f"Elegiste la PRIMERA para la fecha {FECHAS[cid]}", reply_markup=markup)
        return 1

    else:
        bot.delete_message(cid,mid)
        
        #!IMPLEMNETAR LA LIBERACION DE MEMORIA DEL ARREGLO
        del fecha[cid]

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
    #bot.infinity_polling()
    conf.get_default().config_path = './config_ngrok.yml'       #Configuramos la ruta del archivo de ngrok
    conf.get_default().region = 'us'
    ngrok.set_auth_token(NGROK_TOKEN)

    #Creamos un tunel https en el puerto 5000
    ngrok_tunel = ngrok.connect(5000, bind_tls=True)

    #URL del tunel creado
    ngrok_url = ngrok_tunel.public_url
    print('URL NGROG:', ngrok_url)
    bot.remove_webhook()
    time.sleep(2)

    #Definimos el Webhook
    bot.set_webhook(url=ngrok_url)

    #arrancamos el servidor
    #web_server.run(host='0.0.0.0', port=5000)
    serve(web_server, host='0.0.0.0', port=5000)

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