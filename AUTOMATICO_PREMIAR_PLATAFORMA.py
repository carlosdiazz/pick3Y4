# ESTE SCRIPT SE DEJARA EJUCTANDO SIEMPRE QUE ES QUIEN PREMIA EN LA DIFERENTES PLATAFORMAS
import schedule
import VARIABLES
import time
from Funciones_Especiales import run, clearConsole, fecha
from config import TIEMPO_A_BUSCAR
from Objectos_para_Automaticos import *

###! HORARIO DE PREMIAR LOTERIAS
schedule.every().day.at('00:00:00').do(run, clearConsole)

#LOTERIAS AM PICKS ----------------------------------------------------------------
schedule.every().day.at(VARIABLES.OBJ_FL_AM['HORA']).do(run, FLORIDA_MIDDAY)
schedule.every().day.at(VARIABLES.OBJ_NY_AM['HORA']).do(run, NEW_YORK_MIDDAY)
schedule.every().day.at(VARIABLES.OBJ_VA_AM['HORA']).do(run, VIRGINIA_MIDDAY)
schedule.every().day.at(VARIABLES.OBJ_GA_AM['HORA']).do(run, GEORGIA_MIDDAY)
schedule.every().day.at(VARIABLES.OBJ_NJ_AM['HORA']).do(run, NEW_JERSEY_MIDDAY)
schedule.every().day.at(VARIABLES.OBJ_SC_AM2['HORA']).do(run, SOUTH_CAROLINA_MIDDAY)
schedule.every().day.at(VARIABLES.OBJ_PA_AM['HORA']).do(run, PENNSYLVANIA_MIDDAY)
schedule.every().day.at(VARIABLES.OBJ_DC_AM['HORA']).do(run, WASHINGTON_DC_MIDDAY)
schedule.every().day.at(VARIABLES.OBJ_CT_AM['HORA']).do(run, CONNECTICUT_MIDDAY)
schedule.every().day.at(VARIABLES.OBJ_NC_AM['HORA']).do(run, NORTH_CAROLINA_MIDDAY)
schedule.every().day.at(VARIABLES.OBJ_MD_AM['HORA']).do(run, MARYLAND_MIDDAY)

#LOTERIAS PM PICKS --------------------------------------------------------------
schedule.every().day.at(VARIABLES.OBJ_SC_PM2['HORA']).do(run, SOUTH_CAROLINA_EVENING)
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
schedule.every().day.at(VARIABLES.OBJ_MD_PM['HORA']).do(run, MARYLAND_EVENING)

# OTRAS LOTERIA PARA PREMIAR ---------------------------------------------------------
schedule.every().day.at(VARIABLES.OBJ_PRIMERA_PM['HORA']).do(run, PRIMERA_PM_PLATATAFORMA_MEGA)
schedule.every().day.at(VARIABLES.OBJ_PRIMERA_PM['HORA']).do(run, PRIMERA_PM_PLATATAFORMA_RAPI)

clearConsole()
while True:
    fecha_actual = fecha('%d-%m-%Y || %H:%M:%S')
    print(f"|---------- PREMIAR PLATAFORMA -----> {fecha_actual} <----------|")
    saber = schedule.run_pending()
    if(saber == None):
        pass
    else:
        print(schedule.run_pending())
    time.sleep(TIEMPO_A_BUSCAR)