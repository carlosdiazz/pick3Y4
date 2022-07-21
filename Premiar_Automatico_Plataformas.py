import schedule
import VARIABLES
import time
from Funciones_Especiales import run, clearConsole, fecha
from PUBLICAR_NUMEROS import Buscar_Numeros_Premiar

#LOTERIAS AM
FLORIDA_MIDDAY              =   Buscar_Numeros_Premiar(VARIABLES.OBJ_FL_AM).buscar
NEW_YORK_MIDDAY             =   Buscar_Numeros_Premiar(VARIABLES.OBJ_NY_AM).buscar
VIRGINIA_MIDDAY             =   Buscar_Numeros_Premiar(VARIABLES.OBJ_VA_AM).buscar
GEORGIA_MIDDAY              =   Buscar_Numeros_Premiar(VARIABLES.OBJ_GA_AM).buscar
NEW_JERSEY_MIDDAY           =   Buscar_Numeros_Premiar(VARIABLES.OBJ_NJ_AM).buscar
SOUTH_CAROLINA_MIDDAY       =   Buscar_Numeros_Premiar(VARIABLES.OBJ_SC_AM).buscar
PENNSYLVANIA_MIDDAY         =   Buscar_Numeros_Premiar(VARIABLES.OBJ_PA_AM).buscar
WASHINGTON_DC_MIDDAY        =   Buscar_Numeros_Premiar(VARIABLES.OBJ_DC_AM).buscar
CONNECTICUT_MIDDAY          =   Buscar_Numeros_Premiar(VARIABLES.OBJ_CT_AM).buscar
NORTH_CAROLINA_MIDDAY       =   Buscar_Numeros_Premiar(VARIABLES.OBJ_NC_AM).buscar
#LOTERIAS PM
SOUTH_CAROLINA_EVENING      =   Buscar_Numeros_Premiar(VARIABLES.OBJ_SC_PM).buscar
GEORGIA_EVENING             =   Buscar_Numeros_Premiar(VARIABLES.OBJ_GA_PM).buscar
PENNSYLVANIA_EVENING        =   Buscar_Numeros_Premiar(VARIABLES.OBJ_PA_PM).buscar
WASHINGTON_DC_EVENING       =   Buscar_Numeros_Premiar(VARIABLES.OBJ_DC_PM).buscar
FLORIDA_EVENING             =   Buscar_Numeros_Premiar(VARIABLES.OBJ_FL_PM).buscar
CONNECTICUT_EVENING         =   Buscar_Numeros_Premiar(VARIABLES.OBJ_CT_PM).buscar
NEW_YORK_EVENING            =   Buscar_Numeros_Premiar(VARIABLES.OBJ_NY_PM).buscar
VIRGINIA_EVENING            =   Buscar_Numeros_Premiar(VARIABLES.OBJ_VA_PM).buscar
NEW_JERSEY_EVENING          =   Buscar_Numeros_Premiar(VARIABLES.OBJ_NJ_PM).buscar
NORTH_CAROLINA_EVENING      =   Buscar_Numeros_Premiar(VARIABLES.OBJ_NC_PM).buscar
GEORGIA_NIGHT               =   Buscar_Numeros_Premiar(VARIABLES.OBJ_GA_NIGHT).buscar

hora_prueba =  '20:10:00'

###! HORARIO DE BUSCAR NUMEROS
schedule.every().day.at('00:00:00').do(run, clearConsole)

#LOTERIAS AM ----------------------------------------------------------------
schedule.every().day.at(VARIABLES.OBJ_FL_AM['HORA']).do(run, FLORIDA_MIDDAY)
schedule.every().day.at(VARIABLES.OBJ_NY_AM['HORA']).do(run, NEW_YORK_MIDDAY)
schedule.every().day.at(VARIABLES.OBJ_VA_AM['HORA']).do(run, VIRGINIA_MIDDAY)
schedule.every().day.at(VARIABLES.OBJ_GA_AM['HORA']).do(run, GEORGIA_MIDDAY)
schedule.every().day.at(VARIABLES.OBJ_NJ_AM['HORA']).do(run, NEW_JERSEY_MIDDAY)
schedule.every().day.at(VARIABLES.OBJ_SC_AM['HORA']).do(run, SOUTH_CAROLINA_MIDDAY)
schedule.every().day.at(VARIABLES.OBJ_PA_AM['HORA']).do(run, PENNSYLVANIA_MIDDAY)
schedule.every().day.at(VARIABLES.OBJ_DC_AM['HORA']).do(run, WASHINGTON_DC_MIDDAY)
schedule.every().day.at(VARIABLES.OBJ_CT_AM['HORA']).do(run, CONNECTICUT_MIDDAY)
schedule.every().day.at(VARIABLES.OBJ_NC_AM['HORA']).do(run, NORTH_CAROLINA_MIDDAY)

#LOTERIAS PM --------------------------------------------------------------
schedule.every().day.at(VARIABLES.OBJ_SC_PM['HORA']).do(run, SOUTH_CAROLINA_EVENING)
schedule.every().day.at(VARIABLES.OBJ_GA_PM['HORA']).do(run, GEORGIA_EVENING)
schedule.every().day.at(VARIABLES.OBJ_PA_PM['HORA']).do(run, PENNSYLVANIA_EVENING)
schedule.every().day.at(VARIABLES.OBJ_DC_PM['HORA']).do(run, WASHINGTON_DC_EVENING)
schedule.every().day.at(VARIABLES.OBJ_FL_PM['HORA']).do(run, FLORIDA_EVENING)
schedule.every().day.at(VARIABLES.OBJ_NY_PM['HORA']).do(run, NEW_YORK_EVENING)
schedule.every().day.at(VARIABLES.OBJ_CT_PM['HORA']).do(run, CONNECTICUT_EVENING)
schedule.every().day.at(VARIABLES.OBJ_VA_PM['HORA']).do(run, VIRGINIA_EVENING)
schedule.every().day.at(VARIABLES.OBJ_NJ_PM['HORA']).do(run, NEW_JERSEY_EVENING)
schedule.every().day.at(VARIABLES.OBJ_NC_PM['HORA']).do(run, NORTH_CAROLINA_EVENING)
schedule.every().day.at(VARIABLES.OBJ_GA_NIGHT['HORA']).do(run, GEORGIA_NIGHT)

###! BORRAR ESTO
##  schedule.every().day.at(hora_prueba).do(run, FLORIDA_MIDDAY)
##  schedule.every().day.at(hora_prueba).do(run, NEW_YORK_MIDDAY)
##  schedule.every().day.at(hora_prueba).do(run, VIRGINIA_MIDDAY)
##  schedule.every().day.at(hora_prueba).do(run, GEORGIA_MIDDAY)
##  schedule.every().day.at(hora_prueba).do(run, NEW_JERSEY_MIDDAY)
##  schedule.every().day.at(hora_prueba).do(run, SOUTH_CAROLINA_MIDDAY)
##  schedule.every().day.at(hora_prueba).do(run, PENNSYLVANIA_MIDDAY)
##  schedule.every().day.at(hora_prueba).do(run, WASHINGTON_DC_MIDDAY)
##  schedule.every().day.at(hora_prueba).do(run, CONNECTICUT_MIDDAY)
##  schedule.every().day.at(hora_prueba).do(run, NORTh_CAROLINA_MIDDAY)
##  schedule.every().day.at(hora_prueba).do(run, SOUTH_CAROLINA_EVENING)
##  schedule.every().day.at(hora_prueba).do(run, GEORGIA_EVENING)
##  schedule.every().day.at(hora_prueba).do(run, PENNSYLVANIA_EVENING)
##  schedule.every().day.at(hora_prueba).do(run, WASHINGTON_DC_EVENING)
##  schedule.every().day.at(hora_prueba).do(run, FLORIDA_EVENING)
##  schedule.every().day.at(hora_prueba).do(run, NEW_YORK_EVENING)
##  schedule.every().day.at(hora_prueba).do(run, CONNECTICUT_EVENING)
##  schedule.every().day.at(hora_prueba).do(run, VIRGINIA_EVENING)
##  schedule.every().day.at(hora_prueba).do(run, NEW_JERSEY_EVENING)
##  schedule.every().day.at(hora_prueba).do(run, NORTH_CAROLIN##A_EVENING)
##  schedule.every().day.at(hora_prueba).do(run, GEORGIA_NIGHT)


while True:
    fecha_actual = fecha('%d-%m-%Y || %H:%M:%S')
    print(f"|----------> {fecha_actual} <----------|")
    saber = schedule.run_pending()
    if(saber == None):
        pass
    else:
        print(schedule.run_pending())
    time.sleep(1)