import json, requests
from config import API_KEY_MONGO_DB

def Mensaje_start(name):

    text  =     f'<b>HOLA, {name}.</b>\n'
    text  +=      '<code>\nESTE ES EL BOT DE LOTERIAS</code>\n\n'
    text  +=     f'<b>Si desea consultar los premios de alguna loteria escriba /resultados, luego elige la fecha y loteria a consultar</b>\n'

    return text

def Mensaje_loteria(loteria, sorteo, fecha, numeros_ganadores):

    text  =      f'<code>\n -- <u>RESULTADOS</u> -- </code>\n\n'
    text  +=     f'<b>\nLOTERIA: </b><i> {loteria} </i>\n'
    text  +=     f'<b>\n SORTEO: </b><i> {sorteo} </i>\n'
    text  +=     f'<b>\n  FECHA: </b><i> {fecha} </i>\n'
    text  +=     f'<b>\nNUMEROS: </b><i> {numeros_ganadores["NU1"]}-{numeros_ganadores["NU2"]}-{numeros_ganadores["NU3"]} </i>'
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