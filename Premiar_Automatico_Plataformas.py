import schedule
import VARIABLES
from PUBLICAR_NUMEROS import Publicar_En_Plataformas
from Funciones_Especiales import fecha, run, CONSULTAR_NUMEROS_API, saber_sorteo, clearConsole
import time
from config import user_desarrollo
from Datos_Loterias.DATOS_PLATAFORMA import PLATAFORMA_MEGA

class Buscar_Numeros_Premiar():

    def __init__(self, obj):
        self.loteria = obj['LOTERIA']
        self.sorteo = obj['SORTEO']

    def buscar(self):
        #? Con esta funcion buscare los numeros ganadores
        self.fecha = fecha('%d-%m-%Y')
        numeros = CONSULTAR_NUMEROS_API(self.loteria,self.sorteo,self.fecha)
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


FLORIDA_MIDDAY              =   Buscar_Numeros_Premiar(VARIABLES.OBJ_FL_AM).buscar
NEW_YORK_MIDDAY             =   Buscar_Numeros_Premiar(VARIABLES.OBJ_NY_AM).buscar
VIRGINIA_MIDDAY             =   Buscar_Numeros_Premiar(VARIABLES.OBJ_VA_AM).buscar
GEORGIA_MIDDAY              =   Buscar_Numeros_Premiar(VARIABLES.OBJ_GA_AM).buscar
NEW_JERSEY_MIDDAY           =   Buscar_Numeros_Premiar(VARIABLES.OBJ_NJ_AM).buscar
SOUTH_CAROLINA_MIDDAY       =   Buscar_Numeros_Premiar(VARIABLES.OBJ_SC_AM).buscar
PENNSYLVANIA_MIDDAY         =   Buscar_Numeros_Premiar(VARIABLES.OBJ_PA_AM).buscar
WASHINGTON_DC_MIDDAY        =   Buscar_Numeros_Premiar(VARIABLES.OBJ_DC_AM).buscar
CONNECTICUT_MIDDAY          =   Buscar_Numeros_Premiar(VARIABLES.OBJ_CT_AM).buscar
NORTh_CAROLINA_MIDDAY       =   Buscar_Numeros_Premiar(VARIABLES.OBJ_NC_AM).buscar
SOUTH_CAROLINA_EVENING      =   Buscar_Numeros_Premiar(VARIABLES.OBJ_SC_PM).buscar
GEORGIA_EVENING             =   Buscar_Numeros_Premiar(VARIABLES.OBJ_GA_PM).buscar
PENNSYLVANIA_EVENING        =   Buscar_Numeros_Premiar(VARIABLES.OBJ_PA_PM).buscar
WASHINGTON_DC_EVENING       =   Buscar_Numeros_Premiar(VARIABLES.OBJ_DC_PM).buscar
FLORIDA_EVENING             =   Buscar_Numeros_Premiar(VARIABLES.OBJ_FL_PM).buscar
CONNECTICUT_EVENING         =   Buscar_Numeros_Premiar(VARIABLES.OBJ_CT_PM).buscar
NEW_YORK_EVENING            =   Buscar_Numeros_Premiar(VARIABLES.OBJ_NY_PM).buscar
VIRGINIA_EVENING            =   Buscar_Numeros_Premiar(VARIABLES.OBJ_VA_PM).buscar
NEW_JERSEY_EVENING          =   Buscar_Numeros_Premiar(VARIABLES.OBJ_NJ_PM).buscar
GEORGIA_NIGHT               =   Buscar_Numeros_Premiar(VARIABLES.OBJ_GA_NIGHT).buscar
NORTh_CAROLINA_EVENING      =   Buscar_Numeros_Premiar(VARIABLES.OBJ_NC_PM).buscar
##!AGREGAR ALGO PARA BORRAR PANTALLA O LIMPIAR CACHE AL INIICO DE CADA DIA

hora_prueba =  '23:52:00'

###! HORARIO DE BUSCAR NUMEROS
schedule.every().day.at('00:00:00').do(run, clearConsole)

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
schedule.every().day.at(hora_prueba).do(run, SOUTH_CAROLINA_EVENING)
schedule.every().day.at(hora_prueba).do(run, GEORGIA_EVENING)
#? TARDE --------------------------------------------------------------
schedule.every().day.at(hora_prueba).do(run, PENNSYLVANIA_EVENING)
schedule.every().day.at(hora_prueba).do(run, WASHINGTON_DC_EVENING)
schedule.every().day.at(hora_prueba).do(run, FLORIDA_EVENING)
schedule.every().day.at(hora_prueba).do(run, NEW_YORK_EVENING)
schedule.every().day.at(hora_prueba).do(run, CONNECTICUT_EVENING)
schedule.every().day.at(hora_prueba).do(run, VIRGINIA_EVENING)
schedule.every().day.at(hora_prueba).do(run, NEW_JERSEY_EVENING)
schedule.every().day.at(hora_prueba).do(run, NORTh_CAROLINA_EVENING)
schedule.every().day.at(hora_prueba).do(run, GEORGIA_NIGHT)
while True:
    fecha_actual = fecha('%d-%m-%Y || %H:%M:%S')
    print(f"|----------> {fecha_actual} <----------|")
    saber = schedule.run_pending()
    if(saber == None):
        pass
    else:
        print(schedule.run_pending())
    time.sleep(360)