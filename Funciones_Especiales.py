import os
import threading
from datetime import datetime
from VARIABLES import *
import requests
import json
from config import API_KEY_MONGO_DB

def fecha(tipo_fecha):
    return datetime.today().strftime(tipo_fecha)

mesesDic = {
    "01":'Enero',
    "02":'Febrero',
    "03":'Marzo',
    "04":'Abril',
    "05":'Mayo',
    "06":'Junio',
    "07":'Julio',
    "08":'Agosto',
    "09":'Septiembre',
    "10":'Octubre',
    "11":'Noviembre',
    "12":'Diciembre'
}

diasSemanaEso = {
    'Monday' : 'LUNES',
    'Tuesday' : 'MARTES',
    'Wednesday' : 'MIÉRCOLES',
    'Thursday' : 'JUEVES',
    'Friday' : 'VIERNES',
    'Saturday' : 'SÁBADO',
    'Sunday' : 'DOMINGO'
}

def Validar_Fecha_Hoy(fecha_comprobar):

    ANGUILA_MANANA = 'Draw 10:00AM. '+fecha('%d/%m/%Y')
    ANGUILA_MEDIO_DIA = 'Draw 1:00PM. '+fecha('%d/%m/%Y')
    ANGUILA_TARDE = 'Draw 6:00PM. '+fecha('%d/%m/%Y')
    ANGUILA_NOCHE = 'Draw 9:00PM. '+fecha('%d/%m/%Y')
    mes_espanol=mesesDic[fecha('%m')]
    dia_espanol=diasSemanaEso[fecha('%A')]
    fecha_dia_un_digito = fecha('%d')
    fecha_dia_un_digito=fecha_dia_un_digito.lstrip('0')

    Todas_las_Fechas = [

    fecha(f'%A, %B {fecha_dia_un_digito}, %Y'),
    fecha('%A, %b %d, %Y'),
    fecha(f'%A, %b {fecha_dia_un_digito}, %Y'),
    fecha(f'%A %B {fecha_dia_un_digito}th %Y'),
    fecha(f'%A %B {fecha_dia_un_digito}st %Y'),
    fecha(f'%A %B {fecha_dia_un_digito}nd %Y'),
    fecha(f'%A %B {fecha_dia_un_digito}rd %Y'),
    fecha('%a %m/%d/%Y'),
    fecha('%A %B %dth %Y'),
    fecha('%a %m/%d/%y'),
    fecha('%A, %B %d, %Y'),
    fecha('%d-%m-%Y'),
    fecha('%d/%m/%Y'),
    fecha('%Y-%m-%d'),
    fecha(f'Sorteo: %d de {mes_espanol} del %Y.'),
    fecha(f'{dia_espanol}, %d-%m-%Y'),
    fecha('Resultados %d/%m/%Y'),
    ANGUILA_MANANA,
    ANGUILA_MEDIO_DIA,
    ANGUILA_TARDE,
    ANGUILA_NOCHE
    ]
    if fecha_comprobar in Todas_las_Fechas:
        return True
    else:
        #! AQUI TENGO QUE DEVOLVER FALSO ES UNA PRUEBA
        return False

def Validar_Fecha_hoy2(ArrFECHAS, fecha):
    if fecha in ArrFECHAS:
        return True
    else:
        #! AQUI TENGO QUE DEVOLVER FALSO ES UNA PRUEBA
        return False


def Fechas_hoy():

    ANGUILA_MANANA = 'Draw 10:00AM. '+fecha('%d/%m/%Y')
    ANGUILA_MEDIO_DIA = 'Draw 1:00PM. '+fecha('%d/%m/%Y')
    ANGUILA_TARDE = 'Draw 6:00PM. '+fecha('%d/%m/%Y')
    ANGUILA_NOCHE = 'Draw 9:00PM. '+fecha('%d/%m/%Y')
    mes_espanol=mesesDic[fecha('%m')]
    dia_espanol=diasSemanaEso[fecha('%A')]
    fecha_dia_un_digito = fecha('%d')
    fecha_dia_un_digito=fecha_dia_un_digito.lstrip('0')

    Todas_las_Fechas = [

    fecha(f'%A, %B {fecha_dia_un_digito}, %Y'),
    fecha('%A, %b %d, %Y'),
    fecha(f'%A, %b {fecha_dia_un_digito}, %Y'),
    fecha(f'%A %B {fecha_dia_un_digito}th %Y'),
    fecha(f'%A %B {fecha_dia_un_digito}st %Y'),
    fecha(f'%A %B {fecha_dia_un_digito}nd %Y'),
    fecha(f'%A %B {fecha_dia_un_digito}rd %Y'),
    fecha('%A %B %dth %Y'),
    fecha('%a %m/%d/%y'),
    fecha('%A, %B %d, %Y'),
    fecha('%d-%m-%Y'),
    fecha('%d/%m/%Y'),
    fecha('%Y-%m-%d'),
    fecha(f'Sorteo: %d de {mes_espanol} del %Y.'),
    fecha(f'{dia_espanol}, %d-%m-%Y'),
    fecha('Resultados %d/%m/%Y'),
    ANGUILA_MANANA,
    ANGUILA_MEDIO_DIA,
    ANGUILA_TARDE,
    ANGUILA_NOCHE
    ]
    return Todas_las_Fechas

def solo_Numero(numero):
    if(len(numero)>=2):
        numero=numero[len(numero)-2:]
        caracteres = ['1','2','3','4','5','6','7','8','9','0']
        newNumero = ""
        for i in numero:
            if(i in caracteres):
                newNumero+=i
        return newNumero
    else:
        return numero


def solo_undigito(numero):
    numero=solo_Numero(numero)
    if(len(numero) == 1):
        return f'0{numero}'
    else:
        return numero


def comprobar_pick3(arr):
    if(type(arr)==list):
        if(len(arr)==3):
            return f'{arr[0]}{arr[1]}{arr[2]}'
        return False
    else:
        return False

def comprobar_pick4(arr):
    if(type(arr)==list):
        if(len(arr)==4):
            return f'{arr[0]}{arr[1]}{arr[2]}{arr[3]}'
        return False
    else:
        return False

def run(job_func):
    job_thread = threading.Thread(target=job_func)
    job_thread.start()

def VALIDAR_QUE_NO_EXISTAN(url,loteria,sorteo,fecha):
    try:
        url = f'{url}?loteria={loteria}&sorteo={sorteo}&fecha={fecha}'
        r=requests.get(url)
        if(r.status_code == 200):
            res=(r.json())
            if(len(res['message']) == 0):
                return {
                        "ERROR"     :   False,
                        'PUBLICADO' :   False,
                        "MESSAGE"   :   'LOS NUMEROS NO ESTAN PUBLICADOS EN MONGO AUN'
                        }
            else:
                return {
                        "ERROR"     :   False,
                        'PUBLICADO' :   True,
                        "MESSAGE"   :   'LOS NUMEROS YA ESTAN PUBLICADOS'
                        }

        else:
            return {
                    "ERROR"     :   True,
                    'PUBLICADO' :   False,
                    "MESSAGE"   :   'El SERVIDOR NO RESPONDIO'
                    }

    except:
        return {
                "ERROR"     :   True,
                'PUBLICADO' :   False,
                "MESSAGE"   :   'ERROR EN LA PETICION GET'
                }

def PETICION_POST_PUBLICAR(url, Loteria, Sorteo, Numeros_ganadores, Fecha):
    try:
        saber_publicado = CONSULTAR_NUMEROS_API(url,Loteria,Sorteo,Fecha)

        if(saber_publicado['MESSAGE'] == 'AUN EL NUMERO NO ESTA PUBLICADO EN LA BASE DE DATOS'):

            url = f'{url}?loteria={Loteria}&sorteo={Sorteo}&fecha={Fecha}'
            headers = { 'Content-Type': 'application/json'}
            body= json.dumps({
                "loteria": Loteria,
                "sorteo":Sorteo,
                'numeros_ganadores':Numeros_ganadores,
                "fecha" : Fecha,
                "agregado_por": 'BOT'
            })

            Peticion_POST=requests.post(url, headers=headers, data= body)
            if(Peticion_POST.status_code == 201):
                return True
            else:
                return False
        else:
            return False
    except:
        #print(f'\n\n\nNO SE PREMIO ESTA LOTERIA: {Loteria} CON ESTE SORTEO {Sorteo} -------> El SERVIDOR EXPRES NO RESPONDE' )
        return False


def CONSULTAR_NUMEROS_API(urlAPI, loteria,sorteo,fecha):
    try:
        url = f'{urlAPI}?loteria={loteria}&sorteo={sorteo}&fecha={fecha}'
        r=requests.get(url)
        if(r.status_code == 200):
            res=(r.json())
            if(len(res['message']) == 1):
                #Se encontro el numero
                return {
                    "ERROR"     :   False,
                    "MESSAGE"   :   'LOS NUMEROS ESTAN EN LA BASE DATOS',
                    'NUMEROS'   :   res['message'][0]
                }
            else:
                #No se encontro el numero
                return {
                    "ERROR"     :   False,
                    "MESSAGE"   :   "AUN EL NUMERO NO ESTA PUBLICADO EN LA BASE DE DATOS",
                    'NUMEROS'   :   False
                }
        else:
            #Hubo un error en la peticion
            return {
                    "ERROR"     :   True,
                    "MESSAGE"   :   "HUBO UN ERROR EN LA PETICION GET",
                    'NUMEROS'   :   False
                }
    except:
        #Fallo externo
        return  {
                    "ERROR"     :   True,
                    "MESSAGE"   :   "NO SE PUDO HACER LA PETICION GET",
                    'NUMEROS'   :   False
                }

def saber_sorteo(sorteo):
    if(sorteo == 'MIDDAY'):
        return 'AM'
    elif(sorteo == 'EVENING'):
        return 'PM'
    elif(sorteo == 'NIGHT'):
        return 'NIGHT'

def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)

#! -------- ENVIAR NOTIFICACIONE DE LOS RESULTADOS

def Obtener_User_MONGO_NOTIFICACIONES():
    try:
        url = "https://data.mongodb-api.com/app/data-rrmjk/endpoint/data/v1/action/find"
        payload = json.dumps({
            "collection": "usuarios",
            "database": "myFirstDatabase",
            "dataSource": "LoteriasCluster",
            "projection": {

            }
        })
        headers = {
            'Content-Type': 'application/json',
            'Access-Control-Request-Headers': '*',
            'api-key': API_KEY_MONGO_DB
        }
        response = requests.request("POST", url, headers=headers, data=payload)
        arr=response.json()

        New_Arr = []
        for user in arr['documents']:
            usuarios = user['user_id']
            New_Arr.append(usuarios)
        return New_Arr
    except:
        print("NO SE PUDO OBTENER LOS USUARIOS PARA ENVIAR LA NOTIFICACION")
        return False

def sendNotification(message,token ):
    try:
        bot_token = token
        User=Obtener_User_MONGO_NOTIFICACIONES()
        if(User):
            for usuarios in User:
                send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + usuarios + '&parse_mode=Markdown&text=' + message
                requests.get(send_text)
            return True
        else:
            print('NO HAY USUARIO PARA PREMIAR')
            return False

    except:
        print('-----------------------------------------------------------------------')
        print("NO SE PUEDO ENVIAR LA NOTIFICACION DE TELEGRAM")
        print('-----------------------------------------------------------------------')
        return False

def convertir_a_DOMINICANO(obj):
    return{
        'NU1'   :   obj['PICK3'][1:3],
        'NU2'   :   obj['PICK4'][0:2],
        'NU3'   :   obj['PICK4'][2:4]
    }

#? AGREGAR LOS DEMAS NOMBRES A CAMBIAR
def Convertir_nombre_sorteo(namePlataforma,sorteo, loteria):

    if(namePlataforma == 'RAPIDITA'):
        if(sorteo == OBJ_PRIMERA_PM['SORTEO']):
            return 'NOCHE'
        else:
            return sorteo
    elif(namePlataforma == 'DESARROLLO'):
        if(sorteo == OBJ_NEW_YORK_RD_AM['SORTEO'] and loteria == OBJ_NEW_YORK_RD_AM['LOTERIA']):
            return 'NEW YORK AM'
        elif(sorteo == OBJ_FLORIDA_RD_AM['SORTEO'] and loteria == OBJ_FLORIDA_RD_AM['LOTERIA']):
            return 'FLORIDA'
        else:
            return sorteo
    elif(namePlataforma == 'LOTEDOM'):
        if(sorteo == OBJ_NEW_YORK_RD_PM['SORTEO'] and loteria == OBJ_NEW_YORK_RD_PM['LOTERIA']):
            return 'NEW YORK NOCHE'
        elif(sorteo == OBJ_FLORIDA_RD_PM['SORTEO'] and loteria == OBJ_FLORIDA_RD_PM['LOTERIA']):
            return 'FLORIDA PM'
        else:
            return sorteo
    else:
        return sorteo

#? AGREGAR LOS DEMAS NOMBRES A CAMBIAR
def Convertir_nombre_loteria(namePlataforma,loteria):

    if(namePlataforma == 'RAPIDITA'):
        if(loteria == OBJ_PRIMERA_PM['LOTERIA']):
            return '12M'
        else:
            return loteria
    else:
        return loteria

def Response(StatusError, Message,Status ):
    return {
        'StatusError'   :   StatusError,
        'Message'       :   Message,
        'Status'        :   Status
    }