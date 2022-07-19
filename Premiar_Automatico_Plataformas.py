import schedule
import VARIABLES
from PUBLICAR_NUMEROS import Publicar_En_Plataformas
from Funciones_Especiales import fecha, run, CONSULTAR_NUMEROS_API, saber_sorteo
import time
from config import user_desarrollo
from Datos_Loterias.DATOS_PLATAFORMA import PLATAFORMA_DEV, PLATAFORMA_MEGA

class Buscar_Numeros_Premiar():

    def __init__(self, obj):
        self.loteria = obj['LOTERIA']
        self.sorteo = obj['SORTEO']

    def buscar(self):
        #? Con esta funcion buscare los numeros ganadores
        self.fecha = fecha('%d-%m-%Y')                                                  #! -------------- QUITAR ESTA FECHA MALA
        numeros = CONSULTAR_NUMEROS_API(self.loteria,self.sorteo,self.fecha)
        #print(numeros['message'][0])
        if(numeros['error'] == False):
            loteria_a_publicar = numeros['message'][0]

            arrp3 = {
                'loteria'           :   'PICK 3',
                'fecha'             :   loteria_a_publicar['fecha'],
                "sorteo"            :   loteria_a_publicar['loteria'] +" "+saber_sorteo(loteria_a_publicar['sorteo']),
                'numeros_ganadores' :   loteria_a_publicar['numeros_ganadores']['PICK3']
            }

            arrp4 = {
                'loteria'           :   'PICK 4',
                'fecha'             :   loteria_a_publicar['fecha'],
                "sorteo"            :   loteria_a_publicar['loteria'] +" "+saber_sorteo(loteria_a_publicar['sorteo']),
                'numeros_ganadores' :   loteria_a_publicar['numeros_ganadores']['PICK4']
            }

            publicar_P3 = Publicar_En_Plataformas(user_desarrollo, PLATAFORMA_MEGA,arrp3 ).publicar()
            publicar_P4 = Publicar_En_Plataformas(user_desarrollo, PLATAFORMA_MEGA,arrp4 ).publicar()
            if(publicar_P3 and publicar_P4):
                print(f"SE PREMIO CORRECTAMENTE LA LOTERIA: {self.loteria }CON EL SORTEO: {self.sorteo}")
            else:
                print(f"NOOOOOOOO SE PREMIO LA LOTERIA: {self.loteria }CON EL SORTEO: {self.sorteo}")

        else:
            print(f"NO SE PREMIO ESTA LOTERIA: {self.loteria} COn este sorteo {self.sorteo}")


FLORIDA_MIDDAY          =   Buscar_Numeros_Premiar(VARIABLES.OBJ_FL_AM).buscar
NEW_YORK_MIDDAY         =   Buscar_Numeros_Premiar(VARIABLES.OBJ_NY_AM).buscar
VIRGINIA_MIDDAY         =   Buscar_Numeros_Premiar(VARIABLES.OBJ_VA_AM).buscar
GEORGIA_MIDDAY          =   Buscar_Numeros_Premiar(VARIABLES.OBJ_GA_AM).buscar
NEW_JERSEY_MIDDAY       =   Buscar_Numeros_Premiar(VARIABLES.OBJ_NJ_AM).buscar
SOUTH_CAROLINA_MIDDAY   =   Buscar_Numeros_Premiar(VARIABLES.OBJ_SC_AM).buscar
PENNSYLVANIA_MIDDAY     =   Buscar_Numeros_Premiar(VARIABLES.OBJ_PA_AM).buscar
WASHINGTON_DC_MIDDAY    =   Buscar_Numeros_Premiar(VARIABLES.OBJ_DC_AM).buscar
CONNECTICUT_MIDDAY      =   Buscar_Numeros_Premiar(VARIABLES.OBJ_CT_AM).buscar
NORTh_CAROLINA_MIDDAY   =   Buscar_Numeros_Premiar(VARIABLES.OBJ_NC_AM).buscar


##!AGREGAR ALGO PARA BORRAR PANTALLA O LIMPIAR CACHE AL INIICO DE CADA DIA

hora_prueba =  '15:48:00'

###! HORARIO DE BUSCAR NUMEROS
schedule.every().day.at(hora_prueba).do(run, FLORIDA_MIDDAY)
schedule.every().day.at(hora_prueba).do(run, NEW_YORK_MIDDAY)
schedule.every().day.at(hora_prueba).do(run, VIRGINIA_MIDDAY)
schedule.every().day.at(hora_prueba).do(run, GEORGIA_MIDDAY)
schedule.every().day.at(hora_prueba).do(run, NEW_JERSEY_MIDDAY)
schedule.every().day.at(hora_prueba).do(run, SOUTH_CAROLINA_MIDDAY)
schedule.every().day.at(hora_prueba).do(run, PENNSYLVANIA_MIDDAY)
schedule.every().day.at(hora_prueba).do(run, WASHINGTON_DC_MIDDAY)
schedule.every().day.at(hora_prueba).do(run, CONNECTICUT_MIDDAY)
schedule.every().day.at(hora_prueba).do(run, NORTh_CAROLINA_MIDDAY)
#schedule.every().day.at(hora_prueba).do(run, )


while True:
    fecha_actual = fecha('%d-%m-%Y || %H:%M:%S')
    print(f"|----------> {fecha_actual} <----------|")
    saber = schedule.run_pending()
    if(saber == None):
        pass
    else:
        print(schedule.run_pending())
    time.sleep(1)