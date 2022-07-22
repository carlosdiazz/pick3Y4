# ESTE SCRIPT SE DEJARA EJUCTANDO SIEMPRE QUE ES QUIEN PREMIA EN LA DIFERENTES PLATAFORMAS

import schedule
import VARIABLES
import time
from Funciones_Especiales import run, clearConsole, fecha
from PREMIAR_PICKS import PREMIAR_PICKS
from config import TIEMPO_A_BUSCAR

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

###! HORARIO DE BUSCAR NUMEROS
schedule.every().day.at('00:00:00').do(run, clearConsole)

#LOTERIAS AM ----------------------------------------------------------------
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

#LOTERIAS PM --------------------------------------------------------------
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

while True:
    fecha_actual = fecha('%d-%m-%Y || %H:%M:%S')
    print(f"|----------> {fecha_actual} <----------|")
    saber = schedule.run_pending()
    if(saber == None):
        pass
    else:
        print(schedule.run_pending())
    time.sleep(TIEMPO_A_BUSCAR)