from VARIABLES import *
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
    mensaje_a_eliminar = bot.reply_to(message, "Este mensaje se eliminara, al completar de cargar... Su Usuario ha sido registrado para recibir notificaciones")
    print(AGREGAR_USER_MONGO(message.from_user.id))
    message_enviar = Mensaje_start(message.chat.first_name)
    bot.send_chat_action(message.chat.id, 'typing') #PARA PONER QUE ESTA ESCRIBIENDO
    bot.send_message(message.chat.id, message_enviar, parse_mode='html', reply_markup=markup);time.sleep(3)
    bot.delete_message(message.chat.id, mensaje_a_eliminar.message_id)
    #print(message)

##Funcion para buscar los Premios #!TENGO QUE CREAR DIFERENTES FUNCIONES PARA VALIDAR DATO INGRESADO
#@bot.message_handler(commands=['FORZAR','forzar'])
#def cmd_resultados(message):
#    markup = ForceReply()
#    msg = bot.send_message(message.chat.id, "Cual Loteria deseas FORZAR EL PREMIO?", reply_markup=markup)
#    bot.register_next_step_handler(msg, preguntar_sorteo)
#
#def preguntar_sorteo(message):
#    loteria = message.text
#    arr = {'LOTERIA':loteria}
#    markup = ForceReply()
#    msg = bot.send_message(message.chat.id, "Cual Sorteo deseas consultar?", reply_markup=markup)
#    bot.register_next_step_handler(msg, preguntar_fecha, arr )
#
#def preguntar_fecha(message, arr):
#    sorteo = message.text
#    arr['SORTEO']=sorteo
#    markup = ForceReply()
#    msg = bot.send_message(message.chat.id, "Cual Fecha deseas consultar?", reply_markup=markup)
#    bot.register_next_step_handler(msg, Consultar_Datos,arr )
#
#def Consultar_Datos(message,arr ):
#    fecha = message.text
#    arr['FECHA']=fecha
#    markup = ReplyKeyboardMarkup(
#        one_time_keyboard=True,                         # Para que aparezca el mensaje
#        input_field_placeholder='Elige una opcion',     # Mensaje
#        resize_keyboard=True,                           # Con esto ajusto el tamano de los botones
#        #row_width=5                                     #Con esto ajusto la fila que se van a genereada
#    )
#    #markup.add('SI','NO')                               #Aqui se distribuyen solo los botones
#    markup.row('SI')                                    #Aqui especifico qeu en la primera fila solo saldra SI
#    markup.row('NO')
#    msg = bot.send_message(message.chat.id, "Esta seguro?" , reply_markup=markup)
#    bot.register_next_step_handler(msg, Validar_Datos, arr)
#
#def Validar_Datos(message, arr):
#    markup = ReplyKeyboardRemove()
#    if message.text != 'SI' and message.text != 'NO':
#        msg = bot.send_message(message.chat.id, "Error: Datos Invalidos")
#        bot.register_next_step_handler(msg, Validar_Datos, arr)
#        bot.send_message(message.chat.id, "Solo puedes elegir SI o NO", reply_markup=markup)
#    else:
#        print(arr)
#        bot.send_message(message.chat.id, "OK", reply_markup=markup)
#        del arr
#
#Funcion para Buscar Premios con BOTONES en Pantalla
@bot.message_handler(commands=['premios','premio'])

#! PONER UNA OPCION PARA ELEGIR LA FECHA DE HOY DIRECTO O CONSULTAR OTRA FECHA
def start(m):
    FECHAS[m.from_user.id]={}
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
        FECHAS[c.from_user.id]['FECHA']=result
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

        BTN_PRIMERA         = InlineKeyboardButton(OBJ_PRIMERA_AM['LOTERIA']        , callback_data = OBJ_PRIMERA_AM['LOTERIA'])
        BTN_KING            = InlineKeyboardButton(OBJ_KING_AM['LOTERIA']           , callback_data = OBJ_KING_AM['LOTERIA'])
        BTN_LA_SUERTE       = InlineKeyboardButton(OBJ_LA_SUERTE['LOTERIA']         , callback_data = OBJ_LA_SUERTE['LOTERIA'])
        BTN_REAL            = InlineKeyboardButton(OBJ_REAL['LOTERIA']              , callback_data = OBJ_REAL['LOTERIA'])
        BTN_FLORIDA         = InlineKeyboardButton(OBJ_FLORIDA_RD_AM['LOTERIA']     , callback_data = OBJ_FLORIDA_RD_AM['LOTERIA'])
        BTN_LOTEDOM         = InlineKeyboardButton(OBJ_LOTEDOM['LOTERIA']           , callback_data = OBJ_LOTEDOM['LOTERIA'])
        BTN_NEW_YORK        = InlineKeyboardButton(OBJ_NEW_YORK_RD_AM['LOTERIA']    , callback_data = OBJ_NEW_YORK_RD_AM['LOTERIA'] )
        BTN_ANGUILA         = InlineKeyboardButton(OBJ_ANGUILLA_AM['LOTERIA']       , callback_data = OBJ_ANGUILLA_AM['LOTERIA'])
        BTN_LOTEKA          = InlineKeyboardButton(OBJ_LOTEKA['LOTERIA']            , callback_data = OBJ_LOTEKA['LOTERIA'])
        BTN_GANAMAS         = InlineKeyboardButton(OBJ_GANAMAS['LOTERIA']           , callback_data  = OBJ_GANAMAS['LOTERIA'])
        BTN_LEIDSA          = InlineKeyboardButton(OBJ_LEIDSA['LOTERIA']            , callback_data = OBJ_LEIDSA['LOTERIA'])
        BTN_NACIONAL        = InlineKeyboardButton(OBJ_NACIONAL['LOTERIA']          , callback_data = OBJ_NACIONAL['LOTERIA'])
        BTN_GEORGIA         = InlineKeyboardButton(OBJ_GEORGIA_RD_AM['LOTERIA']     , callback_data = OBJ_GEORGIA_RD_AM['LOTERIA'])

        markup.add(
            BTN_PRIMERA,
            BTN_KING,
            BTN_LA_SUERTE,
            BTN_REAL,
            BTN_FLORIDA,
            BTN_LOTEDOM,
            BTN_NEW_YORK,
            BTN_GANAMAS,
            BTN_ANGUILA,
            BTN_LOTEKA,
            BTN_NACIONAL,
            BTN_LEIDSA,
            BTN_GEORGIA
        )
        bot.send_message(cid, "Elige la loteria a Buscar.", reply_markup=markup)

    #! QUEDE AQUI TENGO QUE HACER UNA FUNCION PARA CONSULTAR LOS NUMEROS YA SEA AMERICANOS O DOMINICANO
    elif call.data == OBJ_LA_SUERTE['LOTERIA']: #? LA SUERTE
        FECHAS[cid]['LOTERIA']=OBJ_LA_SUERTE['LOTERIA']
        FECHAS[cid]['MODALIDAD']=OBJ_LA_SUERTE['MODALIDAD']
        bot.delete_message(cid,mid)
        msg = Mensaje_elegiste_loteria(FECHAS[cid])
        msg_resultados = OBTENER_PREMIOS(FECHAS[cid])
        bot.send_message(cid, msg, reply_markup=markup)
        bot.send_message(cid, msg_resultados, reply_markup=markup, parse_mode='html')
        return 1

    elif call.data == OBJ_PRIMERA_AM['LOTERIA']: #? LA PRIMERA
        FECHAS[cid]['LOTERIA']=OBJ_PRIMERA_AM['LOTERIA']
        FECHAS[cid]['MODALIDAD']=OBJ_PRIMERA_AM['MODALIDAD']
        bot.delete_message(cid,mid)
        msg = Mensaje_elegiste_loteria(FECHAS[cid])
        msg_resultados = OBTENER_PREMIOS(FECHAS[cid])
        bot.send_message(cid, msg, reply_markup=markup)
        bot.send_message(cid, msg_resultados, reply_markup=markup, parse_mode='html')
        return 1

    elif call.data == OBJ_KING_AM['LOTERIA']: #? King Loterry
        FECHAS[cid]['LOTERIA']= OBJ_KING_AM['LOTERIA']
        FECHAS[cid]['MODALIDAD']=OBJ_KING_AM['MODALIDAD']
        bot.delete_message(cid,mid)
        msg = Mensaje_elegiste_loteria(FECHAS[cid])
        msg_resultados = OBTENER_PREMIOS(FECHAS[cid])
        bot.send_message(cid, msg, reply_markup=markup)
        bot.send_message(cid, msg_resultados, reply_markup=markup, parse_mode='html')
        return 1

    elif call.data == OBJ_REAL['LOTERIA']: #? REAL
        FECHAS[cid]['LOTERIA'] = OBJ_REAL['LOTERIA']
        FECHAS[cid]['MODALIDAD']=OBJ_REAL['MODALIDAD']
        bot.delete_message(cid,mid)
        msg = Mensaje_elegiste_loteria(FECHAS[cid])
        msg_resultados = OBTENER_PREMIOS(FECHAS[cid])
        bot.send_message(cid, msg, reply_markup=markup)
        bot.send_message(cid, msg_resultados, reply_markup=markup, parse_mode='html')
        return 1

    elif call.data == OBJ_FLORIDA_RD_AM['LOTERIA']: #? FLORIDA
        FECHAS[cid]['LOTERIA']= OBJ_FLORIDA_RD_AM['LOTERIA']
        FECHAS[cid]['MODALIDAD']=OBJ_FLORIDA_RD_AM['MODALIDAD']
        bot.delete_message(cid,mid)
        msg = Mensaje_elegiste_loteria(FECHAS[cid])
        msg_resultados = OBTENER_PREMIOS(FECHAS[cid])
        bot.send_message(cid, msg, reply_markup=markup)
        bot.send_message(cid, msg_resultados, reply_markup=markup, parse_mode='html')
        return 1

    elif call.data ==OBJ_LOTEDOM['LOTERIA']: #? LOTEDOM
        FECHAS[cid]['LOTERIA']= OBJ_LOTEDOM['LOTERIA']
        FECHAS[cid]['MODALIDAD']=OBJ_LOTEDOM['MODALIDAD']
        bot.delete_message(cid,mid)
        msg = Mensaje_elegiste_loteria(FECHAS[cid])
        msg_resultados = OBTENER_PREMIOS(FECHAS[cid])
        bot.send_message(cid, msg, reply_markup=markup)
        bot.send_message(cid, msg_resultados, reply_markup=markup, parse_mode='html')
        return 1

    elif call.data == OBJ_NEW_YORK_RD_AM['LOTERIA']: #? NEW YORK
        FECHAS[cid]['LOTERIA']= OBJ_NEW_YORK_RD_AM['LOTERIA']
        FECHAS[cid]['MODALIDAD']=OBJ_NEW_YORK_RD_AM['MODALIDAD']
        bot.delete_message(cid,mid)
        msg = Mensaje_elegiste_loteria(FECHAS[cid])
        msg_resultados = OBTENER_PREMIOS(FECHAS[cid])
        bot.send_message(cid, msg, reply_markup=markup)
        bot.send_message(cid, msg_resultados, reply_markup=markup, parse_mode='html')
        return 1

    elif call.data == OBJ_ANGUILLA_AM['LOTERIA']: #? ANGUILA
        FECHAS[cid]['LOTERIA']= OBJ_ANGUILLA_AM['LOTERIA']
        FECHAS[cid]['MODALIDAD']=OBJ_ANGUILLA_AM['MODALIDAD']
        bot.delete_message(cid,mid)
        msg = Mensaje_elegiste_loteria(FECHAS[cid])
        msg_resultados = OBTENER_PREMIOS(FECHAS[cid])
        bot.send_message(cid, msg, reply_markup=markup)
        bot.send_message(cid, msg_resultados, reply_markup=markup, parse_mode='html')
        return 1

    elif call.data == OBJ_LOTEKA['LOTERIA']: #? LOTEKA
        FECHAS[cid]['LOTERIA']= OBJ_LOTEKA['LOTERIA']
        FECHAS[cid]['MODALIDAD']=OBJ_LOTEKA['MODALIDAD']
        bot.delete_message(cid,mid)
        msg = Mensaje_elegiste_loteria(FECHAS[cid])
        msg_resultados = OBTENER_PREMIOS(FECHAS[cid])
        bot.send_message(cid, msg, reply_markup=markup)
        bot.send_message(cid, msg_resultados, reply_markup=markup, parse_mode='html')
        return 1

    elif call.data == OBJ_LEIDSA['LOTERIA']: #? LEIDSA
        FECHAS[cid]['LOTERIA']= OBJ_LEIDSA['LOTERIA']
        FECHAS[cid]['MODALIDAD']=OBJ_LEIDSA['MODALIDAD']
        bot.delete_message(cid,mid)
        msg = Mensaje_elegiste_loteria(FECHAS[cid])
        msg_resultados = OBTENER_PREMIOS(FECHAS[cid])
        bot.send_message(cid, msg, reply_markup=markup)
        bot.send_message(cid, msg_resultados, reply_markup=markup, parse_mode='html')
        return 1

    elif call.data == OBJ_GANAMAS['LOTERIA']: #? GANAMAS
        FECHAS[cid]['LOTERIA']= OBJ_GANAMAS['LOTERIA']
        FECHAS[cid]['MODALIDAD']=OBJ_GANAMAS['MODALIDAD']
        bot.delete_message(cid,mid)
        msg = Mensaje_elegiste_loteria(FECHAS[cid])
        msg_resultados = OBTENER_PREMIOS(FECHAS[cid])
        bot.send_message(cid, msg, reply_markup=markup)
        bot.send_message(cid, msg_resultados, reply_markup=markup, parse_mode='html')
        return 1

    elif call.data == OBJ_NACIONAL['LOTERIA']: #? NACIONAl
        FECHAS[cid]['LOTERIA'] = OBJ_NACIONAL['LOTERIA']
        FECHAS[cid]['MODALIDAD']=OBJ_NACIONAL['MODALIDAD']
        bot.delete_message(cid,mid)
        msg = Mensaje_elegiste_loteria(FECHAS[cid])
        msg_resultados = OBTENER_PREMIOS(FECHAS[cid])
        bot.send_message(cid, msg, reply_markup=markup)
        bot.send_message(cid, msg_resultados, reply_markup=markup, parse_mode='html')
        return 1

    elif call.data == OBJ_GEORGIA_RD_AM['LOTERIA']: #? GEORGIA
        FECHAS[cid]['LOTERIA']   = OBJ_GEORGIA_RD_AM['LOTERIA']
        FECHAS[cid]['MODALIDAD'] = OBJ_GEORGIA_RD_AM['MODALIDAD']
        bot.delete_message(cid,mid)
        msg = Mensaje_elegiste_loteria(FECHAS[cid])
        msg_resultados = OBTENER_PREMIOS(FECHAS[cid])
        bot.send_message(cid, msg, reply_markup=markup)
        bot.send_message(cid, msg_resultados, reply_markup=markup, parse_mode='html')
        return 1


    #elif call.data == OBJ_PRIMERA_AM['LOTERIA']: #? LA PRIMERA - LOTERIA
    #    bot.delete_message(cid,mid)
    #    BTN_PRIMERA_AM  = InlineKeyboardButton(OBJ_PRIMERA_AM['SORTEO']        , callback_data = OBJ_PRIMERA_AM['SORTEO'] )
    #    BTN_PRIMERA_PM  = InlineKeyboardButton(OBJ_PRIMERA_PM['SORTEO']        , callback_data = OBJ_PRIMERA_PM['SORTEO'])
    #    markup.add(
    #        BTN_PRIMERA_AM,
    #        BTN_PRIMERA_PM
    #    )
    #    bot.send_message(cid, f"Elige el sorteo a Buscar. ", reply_markup=markup)
    #    #return 1
    #
    #elif call.data == OBJ_PRIMERA_AM['SORTEO'] : #PRIMERA DIA
    #    bot.delete_message(cid,mid)
    #    FECHAS[cid]['LOTERIA']=OBJ_PRIMERA_AM['SORTEO']
    #    bot.send_message(cid, f"Elegiste la {OBJ_PRIMERA_AM['SORTEO'] } para la fecha: ", reply_markup=markup)
    #    return 1
    #
    #elif call.data == OBJ_PRIMERA_AM['SORTEO'] : #PRIMERA NOCHE
    #    bot.delete_message(cid,mid)
    #    FECHAS[cid]['LOTERIA']=OBJ_PRIMERA_AM['SORTEO']
    #    bot.send_message(cid, f"Elegiste la {OBJ_PRIMERA_AM['SORTEO'] } para la fecha: ", reply_markup=markup)
    #    return 1

    elif call.data =='AMERICANA':
        bot.delete_message(cid,mid)
        BTN_GEORGIA         = InlineKeyboardButton(OBJ_GA_AM['LOTERIA']     , callback_data = 'GEORGIA-USA')
        BTN_MARYLAND        = InlineKeyboardButton(OBJ_MD_AM['LOTERIA']     , callback_data = OBJ_MD_AM['LOTERIA'])
        BTN_NEW_JERSEY      = InlineKeyboardButton(OBJ_NJ_AM['LOTERIA']     , callback_data = OBJ_NJ_AM['LOTERIA'])
        BTN_SOUTH_CAROLINA  = InlineKeyboardButton(OBJ_SC_AM2['LOTERIA']    , callback_data = OBJ_SC_AM2['LOTERIA'])
        BTN_NORTH_CAROLINA  = InlineKeyboardButton(OBJ_NC_AM['LOTERIA']     , callback_data = OBJ_NC_AM['LOTERIA'])
        BTN_PENNSYLVANIA    = InlineKeyboardButton(OBJ_PA_AM['LOTERIA']     , callback_data = OBJ_PA_AM['LOTERIA'])
        BTN_FLORIDA_USA     = InlineKeyboardButton(OBJ_FL_AM['LOTERIA']     , callback_data = 'FLORIDA-USA')
        BTN_WASHINGTON      = InlineKeyboardButton(OBJ_DC_AM['LOTERIA']     , callback_data = OBJ_DC_AM['LOTERIA'])
        BTN_VIRGINIA        = InlineKeyboardButton(OBJ_VA_AM['LOTERIA']     , callback_data = OBJ_VA_AM['LOTERIA'])
        BTN_CONNECTICUT     = InlineKeyboardButton(OBJ_CT_AM['LOTERIA']     , callback_data = OBJ_CT_AM['LOTERIA'])
        BTN_NEW_YORK_USA    = InlineKeyboardButton(OBJ_NY_AM['LOTERIA']     , callback_data = 'NEW_YORK-USA')

        markup.add(
            BTN_GEORGIA,
            BTN_MARYLAND,
            BTN_NEW_JERSEY,
            BTN_SOUTH_CAROLINA,
            BTN_NORTH_CAROLINA,
            BTN_PENNSYLVANIA,
            BTN_FLORIDA_USA,
            BTN_WASHINGTON,
            BTN_VIRGINIA,
            BTN_CONNECTICUT,
            BTN_NEW_YORK_USA
        )
        bot.send_message(cid, "Elige la loteria a Buscar.", reply_markup=markup)

    elif call.data == 'GEORGIA-USA': #? GEORGIA USA
        FECHAS[cid]['LOTERIA']=OBJ_GA_AM['LOTERIA']
        FECHAS[cid]['MODALIDAD']=OBJ_GA_AM['MODALIDAD']
        bot.delete_message(cid,mid)
        msg = Mensaje_elegiste_loteria(FECHAS[cid])
        msg_resultados = OBTENER_PREMIOS(FECHAS[cid])
        bot.send_message(cid, msg, reply_markup=markup)
        bot.send_message(cid, msg_resultados, reply_markup=markup, parse_mode='html')
        return 1

    elif call.data == 'FLORIDA-USA': #? FLORIDA USA
        FECHAS[cid]['LOTERIA']      = OBJ_FL_AM['LOTERIA']
        FECHAS[cid]['MODALIDAD']    = OBJ_FL_AM['MODALIDAD']
        bot.delete_message(cid,mid)
        msg = Mensaje_elegiste_loteria(FECHAS[cid])
        msg_resultados = OBTENER_PREMIOS(FECHAS[cid])
        bot.send_message(cid, msg, reply_markup=markup)
        bot.send_message(cid, msg_resultados, reply_markup=markup, parse_mode='html')
        return 1

    elif call.data == 'NEW_YORK-USA': #? NEW YORK
        FECHAS[cid]['LOTERIA']      = OBJ_NY_AM['LOTERIA']
        FECHAS[cid]['MODALIDAD']    = OBJ_NY_AM['MODALIDAD']
        bot.delete_message(cid,mid)
        msg = Mensaje_elegiste_loteria(FECHAS[cid])
        msg_resultados = OBTENER_PREMIOS(FECHAS[cid])
        bot.send_message(cid, msg, reply_markup=markup)
        bot.send_message(cid, msg_resultados, reply_markup=markup, parse_mode='html')
        return 1

    elif call.data == OBJ_MD_AM['LOTERIA']: #? MARYLAND
        FECHAS[cid]['LOTERIA']      = OBJ_MD_AM['LOTERIA']
        FECHAS[cid]['MODALIDAD']    = OBJ_MD_AM['MODALIDAD']
        bot.delete_message(cid,mid)
        msg = Mensaje_elegiste_loteria(FECHAS[cid])
        msg_resultados = OBTENER_PREMIOS(FECHAS[cid])
        bot.send_message(cid, msg, reply_markup=markup)
        bot.send_message(cid, msg_resultados, reply_markup=markup, parse_mode='html')
        return 1

    elif call.data == OBJ_NJ_AM['LOTERIA']: #? NEW JERSEY
        FECHAS[cid]['LOTERIA']      = OBJ_NJ_AM['LOTERIA']
        FECHAS[cid]['MODALIDAD']    = OBJ_NJ_AM['MODALIDAD']
        bot.delete_message(cid,mid)
        msg = Mensaje_elegiste_loteria(FECHAS[cid])
        msg_resultados = OBTENER_PREMIOS(FECHAS[cid])
        bot.send_message(cid, msg, reply_markup=markup)
        bot.send_message(cid, msg_resultados, reply_markup=markup, parse_mode='html')
        return 1

    elif call.data == OBJ_SC_AM2['LOTERIA']: #? SOUTH CAROLINA
        FECHAS[cid]['LOTERIA']      = OBJ_SC_AM2['LOTERIA']
        FECHAS[cid]['MODALIDAD']    = OBJ_SC_AM2['MODALIDAD']
        bot.delete_message(cid,mid)
        msg = Mensaje_elegiste_loteria(FECHAS[cid])
        msg_resultados = OBTENER_PREMIOS(FECHAS[cid])
        bot.send_message(cid, msg, reply_markup=markup)
        bot.send_message(cid, msg_resultados, reply_markup=markup, parse_mode='html')
        return 1

    elif call.data == OBJ_NC_AM['LOTERIA']: #? NORTH CAROLINA
        FECHAS[cid]['LOTERIA']      = OBJ_NC_AM['LOTERIA']
        FECHAS[cid]['MODALIDAD']    = OBJ_NC_AM['MODALIDAD']
        bot.delete_message(cid,mid)
        msg = Mensaje_elegiste_loteria(FECHAS[cid])
        msg_resultados = OBTENER_PREMIOS(FECHAS[cid])
        bot.send_message(cid, msg, reply_markup=markup)
        bot.send_message(cid, msg_resultados, reply_markup=markup, parse_mode='html')
        return 1

    elif call.data == OBJ_PA_AM['LOTERIA']: #? PENNSYLVANIA
        FECHAS[cid]['LOTERIA']      = OBJ_PA_AM['LOTERIA']
        FECHAS[cid]['MODALIDAD']    = OBJ_PA_AM['MODALIDAD']
        bot.delete_message(cid,mid)
        msg = Mensaje_elegiste_loteria(FECHAS[cid])
        msg_resultados = OBTENER_PREMIOS(FECHAS[cid])
        bot.send_message(cid, msg, reply_markup=markup)
        bot.send_message(cid, msg_resultados, reply_markup=markup, parse_mode='html')
        return 1

    elif call.data == OBJ_DC_AM['LOTERIA']: #? WASHINGTON
        FECHAS[cid]['LOTERIA']      = OBJ_DC_AM['LOTERIA']
        FECHAS[cid]['MODALIDAD']    = OBJ_DC_AM['MODALIDAD']
        bot.delete_message(cid,mid)
        msg = Mensaje_elegiste_loteria(FECHAS[cid])
        msg_resultados = OBTENER_PREMIOS(FECHAS[cid])
        bot.send_message(cid, msg, reply_markup=markup)
        bot.send_message(cid, msg_resultados, reply_markup=markup, parse_mode='html')
        return 1

    elif call.data == OBJ_VA_AM['LOTERIA']: #? VIRGINIA
        FECHAS[cid]['LOTERIA']      = OBJ_VA_AM['LOTERIA']
        FECHAS[cid]['MODALIDAD']    = OBJ_VA_AM['MODALIDAD']
        bot.delete_message(cid,mid)
        msg = Mensaje_elegiste_loteria(FECHAS[cid])
        msg_resultados = OBTENER_PREMIOS(FECHAS[cid])
        bot.send_message(cid, msg, reply_markup=markup)
        bot.send_message(cid, msg_resultados, reply_markup=markup, parse_mode='html')
        return 1

    elif call.data == OBJ_CT_AM['LOTERIA']: #? CONNECTICUT
        FECHAS[cid]['LOTERIA']      = OBJ_CT_AM['LOTERIA']
        FECHAS[cid]['MODALIDAD']    = OBJ_CT_AM['MODALIDAD']
        bot.delete_message(cid,mid)
        msg = Mensaje_elegiste_loteria(FECHAS[cid])
        msg_resultados = OBTENER_PREMIOS(FECHAS[cid])
        bot.send_message(cid, msg, reply_markup=markup)
        bot.send_message(cid, msg_resultados, reply_markup=markup, parse_mode='html')
        return 1

    else:
        bot.delete_message(cid,mid)
        del FECHAS[cid]
        print(FECHAS)

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
        #telebot.types.BotCommand('/resultados', 'Para consultar los premios'),
        telebot.types.BotCommand('/premios', 'Para consultar los premios')
    ])
    HILO_BOT = threading.Thread(name='HILO_BOT', target=recibir_mensaje)
    HILO_BOT.start()
    bot.send_message(MI_CHAT_ID, "INICIO EL BOT")