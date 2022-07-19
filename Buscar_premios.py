from Funciones_Especiales import devolver_arreglo, fecha, VALIDAR_QUE_NO_EXISTAN, Peticion_Post_Publicar
from API_USA import API
import time
import config

#? Con esta clase Obtengo los numeros
class Buscar_Premio():

    def __init__(self, Datos):
        self.loteria = Datos['LOTERIA']
        self.sorteo = Datos['SORTEO']
        self.fecha = fecha('%d-%m-%Y')
        self.datos = Datos
        self.intentos=0

    def Buscar_numeros_ganadores(self):

        publicar_numeros = VALIDAR_QUE_NO_EXISTAN(config.URL_API_NODE,self.loteria,self.sorteo,self.fecha)
        #!Crear funcion que valide que no existen en la base de datos
        if(publicar_numeros == True):
            arreglo_loteria = devolver_arreglo(self.datos)
            numeros_ganadores = API().devolver_numeros(arreglo_loteria,self.sorteo)
            if(numeros_ganadores):
                publicar = Peticion_Post_Publicar(config.URL_API_NODE,self.loteria,self.sorteo,numeros_ganadores,self.fecha)
                if(publicar == True):
                    self.intentos=0
                    print(f'Loteria: {self.loteria} con sorteo: {self.sorteo} y {numeros_ganadores} se publico Bien')
                #return {
                #    'LOTERIA'       : self.loteria,
                #    'SORTEO'        : self.sorteo,
                #    'NUMEROS'       : numeros_ganadores,
                #    'FECHA'         : self.fecha,
                #    "AGREGADO_POR"  : "BOT"
                #}
                else:
                    self.intentos=self.intentos+1
                    print(f"No se pudo publicar en NODE esta loteria:{self.loteria} con este sorteo: {self.sorteo} intento #:{self.intentos}")
                    time.sleep(30)
                    self.Buscar_numeros_ganadores()
            else:
                self.intentos=self.intentos+1
                if(self.intentos<150):
                    print(f"No se encontro esta loteria:{self.loteria} con este sorteo: {self.sorteo} intento #:{self.intentos}")
                    time.sleep(30)
                    self.Buscar_numeros_ganadores()
                else:
                    print("No se encontro esta loteria")
                    return False
        else:
            print("Ya la loteria existe")
            return False
