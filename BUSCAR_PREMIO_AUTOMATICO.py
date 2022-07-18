import schedule
import VARIABLES
from Buscar_premios import Buscar_Premio
from Funciones_Especiales import fecha, run
import time


LOTERY_FLORIDA_AM       =   (Buscar_Premio(VARIABLES.OBJ_FL_AM).Buscar_numeros_ganadores)
LOTERY_FLORIDA_PM       =   (Buscar_Premio(VARIABLES.OBJ_FL_PM).Buscar_numeros_ganadores)

LOTERY_NEW_YORK_AM      =   (Buscar_Premio(VARIABLES.OBJ_NY_AM).Buscar_numeros_ganadores)
LOTERY_NEW_YORK_PM      =   (Buscar_Premio(VARIABLES.OBJ_NY_PM).Buscar_numeros_ganadores)

LOTERY_NEW_JERSEY_AM    =   (Buscar_Premio(VARIABLES.OBJ_NJ_AM).Buscar_numeros_ganadores)
LOTERY_NEW_JERSEY_PM    =   (Buscar_Premio(VARIABLES.OBJ_NJ_PM).Buscar_numeros_ganadores)

LOTERY_CONNECTICUT_AM    =   (Buscar_Premio(VARIABLES.OBJ_CT_AM).Buscar_numeros_ganadores)
LOTERY_CONNECTICUT_PM    =   (Buscar_Premio(VARIABLES.OBJ_CT_PM).Buscar_numeros_ganadores)

LOTERY_VIRGINIA_AM    =   (Buscar_Premio(VARIABLES.OBJ_VA_AM).Buscar_numeros_ganadores)
LOTERY_VIRGINIA_PM    =   (Buscar_Premio(VARIABLES.OBJ_VA_PM).Buscar_numeros_ganadores)

LOTERY_WASHINGTON_DC_AM    =   (Buscar_Premio(VARIABLES.OBJ_DC_AM).Buscar_numeros_ganadores)
LOTERY_WASHINGTON_DC_PM    =   (Buscar_Premio(VARIABLES.OBJ_DC_PM).Buscar_numeros_ganadores)

LOTERY_PENNSYLVANIA_AM    =   (Buscar_Premio(VARIABLES.OBJ_PA_AM).Buscar_numeros_ganadores)
LOTERY_PENNSYLVANIA_PM    =   (Buscar_Premio(VARIABLES.OBJ_PA_PM).Buscar_numeros_ganadores)

#!AGREGAR ALGO PARA BORRAR PANTALLA O LIMPIAR CACHE AL INIICO DE CADA DIA

#! HORARIO DE BUSCAR NUMEROS
#schedule.every().day.at("15:48:00").do(run, LOTERY_FLORIDA_AM)
#schedule.every().day.at("15:48:00").do(run, LOTERY_FLORIDA_PM)
#schedule.every().day.at("15:48:00").do(run, LOTERY_NEW_YORK_AM)
#schedule.every().day.at("15:48:00").do(run, LOTERY_NEW_YORK_PM)
#schedule.every().day.at("15:48:00").do(run, LOTERY_NEW_JERSEY_AM)
#schedule.every().day.at("15:48:00").do(run, LOTERY_NEW_JERSEY_PM)
#schedule.every().day.at("15:48:00").do(run, LOTERY_CONNECTICUT_AM)
#schedule.every().day.at("15:48:00").do(run, LOTERY_CONNECTICUT_PM)
#schedule.every().day.at("15:48:00").do(run, LOTERY_VIRGINIA_AM)
#schedule.every().day.at("15:48:00").do(run, LOTERY_VIRGINIA_PM)
#schedule.every().day.at("16:01:30").do(run, LOTERY_WASHINGTON_DC_AM)
#schedule.every().day.at("16:01:30").do(run, LOTERY_WASHINGTON_DC_PM)

schedule.every().day.at("16:13:25").do(run, LOTERY_PENNSYLVANIA_AM)
schedule.every().day.at("16:13:25").do(run, LOTERY_PENNSYLVANIA_PM)

while True:
    fecha_actual = fecha('%d-%m-%Y || %H:%M:%S')
    print(f"|----------> {fecha_actual} <----------|")
    saber = schedule.run_pending()
    if(saber == None):
        pass
    else:
        print(schedule.run_pending())
    time.sleep(1)