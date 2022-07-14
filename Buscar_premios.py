import threading
import schedule
from Funciones_Especiales import devolver_arreglo, fecha
from API_USA import API
import VARIABLES
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
            numeros_ganadores = API().devolver_numeros(arreglo_loteria)
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



LOTERY_FLORIDA_AM       =   (Buscar_Premio(VARIABLES.OBJ_FL_AM).Buscar_numeros_ganadores)
LOTERY_FLORIDA_PM       =   (Buscar_Premio(VARIABLES.OBJ_FL_PM).Buscar_numeros_ganadores)

LOTERY_NEW_YORK_AM      =   (Buscar_Premio(VARIABLES.OBJ_NY_AM).Buscar_numeros_ganadores)
LOTERY_NEW_YORK_PM      =   (Buscar_Premio(VARIABLES.OBJ_NY_PM).Buscar_numeros_ganadores)

LOTERY_NEW_JERSEY_AM    =   (Buscar_Premio(VARIABLES.OBJ_NJ_AM).Buscar_numeros_ganadores)
LOTERY_NEW_JERSEY_PM    =   (Buscar_Premio(VARIABLES.OBJ_NJ_PM).Buscar_numeros_ganadores)

def run_threaded(job_func):
    job_thread = threading.Thread(target=job_func)
    job_thread.start()

#! HORARIO DE BUSCAR NUMEROS
schedule.every().day.at("16:43:00").do(run_threaded, LOTERY_FLORIDA_AM)
schedule.every().day.at("16:43:00").do(run_threaded, LOTERY_FLORIDA_PM)
schedule.every().day.at("16:43:00").do(run_threaded, LOTERY_NEW_YORK_AM)
schedule.every().day.at("16:43:00").do(run_threaded, LOTERY_NEW_YORK_PM)
schedule.every().day.at("16:43:00").do(run_threaded, LOTERY_NEW_JERSEY_AM)
schedule.every().day.at("16:43:00").do(run_threaded, LOTERY_NEW_JERSEY_PM)

while True:
    fecha_actual = fecha('%d-%m-%Y || %H:%M:%S')
    print(f"|----------> {fecha_actual} <----------|")
    saber = schedule.run_pending()
    if(saber == None):
        pass
    else:
        print(schedule.run_pending())
    time.sleep(1)