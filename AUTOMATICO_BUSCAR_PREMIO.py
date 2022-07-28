#ESTE SCRIPT SE DEJARA EJECUTANDO FIJO QUE ES QUIEN SE ENCARGAR DE BUSCAR A LA HORA ESPECIFICAS LOS DIFERENTES NUMEROS GANADORES

import schedule
import VARIABLES
from Funciones_Especiales import fecha, run, clearConsole
import time
from config import TIEMPO_A_BUSCAR
from Objectos_para_Automaticos import *

##! HORARIO DE BUSCAR NUMEROS
schedule.every().day.at('00:00:00').do(run, clearConsole)
#LOTERIAS DOMINICANA ----------------------------------------------------------------------
schedule.every().day.at(VARIABLES.OBJ_PRIMERA_AM['HORA']).do(run,LOTTERY_PRIMERA_AM )
schedule.every().day.at(VARIABLES.OBJ_PRIMERA_PM['HORA']).do(run, LOTTERY_PRIMERA_PM)
schedule.every().day.at(VARIABLES.OBJ_KING_AM['HORA']).do(run, LOTTERY_KING_LOTTERY_AM)
schedule.every().day.at(VARIABLES.OBJ_KING_PM['HORA']).do(run, LOTTERY_KING_LOTTERY_PM)
schedule.every().day.at(VARIABLES.OBJ_LA_SUERTE['HORA']).do(run, LOTTERY_LA_SUERTE)
schedule.every().day.at(VARIABLES.OBJ_REAL['HORA']).do(run,LOTTERY_REAL )
schedule.every().day.at(VARIABLES.OBJ_LOTEDOM['HORA']).do(run,LOTTERY_LOTEDOM )
schedule.every().day.at(VARIABLES.OBJ_GANAMAS['HORA']).do(run,LOTTERY_GANAMAS )
schedule.every().day.at(VARIABLES.OBJ_NACIONAL['HORA']).do(run,LOTTERY_NACIONAL )
schedule.every().day.at(VARIABLES.OBJ_LOTEKA['HORA']).do(run, LOTTERY_LOTEKA)
schedule.every().day.at(VARIABLES.OBJ_LEIDSA['HORA']).do(run,LOTTERY_LEIDSA )
schedule.every().day.at(VARIABLES.OBJ_ANGUILLA_AM['HORA']).do(run,LOTTERY_ANGUILLA_AM )
schedule.every().day.at(VARIABLES.OBJ_ANGUILLA_MD['HORA']).do(run,LOTTERY_ANGUILLA_MD )
schedule.every().day.at(VARIABLES.OBJ_ANGUILLA_TARDE['HORA']).do(run,LOTTERY_ANGUILLA_TARDE )
schedule.every().day.at(VARIABLES.OBJ_ANGUILLA_PM['HORA']).do(run,LOTTERY_ANGUILLA_PM )

#LOTERIAS AMERICANA PICKS AM ----------------------------------------------------------------
schedule.every().day.at(VARIABLES.OBJ_FL_AM['HORA']).do(run, LOTERY_FLORIDA_AM)
schedule.every().day.at(VARIABLES.OBJ_NY_AM['HORA']).do(run, LOTERY_NEW_YORK_AM)
schedule.every().day.at(VARIABLES.OBJ_NJ_AM['HORA']).do(run, LOTERY_NEW_JERSEY_AM)
schedule.every().day.at(VARIABLES.OBJ_CT_AM['HORA']).do(run, LOTERY_CONNECTICUT_AM)
schedule.every().day.at(VARIABLES.OBJ_VA_AM['HORA']).do(run, LOTERY_VIRGINIA_AM)
schedule.every().day.at(VARIABLES.OBJ_DC_AM['HORA']).do(run, LOTERY_WASHINGTON_DC_AM)
schedule.every().day.at(VARIABLES.OBJ_PA_AM['HORA']).do(run, LOTERY_PENNSYLVANIA_AM)
schedule.every().day.at(VARIABLES.OBJ_SC_AM2['HORA']).do(run, LOTERY_SOUTH_CAROLINA_AM)
schedule.every().day.at(VARIABLES.OBJ_GA_AM['HORA']).do(run, LOTERY_GEORGIA_AM)
schedule.every().day.at(VARIABLES.OBJ_NC_AM['HORA']).do(run, LOTERY_NORTH_CAROLINA_AM)
schedule.every().day.at(VARIABLES.OBJ_MD_AM['HORA']).do(run, LOTERY_MARYLAND_AM)

#LOTERIAS AMERICANA PICKS PM --------------------------------------------------------------
schedule.every().day.at(VARIABLES.OBJ_FL_PM['HORA']).do(run, LOTERY_FLORIDA_PM)
schedule.every().day.at(VARIABLES.OBJ_NY_PM['HORA']).do(run, LOTERY_NEW_YORK_PM)
schedule.every().day.at(VARIABLES.OBJ_NJ_PM['HORA']).do(run, LOTERY_NEW_JERSEY_PM)
schedule.every().day.at(VARIABLES.OBJ_CT_PM['HORA']).do(run, LOTERY_CONNECTICUT_PM)
schedule.every().day.at(VARIABLES.OBJ_VA_PM['HORA']).do(run, LOTERY_VIRGINIA_PM)
schedule.every().day.at(VARIABLES.OBJ_DC_PM['HORA']).do(run, LOTERY_WASHINGTON_DC_PM)
schedule.every().day.at(VARIABLES.OBJ_PA_PM['HORA']).do(run, LOTERY_PENNSYLVANIA_PM)
schedule.every().day.at(VARIABLES.OBJ_SC_AM2['HORA']).do(run, LOTERY_SOUTH_CAROLINA_PM)
schedule.every().day.at(VARIABLES.OBJ_GA_PM['HORA']).do(run, LOTERY_GEORGIA_PM)
schedule.every().day.at(VARIABLES.OBJ_NC_PM['HORA']).do(run, LOTERY_NORTH_CAROLINA_PM)
schedule.every().day.at(VARIABLES.OBJ_GA_NIGHT['HORA']).do(run, LOTERY_GEORGIA_NIGHT)
schedule.every().day.at(VARIABLES.OBJ_MD_PM['HORA']).do(run, LOTERY_MARYLAND_PM)

clearConsole()
while True:
    fecha_actual = fecha('%d-%m-%Y || %H:%M:%S')
    print(f"|---------- BUSCAR PREMIO -----> {fecha_actual} <----------|")
    saber = schedule.run_pending()
    if(saber == None):
        pass
    else:
        print(schedule.run_pending())
    time.sleep(TIEMPO_A_BUSCAR)