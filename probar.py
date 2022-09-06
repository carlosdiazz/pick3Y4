
#? ESTE ARCHIVO ES SOLO PARA PROBAR CODIGO
import schedule
from Funciones_Especiales import fecha, run
import time
from config import TIEMPO_A_BUSCAR, hora_prueba
from Objectos_para_Automaticos import *

#! AGREGAR TODO EN PROBAR
#LOTERIAS DOMINICANA ----------------------------------------------------------------------
#schedule.every().day.at(hora_prueba).do(run,LOTTERY_PRIMERA_AM )
# schedule.every().day.at(hora_prueba).do(run, LOTTERY_PRIMERA_PM)
# schedule.every().day.at(hora_prueba).do(run, LOTTERY_KING_LOTTERY_AM)
# schedule.every().day.at(hora_prueba).do(run, LOTTERY_KING_LOTTERY_PM)
# schedule.every().day.at(hora_prueba).do(run, LOTTERY_LA_SUERTE)
# schedule.every().day.at(hora_prueba).do(run,LOTTERY_REAL )
# schedule.every().day.at(hora_prueba).do(run,LOTTERY_LOTEDOM )
# schedule.every().day.at(hora_prueba).do(run,LOTTERY_GANAMAS )
# schedule.every().day.at(hora_prueba).do(run,LOTTERY_NACIONAL )
# schedule.every().day.at(hora_prueba).do(run, LOTTERY_LOTEKA)
# schedule.every().day.at(hora_prueba).do(run,LOTTERY_LEIDSA )
# schedule.every().day.at(hora_prueba).do(run,LOTTERY_ANGUILLA_AM )
# schedule.every().day.at(hora_prueba).do(run,LOTTERY_ANGUILLA_MD )
# schedule.every().day.at(hora_prueba).do(run,LOTTERY_ANGUILLA_TARDE )
# schedule.every().day.at(hora_prueba).do(run,LOTTERY_ANGUILLA_PM )




#LOTERIAS QUE SON SUPER PALES ------------------------------------------------------------------
#schedule.every().day.at(hora_prueba).do(run, LOTTERY_SP_PRIMERA_GANAMAS)
#schedule.every().day.at(hora_prueba).do(run,LOTTERY_SP_REAL_PRIMERA )
#schedule.every().day.at(hora_prueba).do(run,LOTTERY_SP_NYAM_REAL )
#schedule.every().day.at(hora_prueba).do(run,LOTTERY_SP_REAL_GANAMAS)
#schedule.every().day.at(hora_prueba).do(run,LOTTERY_SP_NYAM_FLAM )
#schedule.every().day.at(hora_prueba).do(run, LOTTERY_SP_NYAM_LOTEKA)
#schedule.every().day.at(hora_prueba).do(run,LOTTERY_SP_NYAM_GANAMAS )
#schedule.every().day.at(hora_prueba).do(run,LOTTERY_SP_GANAMAS_LOTEKA )
#schedule.every().day.at(hora_prueba).do(run, LOTTERY_SP_NACIONAL_LEIDSA)
#schedule.every().day.at(hora_prueba).do(run, LOTTERY_SP_LOTEKA_NACIONAL)
#schedule.every().day.at(hora_prueba).do(run,LOTTERY_SP_NYPM_NACIONAL)
#schedule.every().day.at(hora_prueba).do(run, LOTTERY_SP_NYPM_FLPM)

#PREMIOS SUPER PALES SANCHEZ ---------------------------------------------------------------------------------------
#schedule.every().day.at(hora_prueba).do(run, SANCHEZ_SP_REAL_PRIMERA)
#schedule.every().day.at(hora_prueba).do(run, SANCHEZ_SP_PRIMERA_GANAMAS)
#schedule.every().day.at(hora_prueba).do(run, SANCHEZ_SP_NYAM_REAL)
#schedule.every().day.at(hora_prueba).do(run,SANCHEZ_SP_REAl_GANAMAS )
#schedule.every().day.at(hora_prueba).do(run, SANCHEZ_SP_NYAM_FLAM)
#schedule.every().day.at(hora_prueba).do(run,SANCHEZ_SP_NYAM_GANAMAS )
#schedule.every().day.at(hora_prueba).do(run,SANCHEZ_SP_NYAM_LOTEKA )
#schedule.every().day.at(hora_prueba).do(run,SANCHEZ_SP_GANAMAS_LOTEKA )
#schedule.every().day.at(hora_prueba).do(run, SANCHEZ_SP_LOTEKA_NACIONAL)
#schedule.every().day.at(hora_prueba).do(run, SANCHEZ_SP_NACIONAL_LEIDSA)


#PREMIOS SANCHEZ PICKS PM --------------------------------------------------------------------------
#schedule.every().day.at(hora_prueba).do(run, SANCHEZ_MARYLAND_EVENING)
#schedule.every().day.at(hora_prueba).do(run, SANCHEZ_GEORGIA_EVENING)
#schedule.every().day.at(hora_prueba).do(run, SANCHEZ_MAINE_EVENING)
#schedule.every().day.at(hora_prueba).do(run, SANCHEZ_VERMOMT_EVENING )
#schedule.every().day.at(hora_prueba).do(run, SANCHEZ_NEW_HAMPSHIRE_EVENING )

#PREMIOS AMERICANAS PM PERO COMO DOMINICANA SANCHEZ -----------------------------------------------------------------------
#schedule.every().day.at(hora_prueba).do(run, SANCHEZ_MARYLAND_RD_PM )
#schedule.every().day.at(hora_prueba).do(run, SANCHEZ_VERMONT_RD_PM)
#schedule.every().day.at(hora_prueba).do(run, SANCHEZ_NEW_HAMPSHIRE_RD_PM)
#schedule.every().day.at(hora_prueba).do(run, SANCHEZ_MAINE_RD_PM)
#schedule.every().day.at(hora_prueba).do(run, SANCHEZ_GEORGIA_RD_PM)

#schedule.every().day.at(hora_prueba).do(run, PRIMERA_PM_PLATATAFORMA_RAPI)

while True:
    fecha_actual = fecha('%d-%m-%Y || %H:%M:%S')
    print(f"|---------- PRUEBAS --> {fecha_actual} <----------|")
    saber = schedule.run_pending()
    if(saber == None):
        pass
    else:
        print(schedule.run_pending())
    time.sleep(TIEMPO_A_BUSCAR)