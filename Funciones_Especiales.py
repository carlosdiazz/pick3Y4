from datetime import datetime
from Datos_Loterias.FLORIDA_AM import FLORIDA_LOTTERY_USA_AM
from Datos_Loterias.FLORIDA_PM_ import FLORIDA_LOTTERY_USA_PM
from Datos_Loterias.NY_AM import NEW_YORK_TARDE_LOTTERYUSA
from Datos_Loterias.NY_PM import NEW_YORK_PM_LOTTERYUSA
from Datos_Loterias.NJ_AM import NEW_JERSEY_AM_LOTTERYUSA
from Datos_Loterias.NJ_PM import NEW_JERSEY_PM_LOTTERYUSA
from VARIABLES import *

#! Aqui tengo que agregar los diferentes arreglos
def devolver_arreglo(datos):
    if(datos == OBJ_FL_AM):
        return FLORIDA_LOTTERY_USA_AM
    elif(datos == OBJ_FL_PM):
        return FLORIDA_LOTTERY_USA_PM
    elif(datos == OBJ_NY_AM):
        return NEW_YORK_TARDE_LOTTERYUSA
    elif(datos == OBJ_NY_PM):
        return NEW_YORK_PM_LOTTERYUSA
    elif(datos == OBJ_NJ_AM):
        return NEW_JERSEY_AM_LOTTERYUSA
    elif(datos == OBJ_NJ_AM):
            return NEW_JERSEY_PM_LOTTERYUSA
    else:
        return False


def fecha(tipo_fecha):
    return datetime.today().strftime(tipo_fecha)

def Validar_Fecha_Hoy(fecha_comprobar):

    fecha_dia_un_digito = fecha('%d')
    fecha_dia_un_digito=fecha_dia_un_digito.lstrip('0')

    Todas_las_Fechas = [

    fecha(f'%A, %B {fecha_dia_un_digito}, %Y'),
    fecha('%A, %b %d, %Y'),
    fecha(f'%A, %b {fecha_dia_un_digito}, %Y'),
    fecha(f'%A %B {fecha_dia_un_digito}th %Y'),
    fecha(f'%A %B {fecha_dia_un_digito}st %Y'),
    fecha(f'%A %B {fecha_dia_un_digito}nd %Y'),
    fecha(f'%A %B {fecha_dia_un_digito}rd %Y'),
    fecha('%A %B %dth %Y'),
    fecha('%a %m/%d/%y'),
    fecha('%A, %B %d, %Y'),
    fecha('%d-%m-%Y'),
    fecha('%d/%m/%Y'),
    fecha('%Y-%m-%d'),

    ]
    if fecha_comprobar in Todas_las_Fechas:
        return True
    else:
        #! AQUI TENGO QUE DEVOLVER FALSO ES UNA PRUEBA
        return False

def comprobar_pick3(arr):
    if(type(arr)==list):
        if(len(arr)==3):
            return f'{arr[0]}{arr[1]}{arr[2]}'
        return False
    else:
        return False

def comprobar_pick4(arr):
    if(type(arr)==list):
        if(len(arr)==4):
            return f'{arr[0]}{arr[1]}{arr[2]}{arr[3]}'
        return False
    else:
        return False