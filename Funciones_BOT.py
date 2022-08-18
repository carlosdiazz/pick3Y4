import json, requests
from config import API_KEY_MONGO_DB
from Funciones_Especiales import Consultar_Numeros_BOT
from VARIABLES import MODALIDAD,MODALIDAD_RD

def Mensaje_start(name):

    text  =     f'<b>HOLA, {name}.</b>\n'
    text  +=      '<code>\nESTE ES EL BOT DE LOTERIAS</code>\n\n'
    text  +=     f'<b>Si desea consultar los premios de alguna loteria escriba /resultados, luego elige la fecha y loteria a consultar</b>\n'

    return text

def Mensaje_loteria_INDIVIDUAL(loteria, sorteo, fecha, numeros_ganadores,MODALIDAD):

    if(MODALIDAD == MODALIDAD_RD):
        text   =     f'<b>\nLOTERIA: </b><i> {loteria} </i>\n'
        text  +=     f'<b>\nSORTEO: </b><i> {sorteo} </i>\n'
        text  +=     f'<b>\nFECHA: </b><i> {fecha} </i>\n'
        text  +=     f'<b>\nNUMEROS: </b><i> {numeros_ganadores["NU1"]}-{numeros_ganadores["NU2"]}-{numeros_ganadores["NU3"]}\n</i>'
        text  +=     f'<b>------------------------------</b>'
        return text
    else:
        text   =     f'<b>\nLOTERIA: </b><i> {loteria} </i>\n'
        text  +=     f'<b>\nSORTEO: </b><i> {sorteo} </i>\n'
        text  +=     f'<b>\nFECHA: </b><i> {fecha} </i>\n'
        text  +=     f'<b>\nPICK3: </b><i> {numeros_ganadores["PICK3"]}\n</i>'
        text  +=     f'<b>\nPICK4: </b><i> {numeros_ganadores["PICK4"]}\n</i>'
        text  +=     f'<b>------------------------------</b>'
        return text

def OBTENER_USERS_MONGO():
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

def AGREGAR_USER_MONGO(user):
    try:
        ARR_USUARIOS = OBTENER_USERS_MONGO()

        if(ARR_USUARIOS):
            if(user in ARR_USUARIOS):
                print("YA EL USUARIO EXISTE EN MONGODB")
                return False
            else:
                url = "https://data.mongodb-api.com/app/data-rrmjk/endpoint/data/v1/action/insertOne"
                payload = json.dumps({
                    "collection": "usuarios",
                    "database": "myFirstDatabase",
                    "dataSource": "LoteriasCluster",
                    "document": { 'user_id': user}
                })
                headers = {
                    'Content-Type': 'application/json',
                    'Access-Control-Request-Headers': '*',
                    'api-key': API_KEY_MONGO_DB
                }
                requests.request("POST", url, headers=headers, data=payload)
                return True
        else:
            print("NO SE ENCONTRARON USUARIOS EN MONGODB")
            return False
    except:
        print("PASO UN EXCEPT EN LA FUNCION DE AGREGAR USERB")
        return False

def Mensaje_elegiste_loteria(arr):
    loteria = arr['LOTERIA']
    fecha   = arr["FECHA"]
    return f'Elegiste la loteria: {loteria} para la fecha: {fecha}'

def OBTENER_PREMIOS(arr):
    LOTERIA     = arr['LOTERIA']
    FECHA       = arr['FECHA']
    MODALIDAD   = arr['MODALIDAD']
    FECHA=FECHA.strftime('%d-%m-%Y') #Aqui convierto la fecha

    consulta_api=Consultar_Numeros_BOT(MODALIDAD,LOTERIA,FECHA)
    if(consulta_api['NUMEROS']):
        text  =      f'<code>\n -- <u>RESULTADOS</u> -- </code>\n'
        for i in consulta_api['NUMEROS']:
            loteria_actual              = i['loteria']
            sorteo_actual               = i['sorteo']
            fecha_actual                = i['fecha']
            numeros_ganadores_actual    = i['numeros_ganadores']
            mensaje_nuevo = Mensaje_loteria_INDIVIDUAL(loteria_actual,sorteo_actual,fecha_actual, numeros_ganadores_actual, MODALIDAD)
            text += mensaje_nuevo
        return text
    else:
        print(consulta_api['MESSAGE'])
        return 'NO SE ENCONTRARON LOS NUMEROS'


arr_prueba ={
    'LOTERIA'   :   'ANGUILLA',
    'FECHA'     :   '17-08-2022',
    'MODALIDAD' :   'DOMINICANA'
}

#print(OBTENER_PREMIOS(arr_prueba))