#ESTE SCRIPT SE DEJARA EJECUTANDO FIJO QUE ES QUIEN SE ENCARGAR DE BUSCAR A LA HORA ESPECIFICAS LOS DIFERENTES NUMEROS GANADORES

import schedule
import VARIABLES
from Buscar_premios import Buscar_Premio
from Funciones_Especiales import fecha, run, clearConsole
import time
from config import TIEMPO_A_BUSCAR
from PREMIAR_PICKS import PREMIAR_PICKS

#! ME FALTA ....  TENGO QUE ENVIAR UNA FECHA DEL SORTEO QUE BUSCO Y ESA MISMA FECHA PUBLICARALA
#! EN VEZ DE COLOCAR LA FECHA DEL ARCHIVO API< TENMGO QUE ENVBIAR UNA FECHA A BUSCAR SOBRE TODO PARA CUANDP SE PASE DE LAS 12 DE LA NOCHE

#LOTERIAS AM ----------------------------------------------------------------

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

#LOTERIAS PM -------------------------------------------------------------
LOTERY_FLORIDA_PM                =   Buscar_Premio(VARIABLES.OBJ_FL_PM).Buscar_numeros_ganadores
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

#LOTERIAS AM
FLORIDA_MIDDAY              =   PREMIAR_PICKS(VARIABLES.OBJ_FL_AM).premiar
NEW_YORK_MIDDAY             =   PREMIAR_PICKS(VARIABLES.OBJ_NY_AM).premiar
VIRGINIA_MIDDAY             =   PREMIAR_PICKS(VARIABLES.OBJ_VA_AM).premiar
GEORGIA_MIDDAY              =   PREMIAR_PICKS(VARIABLES.OBJ_GA_AM).premiar
NEW_JERSEY_MIDDAY           =   PREMIAR_PICKS(VARIABLES.OBJ_NJ_AM).premiar
SOUTH_CAROLINA_MIDDAY       =   PREMIAR_PICKS(VARIABLES.OBJ_SC_AM).premiar
PENNSYLVANIA_MIDDAY         =   PREMIAR_PICKS(VARIABLES.OBJ_PA_AM).premiar
WASHINGTON_DC_MIDDAY        =   PREMIAR_PICKS(VARIABLES.OBJ_DC_AM).premiar
CONNECTICUT_MIDDAY          =   PREMIAR_PICKS(VARIABLES.OBJ_CT_AM).premiar
NORTH_CAROLINA_MIDDAY       =   PREMIAR_PICKS(VARIABLES.OBJ_NC_AM).premiar
#LOTERIAS PM
SOUTH_CAROLINA_EVENING      =   PREMIAR_PICKS(VARIABLES.OBJ_SC_PM).premiar
GEORGIA_EVENING             =   PREMIAR_PICKS(VARIABLES.OBJ_GA_PM).premiar
PENNSYLVANIA_EVENING        =   PREMIAR_PICKS(VARIABLES.OBJ_PA_PM).premiar
WASHINGTON_DC_EVENING       =   PREMIAR_PICKS(VARIABLES.OBJ_DC_PM).premiar
FLORIDA_EVENING             =   PREMIAR_PICKS(VARIABLES.OBJ_FL_PM).premiar
CONNECTICUT_EVENING         =   PREMIAR_PICKS(VARIABLES.OBJ_CT_PM).premiar
NEW_YORK_EVENING            =   PREMIAR_PICKS(VARIABLES.OBJ_NY_PM).premiar
VIRGINIA_EVENING            =   PREMIAR_PICKS(VARIABLES.OBJ_VA_PM).premiar
NEW_JERSEY_EVENING          =   PREMIAR_PICKS(VARIABLES.OBJ_NJ_PM).premiar
NORTH_CAROLINA_EVENING      =   PREMIAR_PICKS(VARIABLES.OBJ_NC_PM).premiar
GEORGIA_NIGHT               =   PREMIAR_PICKS(VARIABLES.OBJ_GA_NIGHT).premiar

##! HORARIO DE BUSCAR NUMEROS


hora_prueba =  '00:05:50'
####! BORRAR ESTO
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
##! schedule.every().day.at(hora_prueba).do(run, LOTERY_NORTH_CAROLINA_PM)

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
#schedule.every().day.at(hora_prueba).do(run, CONNECTICUT_EVENING)
schedule.every().day.at(hora_prueba).do(run, VIRGINIA_EVENING)
#schedule.every().day.at(hora_prueba).do(run, NEW_JERSEY_EVENING)
schedule.every().day.at(hora_prueba).do(run, NORTH_CAROLINA_EVENING)
#schedule.every().day.at(hora_prueba).do(run, GEORGIA_NIGHT)


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