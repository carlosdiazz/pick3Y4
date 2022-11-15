import os
#? ESTE ARCHIVO ES SOLO PARA PROBAR CODIGO
import schedule
from Funciones_Especiales import fecha, run
import time
from config import TIEMPO_A_BUSCAR, hora_prueba
from Objectos_para_Automaticos import *



# loterias =  """
# schedule.every().day.at(hora_prueba).do(run,LOTTERY_PRIMERA_AM )
# """

#def generate_list( list ):
#    data_final = ""
#    for loteria in list:
#        data_final+=f"schedule.every().day.at(hora_prueba).do(run,{loteria} )\n"
#    print(data_final)
#    return data_final

PID = os.getpid()
print("==>", PID)

#  #! BUSCAR NUMEROS GANADORES
#  #?BUSCAR LOTERIAS DOMINICANA AM ----------------------------------------------------------------------
LOTERIAS_DOMINICANA_AM = [ 'LOTTERY_PRIMERA_AM', 'LOTTERY_KING_LOTTERY_AM', 'LOTTERY_LA_SUERTE', 'LOTTERY_REAL', 'LOTTERY_LOTEDOM', 'LOTTERY_GANAMAS', 'LOTTERY_ANGUILLA_AM', 'LOTTERY_ANGUILLA_MD']
#  schedule.every().day.at(hora_prueba).do(run,LOTTERY_PRIMERA_AM )
#  schedule.every().day.at(hora_prueba).do(run, LOTTERY_KING_LOTTERY_AM)
#  schedule.every().day.at(hora_prueba).do(run, LOTTERY_LA_SUERTE)
#  schedule.every().day.at(hora_prueba).do(run,LOTTERY_REAL )
#  schedule.every().day.at(hora_prueba).do(run,LOTTERY_LOTEDOM )
#  schedule.every().day.at(hora_prueba).do(run,LOTTERY_GANAMAS )
#  schedule.every().day.at(hora_prueba).do(run,LOTTERY_ANGUILLA_AM )
#  schedule.every().day.at(hora_prueba).do(run,LOTTERY_ANGUILLA_MD )
#
#  #?BUSCAR LOTERIAS DOMINICANA PM ---------------------------------------------------------------------
LOTERIAS_DOMINICANA_PM = ['LOTTERY_PRIMERA_PM','LOTTERY_KING_LOTTERY_PM','LOTTERY_NACIONAL','LOTTERY_LOTEKA','LOTTERY_LEIDSA','LOTTERY_ANGUILLA_TARDE','LOTTERY_ANGUILLA_PM']
#  schedule.every().day.at(hora_prueba).do(run, LOTTERY_PRIMERA_PM)
#  schedule.every().day.at(hora_prueba).do(run, LOTTERY_KING_LOTTERY_PM)
#  schedule.every().day.at(hora_prueba).do(run,LOTTERY_NACIONAL )
#  schedule.every().day.at(hora_prueba).do(run, LOTTERY_LOTEKA)
#  schedule.every().day.at(hora_prueba).do(run,LOTTERY_LEIDSA )
#  schedule.every().day.at(hora_prueba).do(run,LOTTERY_ANGUILLA_TARDE )
#  schedule.every().day.at(hora_prueba).do(run,LOTTERY_ANGUILLA_PM )
#
#  #?BUSCAR LOTERIAS AMERICANA PICKS AM ----------------------------------------------------------------
LOTERIAS_AMERICANA_picks_am = ['LOTERY_FLORIDA_AM','LOTERY_NEW_YORK_AM','LOTERY_NEW_JERSEY_AM','LOTERY_CONNECTICUT_AM','LOTERY_VIRGINIA_AM','LOTERY_WASHINGTON_DC_AM','LOTERY_PENNSYLVANIA_AM','LOTERY_SOUTH_CAROLINA_AM','LOTERY_GEORGIA_AM','LOTERY_NORTH_CAROLINA_AM','LOTERY_MARYLAND_AM','LOTERY_VERMONT_AM','LOTERY_NEW_HAMPSHIRE_AM','LOTERY_MAINE_AM','LOTERY_ILLINOIS_AM']
#schedule.every().day.at(hora_prueba).do(run, LOTERY_FLORIDA_AM)
#schedule.every().day.at(hora_prueba).do(run, LOTERY_NEW_YORK_AM)
#schedule.every().day.at(hora_prueba).do(run, LOTERY_NEW_JERSEY_AM)
#schedule.every().day.at(hora_prueba).do(run, LOTERY_CONNECTICUT_AM)
#schedule.every().day.at(hora_prueba).do(run, LOTERY_VIRGINIA_AM)
#schedule.every().day.at(hora_prueba).do(run, LOTERY_WASHINGTON_DC_AM)
#schedule.every().day.at(hora_prueba).do(run, LOTERY_PENNSYLVANIA_AM)
#schedule.every().day.at(hora_prueba).do(run, LOTERY_SOUTH_CAROLINA_AM)
#schedule.every().day.at(hora_prueba).do(run, LOTERY_GEORGIA_AM)
#schedule.every().day.at(hora_prueba).do(run, LOTERY_NORTH_CAROLINA_AM)
#schedule.every().day.at(hora_prueba).do(run, LOTERY_MARYLAND_AM)
#schedule.every().day.at(hora_prueba).do(run, LOTERY_VERMONT_AM)
#schedule.every().day.at(hora_prueba).do(run, LOTERY_NEW_HAMPSHIRE_AM)
#schedule.every().day.at(hora_prueba).do(run, LOTERY_MAINE_AM)
#schedule.every().day.at(hora_prueba).do(run, LOTERY_ILLINOIS_AM)
#
#  LOTERIAS AMERICANA__IC
#  #?BUSCAR LOTERIAS AMERICANA PICKS PM --------------------------------------------------------------
#  schedule.every().day.at(hora_prueba).do(run, LOTERY_FLORIDA_PM)
#  schedule.every().day.at(hora_prueba).do(run, LOTERY_NEW_YORK_PM)
#  schedule.every().day.at(hora_prueba).do(run, LOTERY_NEW_JERSEY_PM)
#  schedule.every().day.at(hora_prueba).do(run, LOTERY_CONNECTICUT_PM)
#  schedule.every().day.at(hora_prueba).do(run, LOTERY_VIRGINIA_PM)
#  schedule.every().day.at(hora_prueba).do(run, LOTERY_WASHINGTON_DC_PM)
#  schedule.every().day.at(hora_prueba).do(run, LOTERY_PENNSYLVANIA_PM)
#  schedule.every().day.at(hora_prueba).do(run, LOTERY_GEORGIA_PM)
#  schedule.every().day.at(hora_prueba).do(run, LOTERY_NORTH_CAROLINA_PM)
#  schedule.every().day.at(hora_prueba).do(run, LOTERY_MARYLAND_PM)
#  schedule.every().day.at(hora_prueba).do(run, LOTERY_VERMONT_PM)
#  schedule.every().day.at(hora_prueba).do(run, LOTERY_NEW_HAMPSHIRE_PM)
#  schedule.every().day.at(hora_prueba).do(run, LOTERY_MAINE_PM)
#  schedule.every().day.at(hora_prueba).do(run, LOTERY_ILLINOIS_PM)
#  schedule.every().day.at(hora_prueba).do(run, LOTERY_CALIFORNIA_PM)
#  schedule.every().day.at(hora_prueba).do(run, LOTERY_GEORGIA_NIGHT)
#  schedule.every().day.at(hora_prueba).do(run, LOTERY_SOUTH_CAROLINA_PM)
#
#  LOTERIAS QUE SON_SU_ER
#  #?BUSCAR LOTERIAS QUE SON SUPER PALES ------------------------------------------------------------------
#  schedule.every().day.at(hora_prueba).do(run, LOTTERY_SP_PRIMERA_GANAMAS)
#  schedule.every().day.at(hora_prueba).do(run,LOTTERY_SP_REAL_PRIMERA )
#  schedule.every().day.at(hora_prueba).do(run,LOTTERY_SP_NYAM_REAL )
#  schedule.every().day.at(hora_prueba).do(run,LOTTERY_SP_REAL_GANAMAS)
#  schedule.every().day.at(hora_prueba).do(run,LOTTERY_SP_NYAM_FLAM )
#  schedule.every().day.at(hora_prueba).do(run, LOTTERY_SP_NYAM_LOTEKA)
#  schedule.every().day.at(hora_prueba).do(run,LOTTERY_SP_NYAM_GANAMAS )
#  schedule.every().day.at(hora_prueba).do(run,LOTTERY_SP_GANAMAS_LOTEKA )
#  schedule.every().day.at(hora_prueba).do(run, LOTTERY_SP_NACIONAL_LEIDSA)
#  schedule.every().day.at(hora_prueba).do(run, LOTTERY_SP_LOTEKA_NACIONAL)
#  schedule.every().day.at(hora_prueba).do(run,LOTTERY_SP_NYPM_NACIONAL)
#  schedule.every().day.at(hora_prueba).do(run, LOTTERY_SP_NYPM_FLPM)
#
#  #! PREMIOS EN TODA LA PLATAFORMA
#  #?PREMIAR PICKS AM MEGALOTERY-----------------------------------------------------------
#  schedule.every().day.at(hora_prueba).do(run, FLORIDA_MIDDAY)
#  schedule.every().day.at(hora_prueba).do(run, NEW_YORK_MIDDAY)
#  schedule.every().day.at(hora_prueba).do(run, VIRGINIA_MIDDAY)
#  schedule.every().day.at(hora_prueba).do(run, GEORGIA_MIDDAY)
#  schedule.every().day.at(hora_prueba).do(run, NEW_JERSEY_MIDDAY)
#  schedule.every().day.at(hora_prueba).do(run, PENNSYLVANIA_MIDDAY)
#  schedule.every().day.at(hora_prueba).do(run, WASHINGTON_DC_MIDDAY)
#  schedule.every().day.at(hora_prueba).do(run, CONNECTICUT_MIDDAY)
#  schedule.every().day.at(hora_prueba).do(run, NORTH_CAROLINA_MIDDAY)
#  schedule.every().day.at(hora_prueba).do(run, MARYLAND_MIDDAY)
#  schedule.every().day.at(hora_prueba).do(run, SOUTH_CAROLINA_MIDDAY)
#
#  #?PREMIAR PICKS PM MEGALOTERY-----------------------------------------------------------
#  schedule.every().day.at(hora_prueba).do(run, SOUTH_CAROLINA_EVENING)
#  schedule.every().day.at(hora_prueba).do(run, GEORGIA_EVENING)
#  schedule.every().day.at(hora_prueba).do(run, PENNSYLVANIA_EVENING)
#  schedule.every().day.at(hora_prueba).do(run, WASHINGTON_DC_EVENING)
#  schedule.every().day.at(hora_prueba).do(run, FLORIDA_EVENING)
#  schedule.every().day.at(hora_prueba).do(run, NEW_YORK_EVENING)
#  schedule.every().day.at(hora_prueba).do(run, CONNECTICUT_EVENING)
#  schedule.every().day.at(hora_prueba).do(run, VIRGINIA_EVENING)
#  schedule.every().day.at(hora_prueba).do(run, NEW_JERSEY_EVENING)
#  schedule.every().day.at(hora_prueba).do(run, NORTH_CAROLINA_EVENING)
#  schedule.every().day.at(hora_prueba).do(run, GEORGIA_NIGHT)
#  schedule.every().day.at(hora_prueba).do(run, MARYLAND_EVENING)
#
#  #?LOTERIA DOMINIACANA EN MEGA Y RAPIDITA --------------------------------------------------------------0---
#  schedule.every().day.at(hora_prueba).do(run, PRIMERA_PM_PLATATAFORMA_MEGA)
#  schedule.every().day.at(hora_prueba).do(run, PRIMERA_PM_PLATATAFORMA_RAPI)
#  schedule.every().day.at(hora_prueba).do(run, KING_LOTTERY_AM_PLATATAFORMA_MEGA)
#  schedule.every().day.at(hora_prueba).do(run, KING_LOTTERY_PM_PLATATAFORMA_MEGA)
#  schedule.every().day.at(hora_prueba).do(run, GEORGIA_AM_PLATAFORMA_MEGA)
#  schedule.every().day.at(hora_prueba).do(run, GEORGIA_PM_PLATAFORMA_MEGA)
#  schedule.every().day.at(hora_prueba).do(run, GEORGIA_NIGHT_PLATAFORMA_MEGA)
#  schedule.every().day.at(hora_prueba).do(run, NEW_JERSEY_AM_PLATAFORMA_MEGA)
#  schedule.every().day.at(hora_prueba).do(run, NEW_JERSEY_PM_PLATAFORMA_MEGA)
#
#  #?OTRAS LOTERIA PARA PREMIAR EN LOTEDOM ---------------------------------------------------------
#  schedule.every().day.at(hora_prueba).do(run, NEW_YORK_PM_LOTEDOM)
#  schedule.every().day.at(hora_prueba).do(run, FLORIDA_PM_LOTEDOM)
#
#  #?PREMIOS SANCHEZ PICKS AM --------------------------------------------------------------------------
#  schedule.every().day.at(hora_prueba).do(run, SANCHEZ_MARYLAND_MIDDAY)
#  schedule.every().day.at(hora_prueba).do(run, SANCHEZ_NEW_HAMPSHIRE_MIDDAY)
#  schedule.every().day.at(hora_prueba).do(run, SANCHEZ_MAINE_MIDDAY )
#  schedule.every().day.at(hora_prueba).do(run, SANCHEZ_VERMOMT_MIDDAY )
#  schedule.every().day.at(hora_prueba).do(run, SANCHEZ_GEORGIA_MIDDAY)
#  schedule.every().day.at(hora_prueba).do(run, SANCHEZ_NEW_JERSEY_MIDDAY)
#  schedule.every().day.at(hora_prueba).do(run, SANCHEZ_FLORIDA_MIDDAY)
#  schedule.every().day.at(hora_prueba).do(run, SANCHEZ_CONNECTICUT_MIDDAY)
#  schedule.every().day.at(hora_prueba).do(run, SANCHEZ_ILLINOIS_MIDDAY)
#  schedule.every().day.at(hora_prueba).do(run, SANCHEZ_NEW_YORK_MIDDAY)
#
#  #?PREMIOS SANCHEZ PICKS PM --------------------------------------------------------------------------
#  schedule.every().day.at(hora_prueba).do(run, SANCHEZ_MARYLAND_EVENING)
#  schedule.every().day.at(hora_prueba).do(run, SANCHEZ_GEORGIA_EVENING)
#  schedule.every().day.at(hora_prueba).do(run, SANCHEZ_MAINE_EVENING)
#  schedule.every().day.at(hora_prueba).do(run, SANCHEZ_VERMOMT_EVENING )
#  schedule.every().day.at(hora_prueba).do(run, SANCHEZ_NEW_HAMPSHIRE_EVENING )
#  schedule.every().day.at(hora_prueba).do(run, SANCHEZ_CALIFORNIA_EVENING )
#  schedule.every().day.at(hora_prueba).do(run, SANCHEZ_FLORIDA_EVENING)
#  schedule.every().day.at(hora_prueba).do(run, SANCHEZ_ILLINOIS_EVENING)
#  schedule.every().day.at(hora_prueba).do(run, SANCHEZ_NEW_YORK_EVENING)
#  schedule.every().day.at(hora_prueba).do(run, SANCHEZ_NEW_JERSEY_EVENING)
#  schedule.every().day.at(hora_prueba).do(run, SANCHEZ_CONNECTICUT_EVENING)
#  schedule.every().day.at(hora_prueba).do(run, SANCHEZ_GEORGIA_NIGHT)
#
#  #?PREMIOS SANCHEZ DOMINICANAS AM --------------------------------------------------------------------------
#  schedule.every().day.at(hora_prueba).do(run, SANCHEZ_KING_LOTERRY_AM)
#  schedule.every().day.at(hora_prueba).do(run, SANCHEZ_ANGUILA_AM)
#  schedule.every().day.at(hora_prueba).do(run, SANCHEZ_ANGUILA_MD)
#  schedule.every().day.at(hora_prueba).do(run, SANCHEZ_PRIMERA_AM)
#  schedule.every().day.at(hora_prueba).do(run, SANCHEZ_LA_SUERTE_AM)
#  schedule.every().day.at(hora_prueba).do(run, SANCHEZ_REAL)
#  schedule.every().day.at(hora_prueba).do(run, SANCHEZ_LOTEDOM)
#  schedule.every().day.at(hora_prueba).do(run, SANCHEZ_GANAMAS)
#
#  #?PREMIOS SANCHEZ DOMINICANAS PM --------------------------------------------------------------------------
#  schedule.every().day.at(hora_prueba).do(run, SANCHEZ_KING_LOTERRY_PM)
#  schedule.every().day.at(hora_prueba).do(run, SANCHEZ_ANGUILA_TARDE)
#  schedule.every().day.at(hora_prueba).do(run, SANCHEZ_ANGILA_PM)
#  schedule.every().day.at(hora_prueba).do(run, SANCHEZ_PRIMERA_PM)
#  schedule.every().day.at(hora_prueba).do(run, SANCHEZ_NACIONAL)
#  schedule.every().day.at(hora_prueba).do(run, SANCHEZ_LEIDSA)
#  schedule.every().day.at(hora_prueba).do(run, SANCHEZ_LOTEKA)
#
#  #?PREMIOS AMERICANAS AM PERO COMO DOMINICANA SANCHEZ -----------------------------------------------------------------------
#  schedule.every().day.at(hora_prueba).do(run, SANCHEZ_FLORIDA_RD_AM)
#  schedule.every().day.at(hora_prueba).do(run, SANCHEZ_MARYLAND_RD_AM )
#  schedule.every().day.at(hora_prueba).do(run, SANCHEZ_MAINE_RD_AM)
#  schedule.every().day.at(hora_prueba).do(run, SANCHEZ_NEW_HAMPSHIRE_RD_AM)
#  schedule.every().day.at(hora_prueba).do(run, SANCHEZ_VERMONT_RD_AM)
#  schedule.every().day.at(hora_prueba).do(run, SANCHEZ_GEORGIA_RD_AM)
#  schedule.every().day.at(hora_prueba).do(run, SANCHEZ_NEW_JERSEY_RD_AM)
#  schedule.every().day.at(hora_prueba).do(run, SANCHEZ_ILLINOIS_RD_AM)
#  schedule.every().day.at(hora_prueba).do(run, SANCHEZ_CONNECTICUT_RD_AM)
#  schedule.every().day.at(hora_prueba).do(run, SANCHEZ_NEW_YORK_RD_AM)
#
#  ?PREMIOS AMERICANAS PM PERO COMO DOMINICANA SANCHEZ -----------------------------------------------------------------------
#  schedule.every().day.at(hora_prueba).do(run, SANCHEZ_MARYLAND_RD_PM )
#  schedule.every().day.at(hora_prueba).do(run, SANCHEZ_VERMONT_RD_PM)
#  schedule.every().day.at(hora_prueba).do(run, SANCHEZ_NEW_HAMPSHIRE_RD_PM)
#  schedule.every().day.at(hora_prueba).do(run, SANCHEZ_MAINE_RD_PM)
#  schedule.every().day.at(hora_prueba).do(run, SANCHEZ_GEORGIA_RD_PM)
#  schedule.every().day.at(hora_prueba).do(run, SANCHEZ_CALIFORNIA_RD_PM)
#  schedule.every().day.at(hora_prueba).do(run, SANCHEZ_FLORIDA_RD_PM)
#  schedule.every().day.at(hora_prueba).do(run, SANCHEZ_ILLINOIS_RD_PM)
#  schedule.every().day.at(hora_prueba).do(run, SANCHEZ_NEW_YORK_RD_PM)
#  schedule.every().day.at(hora_prueba).do(run, SANCHEZ_NEW_JERSEY_RD_PM)
#  schedule.every().day.at(hora_prueba).do(run, SANCHEZ_CONNECTICUT_RD_PM)
#  schedule.every().day.at(hora_prueba).do(run, SANCHEZ_GEORGIA_RD_NIGHT)
#
#  #?PREMIOS SUPER PALES SANCHEZ ---------------------------------------------------------------------------------------
#  schedule.every().day.at(hora_prueba).do(run, SANCHEZ_SP_REAL_PRIMERA)
#  schedule.every().day.at(hora_prueba).do(run, SANCHEZ_SP_PRIMERA_GANAMAS)
#  schedule.every().day.at(hora_prueba).do(run, SANCHEZ_SP_NYAM_REAL)
#  schedule.every().day.at(hora_prueba).do(run,SANCHEZ_SP_REAl_GANAMAS )
#  schedule.every().day.at(hora_prueba).do(run, SANCHEZ_SP_NYAM_FLAM)
#  schedule.every().day.at(hora_prueba).do(run,SANCHEZ_SP_NYAM_GANAMAS )
#  schedule.every().day.at(hora_prueba).do(run,SANCHEZ_SP_NYAM_LOTEKA )
#  schedule.every().day.at(hora_prueba).do(run,SANCHEZ_SP_GANAMAS_LOTEKA )
#  schedule.every().day.at(hora_prueba).do(run, SANCHEZ_SP_LOTEKA_NACIONAL)
#  schedule.every().day.at(hora_prueba).do(run, SANCHEZ_SP_NACIONAL_LEIDSA)
#  schedule.every().day.at(hora_prueba).do(run, SANCHEZ_SP_NYPM_NACIONAL)
#  schedule.every().day.at(hora_prueba).do(run, SANCHEZ_SP_NYPM_FLPM )

#schedule.every().sunday.at(hora_prueba).do(run, ANGUILA_PM_LOTEDOM)

#!PRUEBAS LOTERIAS NUEVAS DIFERENTES
#schedule.every().day.at(hora_prueba).do(run, LOTERY_MASSACHUSETTS_AM)
#schedule.every().day.at(hora_prueba).do(run, LOTERY_MASSACHUSETTS_PM)


#schedule.every().day.at(hora_prueba).do(run, MASSACHUSETTS_SANCHEZ_AM )



#schedule.every().day.at(hora_prueba).do(run, SANCHEZ_CALIFORNIA_EVENING )

while True:
    fecha_actual = fecha('%d-%m-%Y || %H:%M:%S')
    print(f"|---------- PRUEBAS --> {fecha_actual} <----------|")
    saber = schedule.run_pending()
    if(saber == None):
        pass
    else:
        print(schedule.run_pending())
    time.sleep(TIEMPO_A_BUSCAR)



##? ESTE ARCHIVO ES SOLO PARA PROBAR CODIGO
#loterias =  generate_list( LOTERIAS_DOMINICANA_AM )
#def armar_file( lotteries ):
#    file_data =f"""
#import os
#import schedule
#from Funciones_Especiales import fecha, run
#import time
#from config import TIEMPO_A_BUSCAR, hora_prueba
#from Objectos_para_Automaticos import *
#
#pid = os.getpid()
#print("pid-> ", pid)
#{lotteries}
#
#while True:
#    fecha_actual = fecha('%d-%m-%Y || %H:%M:%S')
#    saber = schedule.run_pending()
#    if(saber == None):
#        pass
#    else:
#        print(schedule.run_pending())
#    time.sleep(TIEMPO_A_BUSCAR)
#    """
#    return file_data
#
#data = armar_file( loterias )
#with open('create_runner.py', 'w') as f:
#   f.write(f'{data}')
#
#os.system('python create_runner.py')
