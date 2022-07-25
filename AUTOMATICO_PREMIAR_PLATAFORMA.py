# ESTE SCRIPT SE DEJARA EJUCTANDO SIEMPRE QUE ES QUIEN PREMIA EN LA DIFERENTES PLATAFORMAS
from Datos_Loterias.DATOS_PLATAFORMA import PLATAFORMA_MEGA, USER_MEGALOTTERY, PLATAFORMA_RAPI, USER_RAPIDITA
import schedule
import VARIABLES
import time
from Funciones_Especiales import run, clearConsole, fecha
from PREMIAR import PREMIAR
from config import TIEMPO_A_BUSCAR

#LOTERIAS AM
FLORIDA_MIDDAY                      =   PREMIAR(VARIABLES.OBJ_FL_AM, PLATAFORMA_MEGA, USER_MEGALOTTERY).premiar
NEW_YORK_MIDDAY                     =   PREMIAR(VARIABLES.OBJ_NY_AM, PLATAFORMA_MEGA, USER_MEGALOTTERY).premiar
VIRGINIA_MIDDAY                     =   PREMIAR(VARIABLES.OBJ_VA_AM, PLATAFORMA_MEGA, USER_MEGALOTTERY).premiar
GEORGIA_MIDDAY                      =   PREMIAR(VARIABLES.OBJ_GA_AM, PLATAFORMA_MEGA, USER_MEGALOTTERY).premiar
NEW_JERSEY_MIDDAY                   =   PREMIAR(VARIABLES.OBJ_NJ_AM, PLATAFORMA_MEGA, USER_MEGALOTTERY).premiar
SOUTH_CAROLINA_MIDDAY               =   PREMIAR(VARIABLES.OBJ_SC_AM, PLATAFORMA_MEGA, USER_MEGALOTTERY).premiar
PENNSYLVANIA_MIDDAY                 =   PREMIAR(VARIABLES.OBJ_PA_AM, PLATAFORMA_MEGA, USER_MEGALOTTERY).premiar
WASHINGTON_DC_MIDDAY                =   PREMIAR(VARIABLES.OBJ_DC_AM, PLATAFORMA_MEGA, USER_MEGALOTTERY).premiar
CONNECTICUT_MIDDAY                  =   PREMIAR(VARIABLES.OBJ_CT_AM, PLATAFORMA_MEGA, USER_MEGALOTTERY).premiar
NORTH_CAROLINA_MIDDAY               =   PREMIAR(VARIABLES.OBJ_NC_AM, PLATAFORMA_MEGA, USER_MEGALOTTERY).premiar
#LOTERIAS PM
SOUTH_CAROLINA_EVENING              =   PREMIAR(VARIABLES.OBJ_SC_PM, PLATAFORMA_MEGA, USER_MEGALOTTERY).premiar
GEORGIA_EVENING                     =   PREMIAR(VARIABLES.OBJ_GA_PM, PLATAFORMA_MEGA, USER_MEGALOTTERY).premiar
PENNSYLVANIA_EVENING                =   PREMIAR(VARIABLES.OBJ_PA_PM, PLATAFORMA_MEGA, USER_MEGALOTTERY).premiar
WASHINGTON_DC_EVENING               =   PREMIAR(VARIABLES.OBJ_DC_PM, PLATAFORMA_MEGA, USER_MEGALOTTERY).premiar
FLORIDA_EVENING                     =   PREMIAR(VARIABLES.OBJ_FL_PM, PLATAFORMA_MEGA, USER_MEGALOTTERY).premiar
CONNECTICUT_EVENING                 =   PREMIAR(VARIABLES.OBJ_CT_PM, PLATAFORMA_MEGA, USER_MEGALOTTERY).premiar
NEW_YORK_EVENING                    =   PREMIAR(VARIABLES.OBJ_NY_PM, PLATAFORMA_MEGA, USER_MEGALOTTERY).premiar
VIRGINIA_EVENING                    =   PREMIAR(VARIABLES.OBJ_VA_PM, PLATAFORMA_MEGA, USER_MEGALOTTERY).premiar
NEW_JERSEY_EVENING                  =   PREMIAR(VARIABLES.OBJ_NJ_PM, PLATAFORMA_MEGA, USER_MEGALOTTERY).premiar
NORTH_CAROLINA_EVENING              =   PREMIAR(VARIABLES.OBJ_NC_PM, PLATAFORMA_MEGA, USER_MEGALOTTERY).premiar
GEORGIA_NIGHT                       =   PREMIAR(VARIABLES.OBJ_GA_NIGHT, PLATAFORMA_MEGA, USER_MEGALOTTERY).premiar

#LOTERIAS TRADICIONALES MEGALOTTERY -------------------------------------------------------------------
PRIMERA_PM_PLATATAFORMA_MEGA        = PREMIAR(VARIABLES.OBJ_PRIMERA_PM, PLATAFORMA_MEGA, USER_MEGALOTTERY).premiar

#LOTERIAS TRADICIONALES RAPIDITA -------------------------------------------------------------------
PRIMERA_PM_PLATATAFORMA_RAPI        = PREMIAR(VARIABLES.OBJ_PRIMERA_PM, PLATAFORMA_RAPI, USER_RAPIDITA).premiar




###! HORARIO DE BUSCAR NUMEROS
schedule.every().day.at('00:00:00').do(run, clearConsole)

#LOTERIAS AM PICKS ----------------------------------------------------------------
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

#LOTERIAS PM PICKS --------------------------------------------------------------
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