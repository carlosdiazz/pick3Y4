
#? ESTE ARCHIVO ES SOLO PARA PROBAR CODIGO
import schedule
from Funciones_Especiales import fecha, run
import time
from config import TIEMPO_A_BUSCAR, hora_prueba
from Objectos_para_Automaticos import *

#! AGREGAR TODO EN PROBAR
#LOTERIAS QUE SON SUPER PALES ------------------------------------------------------------------
#LOTERIAS QUE SON SUPER PALES ------------------------------------------------------------------
#schedule.every().day.at(hora_prueba).do(run, LOTTERY_SP_PRIMERA_GANAMAS)
#schedule.every().day.at(hora_prueba).do(run,LOTTERY_SP_REAL_PRIMERA )
#schedule.every().day.at(hora_prueba).do(run,LOTTERY_SP_NYAM_REAL )
#schedule.every().day.at(hora_prueba).do(run,LOTTERY_SP_REAL_GANAMAS)
#schedule.every().day.at(hora_prueba).do(run,LOTTERY_SP_NYAM_FLAM )
#schedule.every().day.at(hora_prueba).do(run, LOTTERY_SP_NYAM_LOTEKA)
#schedule.every().day.at(hora_prueba).do(run,LOTTERY_SP_NYAM_GANAMAS )
#schedule.every().day.at(hora_prueba).do(run,LOTTERY_SP_GANAMAS_LOTEKA )
#schedule.every().day.at(hora_prueba).do(run, LOTTERY_SP_NACIONAL_LEIDSA) #! ESTE SUPER PALE NO SE PUBLICO AYER
#schedule.every().day.at(hora_prueba).do(run, LOTTERY_SP_LOTEKA_NACIONAL)
#schedule.every().day.at(hora_prueba).do(run,LOTTERY_SP_NYPM_NACIONAL)
#schedule.every().day.at(hora_prueba).do(run, LOTTERY_SP_NYPM_FLPM)

#PREMIOS SUPER PALES SANCHEZ ---------------------------------------------------------------------------------------
schedule.every().day.at(hora_prueba).do(run, SANCHEZ_SP_REAL_PRIMERA)
schedule.every().day.at(hora_prueba).do(run, SANCHEZ_SP_PRIMERA_GANAMAS)
schedule.every().day.at(hora_prueba).do(run, SANCHEZ_SP_NYAM_REAL)
schedule.every().day.at(hora_prueba).do(run,SANCHEZ_SP_REAl_GANAMAS )
schedule.every().day.at(hora_prueba).do(run, SANCHEZ_SP_NYAM_FLAM)
schedule.every().day.at(hora_prueba).do(run,SANCHEZ_SP_NYAM_GANAMAS )

while True:
    fecha_actual = fecha('%d-%m-%Y || %H:%M:%S')
    print(f"|---------- PRUEBAS --> {fecha_actual} <----------|")
    saber = schedule.run_pending()
    if(saber == None):
        pass
    else:
        print(schedule.run_pending())
    time.sleep(TIEMPO_A_BUSCAR)