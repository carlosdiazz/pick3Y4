
#? ESTE ARCHIVO ES SOLO PARA PROBAR CODIGO
import schedule
from Funciones_Especiales import fecha, run, clearConsole
import time
from config import TIEMPO_A_BUSCAR, hora_prueba
from Objectos_para_Automaticos import *

##? BUSCAR NUMEROS------------------------------------------------------------------------
###LOTERIAS DOMINICANA ------------------------------------------------------
#schedule.every().day.at(hora_prueba).do(run,LOTTERY_PRIMERA_AM )
#schedule.every().day.at(hora_prueba).do(run, LOTTERY_PRIMERA_PM)
#schedule.every().day.at(hora_prueba).do(run, LOTTERY_KING_LOTTERY_AM)
#schedule.every().day.at(hora_prueba).do(run, LOTTERY_KING_LOTTERY_PM)
#schedule.every().day.at(hora_prueba).do(run, LOTTERY_LA_SUERTE)
#schedule.every().day.at(hora_prueba).do(run,LOTTERY_REAL )
#schedule.every().day.at(hora_prueba).do(run,LOTTERY_LOTEDOM )
#schedule.every().day.at(hora_prueba).do(run,LOTTERY_GANAMAS )
#schedule.every().day.at(hora_prueba).do(run,LOTTERY_NACIONAL )
#schedule.every().day.at(hora_prueba).do(run, LOTTERY_LOTEKA)
#schedule.every().day.at(hora_prueba).do(run,LOTTERY_LEIDSA )
#schedule.every().day.at(hora_prueba).do(run,LOTTERY_ANGUILLA_AM )
#schedule.every().day.at(hora_prueba).do(run,LOTTERY_ANGUILLA_MD )
#schedule.every().day.at(hora_prueba).do(run,LOTTERY_ANGUILLA_TARDE )
#schedule.every().day.at(hora_prueba).do(run,LOTTERY_ANGUILLA_PM )
###LOTERIAS AM ----------------------------------------------------------------
#schedule.every().day.at(hora_prueba).do(run, LOTERY_FLORIDA_AM)
#schedule.every().day.at(hora_prueba).do(run, LOTERY_NEW_YORK_AM)
#schedule.every().day.at(hora_prueba).do(run, LOTERY_NEW_JERSEY_AM)
#schedule.every().day.at(hora_prueba).do(run, LOTERY_CONNECTICUT_AM)
#schedule.every().day.at(hora_prueba).do(run, LOTERY_VIRGINIA_AM)
#schedule.every().day.at(hora_prueba).do(run, LOTERY_WASHINGTON_DC_AM)
#schedule.every().day.at(hora_prueba).do(run, LOTERY_PENNSYLVANIA_AM)
#schedule.every().day.at(hora_prueba).do(run, LOTERY_SOUTH_CAROLINA_AM)
#schedule.every().day.at(hora_prueba).do(run, LOTERY_GEORGIA_AM)
#schedule.every().day.at(hora_prueba).do(run, LOTERY_NORTH_CAROLINA_AM)
#schedule.every().day.at(hora_prueba).do(run, LOTERY_MARYLAND_AM)
#LOTERIAS PM --------------------------------------------------------------
#schedule.every().day.at(hora_prueba).do(run, LOTERY_FLORIDA_PM)
#schedule.every().day.at(hora_prueba).do(run, LOTERY_NEW_YORK_PM)
#schedule.every().day.at(hora_prueba).do(run, LOTERY_NEW_JERSEY_PM)
#schedule.every().day.at(hora_prueba).do(run, LOTERY_CONNECTICUT_PM)
#schedule.every().day.at(hora_prueba).do(run, LOTERY_VIRGINIA_PM)
#schedule.every().day.at(hora_prueba).do(run, LOTERY_WASHINGTON_DC_PM)
#schedule.every().day.at(hora_prueba).do(run, LOTERY_PENNSYLVANIA_PM)
#schedule.every().day.at(hora_prueba).do(run, LOTERY_SOUTH_CAROLINA_PM)
#schedule.every().day.at(hora_prueba).do(run, LOTERY_GEORGIA_PM)
#schedule.every().day.at(hora_prueba).do(run, LOTERY_NORTH_CAROLINA_PM)
#schedule.every().day.at(hora_prueba).do(run, LOTERY_GEORGIA_NIGHT)
#schedule.every().day.at(hora_prueba).do(run, LOTERY_MARYLAND_PM)
##? PREMIAR PLATAFORMA ----------------------------------------------------------
#schedule.every().day.at(hora_prueba).do(run, MARYLAND_MIDDAY)
#schedule.every().day.at(hora_prueba).do(run, MARYLAND_EVENING)
##LOTERIAS AM PICKS ----------------------------------------------------------------
schedule.every().day.at(hora_prueba).do(run, FLORIDA_MIDDAY)
#schedule.every().day.at(hora_prueba).do(run, NEW_YORK_MIDDAY)
#schedule.every().day.at(hora_prueba).do(run, VIRGINIA_MIDDAY)
#schedule.every().day.at(hora_prueba).do(run, GEORGIA_MIDDAY)
#schedule.every().day.at(hora_prueba).do(run, NEW_JERSEY_MIDDAY)
#schedule.every().day.at(hora_prueba).do(run, SOUTH_CAROLINA_MIDDAY)
#schedule.every().day.at(hora_prueba).do(run, PENNSYLVANIA_MIDDAY)
#schedule.every().day.at(hora_prueba).do(run, WASHINGTON_DC_MIDDAY)
#schedule.every().day.at(hora_prueba).do(run, CONNECTICUT_MIDDAY)
#schedule.every().day.at(hora_prueba).do(run, NORTH_CAROLINA_MIDDAY)

##LOTERIAS PM PICKS --------------------------------------------------------------
#schedule.every().day.at(hora_prueba).do(run, SOUTH_CAROLINA_EVENING)
#schedule.every().day.at(hora_prueba).do(run, GEORGIA_EVENING)
#schedule.every().day.at(hora_prueba).do(run, PENNSYLVANIA_EVENING)
#schedule.every().day.at(hora_prueba).do(run, WASHINGTON_DC_EVENING)
#schedule.every().day.at(hora_prueba).do(run, FLORIDA_EVENING)
#schedule.every().day.at(hora_prueba).do(run, NEW_YORK_EVENING)
#schedule.every().day.at(hora_prueba).do(run, CONNECTICUT_EVENING)
#schedule.every().day.at(hora_prueba).do(run, VIRGINIA_EVENING)
#schedule.every().day.at(hora_prueba).do(run, NEW_JERSEY_EVENING)
#schedule.every().day.at(hora_prueba).do(run, NORTH_CAROLINA_EVENING)
#schedule.every().day.at(hora_prueba).do(run, GEORGIA_NIGHT)

## OTRAS LOTERIA PARA PREMIAR ---------------------------------------------------------
#schedule.every().day.at(hora_prueba).do(run, PRIMERA_PM_PLATATAFORMA_MEGA)
#schedule.every().day.at(hora_prueba).do(run, PRIMERA_PM_PLATATAFORMA_RAPI)

#schedule.every().day.at(hora_prueba).do(run, NEW_YORK_AM_PLATAFORMA_DEV)
#schedule.every().day.at(hora_prueba).do(run, FLORIDA_AM_PLATAFORMA_DEV)

while True:
    fecha_actual = fecha('%d-%m-%Y || %H:%M:%S')
    print(f"|---------- PRUEBAS --> {fecha_actual} <----------|")
    saber = schedule.run_pending()
    if(saber == None):
        pass
    else:
        print(schedule.run_pending())
    time.sleep(TIEMPO_A_BUSCAR)