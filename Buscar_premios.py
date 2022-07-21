# ESTE ARCHIVO ES QUIEN BUSCA LOS NUMEROS GANADORES VARIAS VECES HASTA ENCONTRARLO Y PUBLICARLO EN MONGODB

from Funciones_Especiales import DEVOLVER_ARREGLO_XPATH, fecha, VALIDAR_QUE_NO_EXISTAN, PETICION_POST_PUBLICAR
from API_USA_PICK import API_USA_PICK
import time
import config

#? Con esta clase Obtengo los numeros
class Buscar_Premio():

    def __init__(self, Datos):
        self.loteria    = Datos['LOTERIA']
        self.sorteo     = Datos['SORTEO']
        self.datos      = Datos
        self.intentos   = 0

    def Buscar_numeros_ganadores(self):
        try:
            self.fecha = fecha('%d-%m-%Y')
            COMPROBAR_QUE_NO_ESTEN = VALIDAR_QUE_NO_EXISTAN(config.URL_API_NODE,self.loteria,self.sorteo,self.fecha)

            if(COMPROBAR_QUE_NO_ESTEN['PUBLICADO'] == False):

                ARR_LOTERIA_XPATH = DEVOLVER_ARREGLO_XPATH(self.datos)
                NUMEROS_VALIDOS_A_PUBLICAR = API_USA_PICK().devolver_numeros(ARR_LOTERIA_XPATH,self.sorteo)

                if(NUMEROS_VALIDOS_A_PUBLICAR):
                    publicar = PETICION_POST_PUBLICAR(config.URL_API_NODE,self.loteria,self.sorteo,NUMEROS_VALIDOS_A_PUBLICAR,self.fecha)
                    if(publicar == True):
                        self.intentos=0
                        print(f'Loteria: {self.loteria} con sorteo: {self.sorteo} y {NUMEROS_VALIDOS_A_PUBLICAR} se publico Bien EN LA BASE DE DATOS')
                        #return True #! ----ME FALTA enviar NOTIFICACION TELEGRAM -------------------------------------------------------------------------------

                    else:
                        self.intentos=self.intentos+1
                        print(f"No se pudo publicar en NODE esta loteria:{self.loteria} con este sorteo: {self.sorteo} intento #:{self.intentos}")
                        time.sleep(1)
                        self.Buscar_numeros_ganadores()
                else:
                    print(NUMEROS_VALIDOS_A_PUBLICAR)
                    self.intentos=self.intentos+1
                    if(self.intentos<100):
                        print(f"No se encontro esta loteria:{self.loteria} con este sorteo: {self.sorteo} intento #:{self.intentos}")
                        time.sleep(1)
                        self.Buscar_numeros_ganadores()
                    else:
                        print(f"ERROR PASARON TODOS LOS INTENTOS Y NO SE PUBLICO... LOTERIA: {self.loteria} SORTEO: {self.sorteo} INTENTO#: {self.intentos}")
                        self.intentos=0
                        return False  #! ---- ME FALTA enviar NOTIFICACION TELEGRAM NO SE ENVIO -------------------------------------------------------------------------------

            else:
                print(COMPROBAR_QUE_NO_ESTEN['MESSAGE'] +f' Para La LOTERIA: => {self.loteria} con el SORTEO => {self.sorteo}')

        except:
            print('ERROR ENTRE EN EXCEPT DEL ARCHIVO BUSCAR PREMIO')
            time.sleep(1)
            self.intentos=self.intentos+1
            self.Buscar_numeros_ganadores()

