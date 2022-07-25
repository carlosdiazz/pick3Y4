# ESTE ARCHIVO ES QUIEN BUSCA LOS NUMEROS GANADORES VARIAS VECES HASTA ENCONTRARLO Y PUBLICARLO EN MONGODB
from VARIABLES import MODALIDAD, MODALIDAD_RD
from Funciones_Especiales import DEVOLVER_ARREGLO_XPATH, fecha, VALIDAR_QUE_NO_EXISTAN, PETICION_POST_PUBLICAR, sendNotification
from API_USA_PICK import API_USA_PICK
from API_DOMINICANAS import API_DOMINICANA
import time
import config
from config import TIEMPO_A_ESPERAR, INTENTOS
#? Con esta clase Obtengo los numeros
class Buscar_Premio():

    def __init__(self, Datos):
        self.loteria    = Datos['LOTERIA']
        self.sorteo     = Datos['SORTEO']
        self.MODALIDAD  = Datos['MODALIDAD']
        self.datos      = Datos

    def Buscar_numeros_ganadores(self):
        print(f'INICIANDO BUSCADOR DE PREMIO {self.loteria} {self.sorteo}')
        validar     = False
        publicar    = False
        self.fecha = fecha('%d-%m-%Y')

        if(self.MODALIDAD == MODALIDAD):
            self.URI_PETICION = config.URL_API_NODE_LAMERICANA
        elif(self.MODALIDAD == MODALIDAD_RD):
            self.URI_PETICION = config.URL_API_NODE_LDOMINICANA

        for intento in range (INTENTOS):
            COMPROBAR_QUE_NO_ESTEN = VALIDAR_QUE_NO_EXISTAN(self.URI_PETICION,self.loteria,self.sorteo,self.fecha)

            if(COMPROBAR_QUE_NO_ESTEN['PUBLICADO'] == True):
                message = f"\nLOTERIA: {self.loteria} \n\nSORTEO: {self.sorteo} \n\nFECHA: {self.fecha} \n\n{COMPROBAR_QUE_NO_ESTEN['MESSAGE']}"
                print(message)
                sendNotification(message, config.BOT_NOTIFICACIONES['TOKEN'])
                validar = True
                break
            else:
                if(COMPROBAR_QUE_NO_ESTEN['ERROR'] == False):
                    publicar = self.publicar()

                    if(publicar['STATUS']):
                        message = publicar['MESSAGE']
                        print(message)
                        sendNotification(message, config.BOT_NOTIFICACIONES['TOKEN'])
                        validar = True
                        break
                    else:
                        print(publicar['MESSAGE']+ f' INTENTO # {intento}')
                        time.sleep(TIEMPO_A_ESPERAR)
                else:
                    print(COMPROBAR_QUE_NO_ESTEN['MESSAGE'])
                    time.sleep(TIEMPO_A_ESPERAR)


        if(validar == False):
            if(publicar):
                message = publicar['MESSAGE']
                print(message)
                sendNotification(message,config.BOT_NOTIFICACIONES['TOKEN'])
            else:
                message = f"NO SE PUBLICO\n\n\nERROR: {COMPROBAR_QUE_NO_ESTEN['MESSAGE']} \n\nLOTERIA: {self.loteria}\n\nSORTEO: {self.sorteo}"
                print(message)
                sendNotification(message,config.BOT_NOTIFICACIONES['TOKEN'])

    def publicar(self):

        if(self.MODALIDAD == 'AMERICANA'):
            ARR_LOTERIA_XPATH = DEVOLVER_ARREGLO_XPATH(self.datos)
            NUMEROS_VALIDOS_A_PUBLICAR = API_USA_PICK().devolver_numeros(ARR_LOTERIA_XPATH,self.sorteo)

        else:
            ARR_LOTERIA_XPATH = DEVOLVER_ARREGLO_XPATH(self.datos)
            NUMEROS_VALIDOS_A_PUBLICAR = API_DOMINICANA().devolver_numeros(ARR_LOTERIA_XPATH)

        if(NUMEROS_VALIDOS_A_PUBLICAR):
            publicar = PETICION_POST_PUBLICAR(self.URI_PETICION,self.loteria,self.sorteo,NUMEROS_VALIDOS_A_PUBLICAR,self.fecha)
            if(publicar == True):
                message = f'SE PUBLICO BIEN EN B.D \n\nLoteria: {self.loteria} \n\nSorteo: {self.sorteo} \n\nNUMEROS GANADORES: {NUMEROS_VALIDOS_A_PUBLICAR}'
                return {'STATUS': True, 'MESSAGE':message}
            else:
                message = f"NO SE PUDO PUBLICAR EN NODE\n\nLOTERIA: {self.loteria} \n\nSORTEO: {self.sorteo}"
                return {'STATUS': False,  'MESSAGE':message}
        else:
            message = f"NO SE ENCONTRARON EN LA PAGINA OFICIALES LOS NUMEROS PARA\n\nLOTERIA: {self.loteria} \n\nSORTEO: {self.sorteo}"
            return {'STATUS': False,  'MESSAGE':message}

