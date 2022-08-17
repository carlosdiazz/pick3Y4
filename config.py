from datetime import datetime
from VARIABLES_ENTORNO import *

## MI ARICHO DE CONFIGURACION BASICA COMO VARIABLES DE ENTORNOS

#URL DE LA API DE DONDE SACARE LAS LOTERIAS AMERICANA
URL_API_NODE_LAMERICANA = 'http://localhost:4000/api/v1/loterias'

#URL DE LA API DE DONDE SACARE LAS LOTERIAS DOMINICANA
URL_API_NODE_LDOMINICANA = 'http://localhost:4000/api/v1/loteriasRD'

#BOT PARA ENVIAR NOTIFICACIONES
BOT_NOTIFICACIONES = {
    'TOKEN' : os.getenv('TOKEN_NOTIFICACIONES')
}

#BOT GENERAL PARA PREMIAR TODAS LAS PLATAFORMAS
BOT_PREMIAR = {
    'TOKEN' : os.getenv("TOKEN_PREMIAR")
}

#Configuracion MONGO DB
API_KEY_MONGO_DB    = os.getenv("API_MONGO_DB")

#INTENTOS A REPETIR
INTENTOS            = int(os.getenv("INTENTOS"))

#INTERVALO DE TIEMPO A ESPERAR
TIEMPO_A_ESPERAR    = int(os.getenv("TIEMPO_A_ESPERAR"))

#TIEMPO A ESPERAR A BUSCAR DE NUEVO
TIEMPO_A_BUSCAR     = int(os.getenv("TIEMPO_A_BUSCAR"))

#TOKEN TELEGRAM PADRE BOT
TOKEN_TELEGRAM      = os.getenv('TOKEN_BOT_PADRE')

#TOKEN DEL SERVER NGROK
NGROK_TOKEN         = os.getenv('NGROK_TOKEN')

#MI ID DE TELEGRAM PARA ENVIARME UN MENSAJE CADA VEZ QUE IINICA EL BOT
MI_CHAT_ID          = int(os.getenv('MI_CHAT_ID'))


#UNA FUNCION PARA TENER LA HORA 5 SEGUNDO DESPUES,SOLO SI LOS SEGUNDO SON MENORES QUE 54
def segundo_extra(seg):
    if(int(seg)>54):
        return '05'
    else:
        return f'{int(seg)+5}'

date = datetime.now()
segundo = segundo_extra(date.time().strftime("%S"))
HORA_MINUTO = date.time().strftime("%H:%M")
hora_prueba = f'{HORA_MINUTO}:{segundo}'