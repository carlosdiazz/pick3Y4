from datetime import datetime
from VARIABLES_ENTORNO import *

## MI ARICHO DE CONFIGURACION BASICA COMO VARIABLES DE ENTORNOS

URL_API_NODE_LAMERICANA = 'http://localhost:4000/api/v1/loterias'

URL_API_NODE_LDOMINICANA = 'http://localhost:4000/api/v1/loteriasRD'

BOT_NOTIFICACIONES = {
    'TOKEN' : os.getenv('TOKEN_NOTIFICACIONES')
}

BOT_PREMIAR_MEGALOTTERY = {
    'TOKEN' : os.getenv("TOKEN_PREMIAR")
}

BOT_TELEGRAM_PADRE = {
    'TOKEN' : os.getenv("TOKEN_BOT_PADRE")
}

#Configuracion MONGO DB
API_KEY_MONGO_DB    = os.getenv("API_MONGO_DB")
#INTENTOS A REPETIR
INTENTOS            = int(os.getenv("INTENTOS"))
#INTERVALO DE TIEMPO A ESPERAR
TIEMPO_A_ESPERAR    = int(os.getenv("TIEMPO_A_ESPERAR"))
#TIEMPO A ESPERAR A BUSCAR DE NUEVO
TIEMPO_A_BUSCAR     = int(os.getenv("TIEMPO_A_BUSCAR"))


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