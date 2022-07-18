from Funciones_Especiales import devolver_arreglo, fecha
from API_USA import API
import time

#? Con esta clase Obtengo los numeros
class Buscar_Premio():

    def __init__(self, Datos):
        self.loteria = Datos['LOTERIA']
        self.sorteo = Datos['SORTEO']
        self.datos = Datos
        self.intentos=0

    def Buscar_numeros_ganadores(self):

        #!Crear funcion que valide que no existen en la base de datos
        if(True):
            arreglo_loteria = devolver_arreglo(self.datos)
            numeros_ganadores = API().devolver_numeros(arreglo_loteria,self.sorteo)
            if(numeros_ganadores):
                self.intentos=0
                print(
                    {
                        'LOTERIA'       : self.loteria,
                        'SORTEO'        : self.sorteo,
                        'NUMEROS'       : numeros_ganadores,
                        'FECHA'         : fecha('%d-%m-%Y'),
                        "AGREGADO_POR"  : "BOT"
                    }
                )
                return {
                    'LOTERIA'       : self.loteria,
                    'SORTEO'        : self.sorteo,
                    'NUMEROS'       : numeros_ganadores,
                    'FECHA'         : fecha('%d-%m-%Y'),
                    "AGREGADO_POR"  : "BOT"
                }
            else:
                self.intentos=self.intentos+1
                if(self.intentos<150):
                    print(f"No se encontro esta loteria:{self.loteria} con este sorteo: {self.sorteo} intento #:{self.intentos}")
                    time.sleep(30)
                    self.Buscar_numeros_ganadores()
                else:
                    print("No se encontro esta loteria")
                    return False
                    print("No se encontro esta loteria")
        else:
            print("Ya la loteria existe")
            return False
