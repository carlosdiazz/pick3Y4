
#? ESTE ARCHIVO ES SOLO PARA PROBAR CODIGO
import schedule
import VARIABLES
from Buscar_premios import Buscar_Premio
from Funciones_Especiales import fecha, run, clearConsole
import time
from config import TIEMPO_A_BUSCAR, hora_prueba
from PREMIAR import PREMIAR
from Datos_Loterias.DATOS_PLATAFORMA import PLATAFORMA_MEGA, USER_MEGALOTTERY, PLATAFORMA_RAPI, USER_RAPIDITA


#LOTERIAS AMERICANA AM ---------------------------------------------------------------- BUSCAR NUMEROS

LOTERY_FLORIDA_AM               =   Buscar_Premio(VARIABLES.OBJ_FL_AM).Buscar_numeros_ganadores
LOTERY_NEW_YORK_AM              =   Buscar_Premio(VARIABLES.OBJ_NY_AM).Buscar_numeros_ganadores
LOTERY_NEW_JERSEY_AM            =   Buscar_Premio(VARIABLES.OBJ_NJ_AM).Buscar_numeros_ganadores
LOTERY_CONNECTICUT_AM           =   Buscar_Premio(VARIABLES.OBJ_CT_AM).Buscar_numeros_ganadores
LOTERY_VIRGINIA_AM              =   Buscar_Premio(VARIABLES.OBJ_VA_AM).Buscar_numeros_ganadores
LOTERY_WASHINGTON_DC_AM         =   Buscar_Premio(VARIABLES.OBJ_DC_AM).Buscar_numeros_ganadores
LOTERY_PENNSYLVANIA_AM          =   Buscar_Premio(VARIABLES.OBJ_PA_AM).Buscar_numeros_ganadores
LOTERY_SOUTH_CAROLINA_AM        =   Buscar_Premio(VARIABLES.OBJ_SC_AM).Buscar_numeros_ganadores
LOTERY_NORTH_CAROLINA_AM        =   Buscar_Premio(VARIABLES.OBJ_NC_AM).Buscar_numeros_ganadores
LOTERY_GEORGIA_AM               =   Buscar_Premio(VARIABLES.OBJ_GA_AM).Buscar_numeros_ganadores

#LOTERIAS AMERICANA PM ------------------------------------------------------------- BUSCAR NUMEROS
LOTERY_FLORIDA_PM               =   Buscar_Premio(VARIABLES.OBJ_FL_PM).Buscar_numeros_ganadores
LOTERY_NEW_YORK_PM              =   Buscar_Premio(VARIABLES.OBJ_NY_PM).Buscar_numeros_ganadores
LOTERY_NEW_JERSEY_PM            =   Buscar_Premio(VARIABLES.OBJ_NJ_PM).Buscar_numeros_ganadores
LOTERY_CONNECTICUT_PM           =   Buscar_Premio(VARIABLES.OBJ_CT_PM).Buscar_numeros_ganadores
LOTERY_VIRGINIA_PM              =   Buscar_Premio(VARIABLES.OBJ_VA_PM).Buscar_numeros_ganadores
LOTERY_WASHINGTON_DC_PM         =   Buscar_Premio(VARIABLES.OBJ_DC_PM).Buscar_numeros_ganadores
LOTERY_PENNSYLVANIA_PM          =   Buscar_Premio(VARIABLES.OBJ_PA_PM).Buscar_numeros_ganadores
LOTERY_SOUTH_CAROLINA_PM        =   Buscar_Premio(VARIABLES.OBJ_SC_PM).Buscar_numeros_ganadores
LOTERY_NORTH_CAROLINA_PM        =   Buscar_Premio(VARIABLES.OBJ_NC_PM).Buscar_numeros_ganadores
LOTERY_GEORGIA_PM               =   Buscar_Premio(VARIABLES.OBJ_GA_PM).Buscar_numeros_ganadores
LOTERY_GEORGIA_NIGHT            =   Buscar_Premio(VARIABLES.OBJ_GA_NIGHT).Buscar_numeros_ganadores

#LOTERIAS DOMINICANA AM ------------------------------------------------------------- BUSCAR NUMEROS
#LOTERIAS DOMINICANA --------------------------------------------------------

LOTTERY_PRIMERA_AM              =   Buscar_Premio(VARIABLES.OBJ_PRIMERA_AM).Buscar_numeros_ganadores
LOTTERY_PRIMERA_PM              =   Buscar_Premio(VARIABLES.OBJ_PRIMERA_PM).Buscar_numeros_ganadores

LOTTERY_KING_LOTTERY_AM         =   Buscar_Premio(VARIABLES.OBJ_KING_AM).Buscar_numeros_ganadores
LOTTERY_KING_LOTTERY_PM         =   Buscar_Premio(VARIABLES.OBJ_KING_PM).Buscar_numeros_ganadores

LOTTERY_LA_SUERTE               =   Buscar_Premio(VARIABLES.OBJ_LA_SUERTE).Buscar_numeros_ganadores

LOTTERY_REAL                    =   Buscar_Premio(VARIABLES.OBJ_REAL).Buscar_numeros_ganadores
LOTTERY_LOTEDOM                 =   Buscar_Premio(VARIABLES.OBJ_LOTEDOM).Buscar_numeros_ganadores

LOTTERY_GANAMAS                 =   Buscar_Premio(VARIABLES.OBJ_GANAMAS).Buscar_numeros_ganadores
LOTTERY_NACIONAL                =   Buscar_Premio(VARIABLES.OBJ_NACIONAL).Buscar_numeros_ganadores

LOTTERY_LOTEKA                  =   Buscar_Premio(VARIABLES.OBJ_LOTEKA).Buscar_numeros_ganadores

LOTTERY_LEIDSA                  =   Buscar_Premio(VARIABLES.OBJ_LEIDSA).Buscar_numeros_ganadores

LOTTERY_ANGUILLA_AM             =   Buscar_Premio(VARIABLES.OBJ_ANGUILLA_AM).Buscar_numeros_ganadores
LOTTERY_ANGUILLA_MD             =   Buscar_Premio(VARIABLES.OBJ_ANGUILLA_MD).Buscar_numeros_ganadores
LOTTERY_ANGUILLA_TARDE          =   Buscar_Premio(VARIABLES.OBJ_ANGUILLA_TARDE).Buscar_numeros_ganadores
LOTTERY_ANGUILLA_PM             =   Buscar_Premio(VARIABLES.OBJ_ANGUILLA_PM).Buscar_numeros_ganadores

#LOTERIAS DOMINICANA BUSCAR NUMEROS------------------------------------------------------
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


#! -------------------------------------------------------------------------------------------------
#LOTERIAS AM
FLORIDA_MIDDAY              =   PREMIAR(VARIABLES.OBJ_FL_AM,PLATAFORMA_MEGA,USER_MEGALOTTERY).premiar
NEW_YORK_MIDDAY             =   PREMIAR(VARIABLES.OBJ_NY_AM,PLATAFORMA_MEGA,USER_MEGALOTTERY).premiar
VIRGINIA_MIDDAY             =   PREMIAR(VARIABLES.OBJ_VA_AM,PLATAFORMA_MEGA,USER_MEGALOTTERY).premiar
GEORGIA_MIDDAY              =   PREMIAR(VARIABLES.OBJ_GA_AM,PLATAFORMA_MEGA,USER_MEGALOTTERY).premiar
NEW_JERSEY_MIDDAY           =   PREMIAR(VARIABLES.OBJ_NJ_AM,PLATAFORMA_MEGA,USER_MEGALOTTERY).premiar
SOUTH_CAROLINA_MIDDAY       =   PREMIAR(VARIABLES.OBJ_SC_AM,PLATAFORMA_MEGA,USER_MEGALOTTERY).premiar
PENNSYLVANIA_MIDDAY         =   PREMIAR(VARIABLES.OBJ_PA_AM,PLATAFORMA_MEGA,USER_MEGALOTTERY).premiar
WASHINGTON_DC_MIDDAY        =   PREMIAR(VARIABLES.OBJ_DC_AM,PLATAFORMA_MEGA,USER_MEGALOTTERY).premiar
CONNECTICUT_MIDDAY          =   PREMIAR(VARIABLES.OBJ_CT_AM,PLATAFORMA_MEGA,USER_MEGALOTTERY).premiar
NORTH_CAROLINA_MIDDAY       =   PREMIAR(VARIABLES.OBJ_NC_AM,PLATAFORMA_MEGA,USER_MEGALOTTERY).premiar
#LOTERIAS PM
SOUTH_CAROLINA_EVENING      =   PREMIAR(VARIABLES.OBJ_SC_PM, PLATAFORMA_MEGA, USER_MEGALOTTERY).premiar
GEORGIA_EVENING             =   PREMIAR(VARIABLES.OBJ_GA_PM, PLATAFORMA_MEGA, USER_MEGALOTTERY).premiar
PENNSYLVANIA_EVENING        =   PREMIAR(VARIABLES.OBJ_PA_PM, PLATAFORMA_MEGA, USER_MEGALOTTERY).premiar
WASHINGTON_DC_EVENING       =   PREMIAR(VARIABLES.OBJ_DC_PM, PLATAFORMA_MEGA, USER_MEGALOTTERY).premiar
FLORIDA_EVENING             =   PREMIAR(VARIABLES.OBJ_FL_PM, PLATAFORMA_MEGA, USER_MEGALOTTERY).premiar
CONNECTICUT_EVENING         =   PREMIAR(VARIABLES.OBJ_CT_PM, PLATAFORMA_MEGA, USER_MEGALOTTERY).premiar
NEW_YORK_EVENING            =   PREMIAR(VARIABLES.OBJ_NY_PM, PLATAFORMA_MEGA, USER_MEGALOTTERY).premiar
VIRGINIA_EVENING            =   PREMIAR(VARIABLES.OBJ_VA_PM, PLATAFORMA_MEGA, USER_MEGALOTTERY).premiar
NEW_JERSEY_EVENING          =   PREMIAR(VARIABLES.OBJ_NJ_PM, PLATAFORMA_MEGA, USER_MEGALOTTERY).premiar
NORTH_CAROLINA_EVENING      =   PREMIAR(VARIABLES.OBJ_NC_PM, PLATAFORMA_MEGA, USER_MEGALOTTERY).premiar
GEORGIA_NIGHT               =   PREMIAR(VARIABLES.OBJ_GA_NIGHT, PLATAFORMA_MEGA, USER_MEGALOTTERY).premiar

#LOTERIAS TRADICIONALES MEGALOTTERY -------------------------------------------------------------------
PRIMERA_PM_PLATATAFORMA_MEGA        = PREMIAR(VARIABLES.OBJ_PRIMERA_PM, PLATAFORMA_MEGA, USER_MEGALOTTERY).premiar

#LOTERIAS TRADICIONALES RAPIDITA -------------------------------------------------------------------
PRIMERA_PM_PLATATAFORMA_RAPI        = PREMIAR(VARIABLES.OBJ_PRIMERA_PM, PLATAFORMA_RAPI, USER_RAPIDITA).premiar



####! AQUI PRUEBO BUSCAR LOS NUMEROS AUTOMATICO
#schedule.every().day.at(hora_prueba).do(run, LOTERY_FLORIDA_AM)
#schedule.every().day.at(hora_prueba).do(run, LOTERY_FLORIDA_PM)
#schedule.every().day.at(hora_prueba).do(run, LOTERY_NEW_YORK_AM)
#schedule.every().day.at(hora_prueba).do(run, LOTERY_NEW_YORK_PM)
#schedule.every().day.at(hora_prueba).do(run, LOTERY_NEW_JERSEY_AM)
#schedule.every().day.at(hora_prueba).do(run, LOTERY_NEW_JERSEY_PM)
#schedule.every().day.at(hora_prueba).do(run, LOTERY_CONNECTICUT_AM)
#schedule.every().day.at(hora_prueba).do(run, LOTERY_CONNECTICUT_PM)
#schedule.every().day.at(hora_prueba).do(run, LOTERY_VIRGINIA_AM)
#schedule.every().day.at(hora_prueba).do(run, LOTERY_VIRGINIA_PM)
#schedule.every().day.at(hora_prueba).do(run, LOTERY_WASHINGTON_DC_AM)
#schedule.every().day.at(hora_prueba).do(run, LOTERY_WASHINGTON_DC_PM)
#schedule.every().day.at(hora_prueba).do(run, LOTERY_PENNSYLVANIA_AM)
#schedule.every().day.at(hora_prueba).do(run, LOTERY_PENNSYLVANIA_PM)
#schedule.every().day.at(hora_prueba).do(run, LOTERY_SOUTH_CAROLINA_AM)
#schedule.every().day.at(hora_prueba).do(run, LOTERY_SOUTH_CAROLINA_PM)
#schedule.every().day.at(hora_prueba).do(run, LOTERY_GEORGIA_AM)
#schedule.every().day.at(hora_prueba).do(run, LOTERY_GEORGIA_PM)
#schedule.every().day.at(hora_prueba).do(run, LOTERY_GEORGIA_NIGHT)
#schedule.every().day.at(hora_prueba).do(run, LOTERY_NORTH_CAROLINA_AM)
#schedule.every().day.at(hora_prueba).do(run, LOTERY_NORTH_CAROLINA_PM)

####! AQUI PRUEBO PREMIAR LAS LOTERIAS AUTOMATICO
## schedule.every().day.at(hora_prueba).do(run, FLORIDA_MIDDAY)
## schedule.every().day.at(hora_prueba).do(run, NEW_YORK_MIDDAY)
## schedule.every().day.at(hora_prueba).do(run, VIRGINIA_MIDDAY)
## schedule.every().day.at(hora_prueba).do(run, GEORGIA_MIDDAY)
## schedule.every().day.at(hora_prueba).do(run, NEW_JERSEY_MIDDAY)
## schedule.every().day.at(hora_prueba).do(run, SOUTH_CAROLINA_MIDDAY)
## schedule.every().day.at(hora_prueba).do(run, PENNSYLVANIA_MIDDAY)
## schedule.every().day.at(hora_prueba).do(run, WASHINGTON_DC_MIDDAY)
## schedule.every().day.at(hora_prueba).do(run, CONNECTICUT_MIDDAY)
## schedule.every().day.at(hora_prueba).do(run, NORTH_CAROLINA_MIDDAY)
## schedule.every().day.at(hora_prueba).do(run, SOUTH_CAROLINA_EVENING)
## schedule.every().day.at(hora_prueba).do(run, GEORGIA_EVENING)
## schedule.every().day.at(hora_prueba).do(run, PENNSYLVANIA_EVENING)
## schedule.every().day.at(hora_prueba).do(run, WASHINGTON_DC_EVENING)
## schedule.every().day.at(hora_prueba).do(run, FLORIDA_EVENING)
## schedule.every().day.at(hora_prueba).do(run, NEW_YORK_EVENING)
## schedule.every().day.at(hora_prueba).do(run, CONNECTICUT_EVENING)
## schedule.every().day.at(hora_prueba).do(run, VIRGINIA_EVENING)
## schedule.every().day.at(hora_prueba).do(run, NEW_JERSEY_EVENING)
## schedule.every().day.at(hora_prueba).do(run, NORTH_CAROLINA_EVENING)
## schedule.every().day.at(hora_prueba).do(run, GEORGIA_NIGHT)

# OTRAS LOTERIA PARA PREMIAR ---------------------------------------------------------
## schedule.every().day.at(hora_prueba).do(run, PRIMERA_PM_PLATATAFORMA_MEGA)
## schedule.every().day.at(hora_prueba).do(run, PRIMERA_PM_PLATATAFORMA_RAPI)


clearConsole()
while True:
    fecha_actual = fecha('%d-%m-%Y || %H:%M:%S')
    print(f"|----------> {fecha_actual} <----------|")
    saber = schedule.run_pending()
    if(saber == None):
        pass
    else:
        print(schedule.run_pending())
    time.sleep(TIEMPO_A_BUSCAR)