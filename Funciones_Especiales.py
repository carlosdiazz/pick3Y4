import threading
from datetime import datetime
from VARIABLES import *

from Datos_Loterias.FLORIDA import FLORIDA_LOTTERYUSA
from Datos_Loterias.NEW_YORK import NEW_YORK_LOTTERYUSA
from Datos_Loterias.NEW_JERSEY import NEW_JERSEY_LOTTERYUSA
from Datos_Loterias.CONNECTICUT import CONNECTICUT_LOTTERYUSA
from Datos_Loterias.VIRGINIA import VIRGINIA_LOTTERYUSA
from Datos_Loterias.WASHINGTON_DC import WASHINGTON_DC_LOTTERYUSA
from Datos_Loterias.PENNSYLVANIA import PENNSYLVANIA_LOTTERYUSA
from Datos_Loterias.SOUTH_CAROLINA import SOUTH_CAROLINA_LOTTERYUSA


#! Aqui tengo que agregar los diferentes arreglos
def devolver_arreglo(datos):
    if(datos == OBJ_FL_AM or datos == OBJ_FL_PM):
        return FLORIDA_LOTTERYUSA

    elif(datos == OBJ_NY_AM or datos == OBJ_NY_PM):
        return NEW_YORK_LOTTERYUSA

    elif(datos == OBJ_NJ_AM or datos == OBJ_NJ_PM):
        return NEW_JERSEY_LOTTERYUSA

    elif(datos == OBJ_CT_AM or datos == OBJ_CT_PM):
        return CONNECTICUT_LOTTERYUSA

    elif(datos == OBJ_VA_AM or datos == OBJ_VA_PM):
        return VIRGINIA_LOTTERYUSA

    elif(datos == OBJ_DC_AM or datos == OBJ_DC_PM):
        return WASHINGTON_DC_LOTTERYUSA

    elif(datos == OBJ_PA_AM or datos == OBJ_PA_PM):
        return PENNSYLVANIA_LOTTERYUSA

    elif(datos == OBJ_SC_AM or datos == OBJ_SC_PM):
        return SOUTH_CAROLINA_LOTTERYUSA

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

def run(job_func):
    job_thread = threading.Thread(target=job_func)
    job_thread.start()