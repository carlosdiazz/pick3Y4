#ESTE SCRIPT SE DEJARA EJECUTANDO FIJO QUE ES QUIEN SE ENCARGAR DE BUSCAR A LA HORA ESPECIFICAS LOS DIFERENTES NUMEROS GANADORES

import schedule
import VARIABLES
from Buscar_premios import Buscar_Premio
from Funciones_Especiales import fecha, run, clearConsole
import time
from config import TIEMPO_A_BUSCAR

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

#LOTERIAS DOMINICANA ------------------------------------------------------
schedule.every().day.at(VARIABLES.OBJ_PRIMERA_AM['HORA']).do(run,LOTTERY_PRIMERA_AM )
schedule.every().day.at(VARIABLES.OBJ_PRIMERA_PM['HORA']).do(run, LOTTERY_PRIMERA_PM)
schedule.every().day.at(VARIABLES.OBJ_KING_AM['HORA']).do(run, LOTTERY_KING_LOTTERY_AM)
schedule.every().day.at(VARIABLES.OBJ_KING_PM['HORA']).do(run, LOTTERY_KING_LOTTERY_PM)
schedule.every().day.at(VARIABLES.OBJ_LA_SUERTE['HORA']).do(run, LOTTERY_LA_SUERTE)
schedule.every().day.at(VARIABLES.OBJ_REAL['HORA']).do(run,LOTTERY_REAL )
schedule.every().day.at(VARIABLES.OBJ_LOTEDOM['HORA']).do(run,LOTTERY_LOTEDOM )
schedule.every().day.at(VARIABLES.OBJ_GANAMAS['HORA']).do(run,LOTTERY_GANAMAS )
schedule.every().day.at(VARIABLES.OBJ_NACIONAL['HORA']).do(run,LOTTERY_NACIONAL )
schedule.every().day.at(VARIABLES.OBJ_LOTEKA['HORA']).do(run, LOTTERY_LOTEKA)
schedule.every().day.at(VARIABLES.OBJ_LEIDSA['HORA']).do(run,LOTTERY_LEIDSA )


##! HORARIO DE BUSCAR NUMEROS
schedule.every().day.at('00:00:00').do(run, clearConsole)

#LOTERIAS AM ----------------------------------------------------------------
schedule.every().day.at(VARIABLES.OBJ_FL_AM['HORA']).do(run, LOTERY_FLORIDA_AM)
schedule.every().day.at(VARIABLES.OBJ_NY_AM['HORA']).do(run, LOTERY_NEW_YORK_AM)
schedule.every().day.at(VARIABLES.OBJ_NJ_AM['HORA']).do(run, LOTERY_NEW_JERSEY_AM)
schedule.every().day.at(VARIABLES.OBJ_CT_AM['HORA']).do(run, LOTERY_CONNECTICUT_AM)
schedule.every().day.at(VARIABLES.OBJ_VA_AM['HORA']).do(run, LOTERY_VIRGINIA_AM)
schedule.every().day.at(VARIABLES.OBJ_DC_AM['HORA']).do(run, LOTERY_WASHINGTON_DC_AM)
schedule.every().day.at(VARIABLES.OBJ_PA_AM['HORA']).do(run, LOTERY_PENNSYLVANIA_AM)
schedule.every().day.at(VARIABLES.OBJ_SC_AM['HORA']).do(run, LOTERY_SOUTH_CAROLINA_AM)
schedule.every().day.at(VARIABLES.OBJ_GA_AM['HORA']).do(run, LOTERY_GEORGIA_AM)
schedule.every().day.at(VARIABLES.OBJ_NC_AM['HORA']).do(run, LOTERY_NORTH_CAROLINA_AM)

#LOTERIAS PM --------------------------------------------------------------
schedule.every().day.at(VARIABLES.OBJ_FL_PM['HORA']).do(run, LOTERY_FLORIDA_PM)
schedule.every().day.at(VARIABLES.OBJ_NY_PM['HORA']).do(run, LOTERY_NEW_YORK_PM)
schedule.every().day.at(VARIABLES.OBJ_NJ_PM['HORA']).do(run, LOTERY_NEW_JERSEY_PM)
schedule.every().day.at(VARIABLES.OBJ_CT_PM['HORA']).do(run, LOTERY_CONNECTICUT_PM)
schedule.every().day.at(VARIABLES.OBJ_VA_PM['HORA']).do(run, LOTERY_VIRGINIA_PM)
schedule.every().day.at(VARIABLES.OBJ_DC_PM['HORA']).do(run, LOTERY_WASHINGTON_DC_PM)
schedule.every().day.at(VARIABLES.OBJ_PA_PM['HORA']).do(run, LOTERY_PENNSYLVANIA_PM)
schedule.every().day.at(VARIABLES.OBJ_SC_AM['HORA']).do(run, LOTERY_SOUTH_CAROLINA_PM)
schedule.every().day.at(VARIABLES.OBJ_GA_PM['HORA']).do(run, LOTERY_GEORGIA_PM)
schedule.every().day.at(VARIABLES.OBJ_NC_PM['HORA']).do(run, LOTERY_NORTH_CAROLINA_PM)
schedule.every().day.at(VARIABLES.OBJ_GA_NIGHT['HORA']).do(run, LOTERY_GEORGIA_NIGHT)

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