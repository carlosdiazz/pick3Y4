
#? ESTE ARCHIVO ES SOLO PARA PROBAR CODIGO
import schedule
from Funciones_Especiales import fecha, run
import time
from config import TIEMPO_A_BUSCAR, hora_prueba
from Objectos_para_Automaticos import *

#! AGREGAR TODO EN PROBAR
#LOTERIAS QUE SON SUPER PALES ------------------------------------------------------------------
schedule.every().day.at(hora_prueba).do(run, LOTTERY_SP_PRIMERA_GANAMAS)


while True:
    fecha_actual = fecha('%d-%m-%Y || %H:%M:%S')
    print(f"|---------- PRUEBAS --> {fecha_actual} <----------|")
    saber = schedule.run_pending()
    if(saber == None):
        pass
    else:
        print(schedule.run_pending())
    time.sleep(TIEMPO_A_BUSCAR)