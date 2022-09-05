
from Funciones_Especiales import fecha, VALIDAR_QUE_NO_EXISTAN, PETICION_POST_PUBLICAR, sendNotification, saber_super_pale, CONSULTAR_NUMEROS_API
import time
from config import TIEMPO_A_ESPERAR, INTENTOS, URL_API_NODE_LDOMINICANA, BOT_NOTIFICACIONES
#? Con esta clase Obtengo los numeros
class Buscar_super_pale():

    def __init__(self, Datos):
        self.arr_loterias       =   saber_super_pale(Datos)
        self.URI_PETICION       =   URL_API_NODE_LDOMINICANA
        self.OBJ_super_pale_1   =   self.arr_loterias['LOTERIA_1']
        self.OBJ_super_pale_2   =   self.arr_loterias['LOTERIA_2']
        self.loteria            =   Datos['LOTERIA']
        self.sorteo             =   Datos['SORTEO']


    def Buscar_numeros_ganadores(self):
        print(f'INICIANDO BUSCADOR DE PREMIOS LOTERIA: {self.loteria} SORTEO: {self.sorteo}')
        validar                 = False
        publicar                = False
        self.fecha              = fecha('%d-%m-%Y')
        #self.fecha              = '04-09-2022'
        self.NUMERO_LOTERIA_1   = False
        self.NUMERO_LOTERIA_2   = False


        for intento in range (INTENTOS):
            COMPROBAR_QUE_NO_ESTEN = VALIDAR_QUE_NO_EXISTAN(self.URI_PETICION,self.loteria,self.sorteo,self.fecha)

            if(COMPROBAR_QUE_NO_ESTEN['PUBLICADO'] == True): #ES PORQUE YA ESTA PUBLICADO EN MONGO
                message = f"\nLOTERIA: {self.loteria} \n\nSORTEO: {self.sorteo} \n\nFECHA: {self.fecha} \n\n{COMPROBAR_QUE_NO_ESTEN['MESSAGE']}"
                print(message)
                sendNotification(True, message, BOT_NOTIFICACIONES['TOKEN'])
                validar = True
                break
            else: #ES PORQUE AUN NO ESTA PUBLICADO EN MONGO

                if(COMPROBAR_QUE_NO_ESTEN['ERROR'] == False):
                    publicar = self.publicar()

                    if(publicar['STATUS']): #SI ES TRUE SWE PUBLICO EN BASE DE DATO
                        message = publicar['MESSAGE']
                        print(message)
                        sendNotification(False, message, BOT_NOTIFICACIONES['TOKEN'])
                        validar = True
                        break
                    else:
                        print(publicar['MESSAGE']+ f' INTENTO # {intento}')
                        time.sleep(TIEMPO_A_ESPERAR)
                else:
                    print(COMPROBAR_QUE_NO_ESTEN['MESSAGE']) # AQUI MUESTRO SI HAY UN ERROR EN CONSOLA
                    time.sleep(TIEMPO_A_ESPERAR)


        if(validar == False):
            if(publicar):#NO SE PUBLICO
                message = publicar['MESSAGE']
                print(message)
                sendNotification(True, message,BOT_NOTIFICACIONES['TOKEN'])
            else:
                message = f"NO SE PUBLICO\n\n\nERROR: {COMPROBAR_QUE_NO_ESTEN['MESSAGE']} \n\nLOTERIA: {self.loteria}\n\nSORTEO: {self.sorteo}"
                print(message)
                sendNotification(True, message,BOT_NOTIFICACIONES['TOKEN'])

    def buscar_super_pale(self):
        if(self.NUMERO_LOTERIA_1 == False):
            super_pale_1 = CONSULTAR_NUMEROS_API(self.URI_PETICION,self.OBJ_super_pale_1['LOTERIA'],self.OBJ_super_pale_1['SORTEO'],self.fecha)
            if(super_pale_1['NUMEROS'] and super_pale_1['ERROR'] == False):
                self.NUMERO_LOTERIA_1 = True
            else:
                self.NUMERO_LOTERIA_1 = False
                print(super_pale_1['MESSAGE'])

        if(self.NUMERO_LOTERIA_2 == False):
            super_pale_2 = CONSULTAR_NUMEROS_API(self.URI_PETICION,self.OBJ_super_pale_2['LOTERIA'],self.OBJ_super_pale_2['SORTEO'],self.fecha)
            if(super_pale_2['NUMEROS'] and super_pale_2['ERROR'] == False):
                self.NUMERO_LOTERIA_2 = True
            else:
                self.NUMERO_LOTERIA_2 = False
                print(super_pale_2['MESSAGE'])

        if(self.NUMERO_LOTERIA_1 and self.NUMERO_LOTERIA_1):
            return {
                'NU_1'  :   super_pale_1['NUMEROS']['numeros_ganadores']['NU1'],
                'NU_2'  :   super_pale_2['NUMEROS']['numeros_ganadores']['NU1']
            }
        else:
            return False


    def publicar(self):

        NUMEROS_VALIDOS_A_PUBLICAR = self.buscar_super_pale()

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