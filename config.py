from datetime import datetime
## MI ARICHO DE CONFIGURACION BASICA COMO VARIABLES DE ENTORNOS

URL_API_NODE_LAMERICANA = 'http://localhost:4000/api/v1/loterias'

URL_API_NODE_LDOMINICANA = 'http://localhost:4000/api/v1/loteriasRD'

BOT_NOTIFICACIONES = {
    'TOKEN' : '5482263496:AAHvO_eI-ipwF3n-OLs2wAjNrW3VXwQD-YM'
}

BOT_PREMIAR_MEGALOTTERY = {
    'TOKEN' : '5451666219:AAF3KWQeE1JlC_gK-dYkJpLs_JBFqoa9FGI'
}

#?Configuracion MONGO DB
API_KEY_MONGO_DB = 'raLTadjYvDiA8Yj9GWWAPgJmH3DPFmy2cYLQrntaRoZI9OkyX2Fg3nnDmbkUKdbJ'

#INTENTOS = 20
#TIEMPO_A_ESPERAR = 60
#TIEMPO_A_BUSCAR = 120

INTENTOS = 10
TIEMPO_A_ESPERAR = 1
TIEMPO_A_BUSCAR = 1

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