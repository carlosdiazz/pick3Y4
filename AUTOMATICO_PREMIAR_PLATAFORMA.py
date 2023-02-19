# ESTE SCRIPT SE DEJARA EJUCTANDO SIEMPRE QUE ES QUIEN PREMIA EN LA DIFERENTES PLATAFORMAS
import schedule
import VARIABLES
import time
from Funciones_Especiales import run, clearConsole, fecha
from config import TIEMPO_A_BUSCAR
from Objectos_para_Automaticos import *

###! HORARIO DE PREMIAR LOTERIAS
schedule.every().day.at('00:00:00').do(run, clearConsole)

#PREMIAR PICKS AM MEGALOTERY-----------------------------------------------------------
schedule.every().day.at(VARIABLES.OBJ_FL_AM['HORA']).do(run, FLORIDA_MIDDAY)
schedule.every().day.at(VARIABLES.OBJ_NY_AM['HORA']).do(run, NEW_YORK_MIDDAY)
#schedule.every().day.at(VARIABLES.OBJ_VA_AM['HORA']).do(run, VIRGINIA_MIDDAY)
#schedule.every().day.at(VARIABLES.OBJ_GA_AM['HORA']).do(run, GEORGIA_MIDDAY)
#schedule.every().day.at(VARIABLES.OBJ_NJ_AM['HORA']).do(run, NEW_JERSEY_MIDDAY)
#schedule.every().day.at(VARIABLES.OBJ_SC_AM2['HORA']).do(run, SOUTH_CAROLINA_MIDDAY)
schedule.every().day.at(VARIABLES.OBJ_PA_AM['HORA']).do(run, PENNSYLVANIA_MIDDAY)
#schedule.every().day.at(VARIABLES.OBJ_DC_AM['HORA']).do(run, WASHINGTON_DC_MIDDAY)
#schedule.every().day.at(VARIABLES.OBJ_CT_AM['HORA']).do(run, CONNECTICUT_MIDDAY)
#schedule.every().day.at(VARIABLES.OBJ_NC_AM['HORA']).do(run, NORTH_CAROLINA_MIDDAY)
#schedule.every().day.at(VARIABLES.OBJ_MD_AM['HORA']).do(run, MARYLAND_MIDDAY)

#PREMIAR PICKS PM MEGALOTERY-----------------------------------------------------------
#schedule.every().day.at(VARIABLES.OBJ_SC_PM2['HORA']).do(run, SOUTH_CAROLINA_EVENING)
#schedule.every().day.at(VARIABLES.OBJ_GA_PM['HORA']).do(run, GEORGIA_EVENING)
schedule.every().day.at(VARIABLES.OBJ_PA_PM['HORA']).do(run, PENNSYLVANIA_EVENING)
#schedule.every().day.at(VARIABLES.OBJ_DC_PM['HORA']).do(run, WASHINGTON_DC_EVENING)
schedule.every().day.at(VARIABLES.OBJ_FL_PM['HORA']).do(run, FLORIDA_EVENING)
schedule.every().day.at(VARIABLES.OBJ_NY_PM['HORA']).do(run, NEW_YORK_EVENING)
#schedule.every().day.at(VARIABLES.OBJ_CT_PM['HORA']).do(run, CONNECTICUT_EVENING)
#schedule.every().day.at(VARIABLES.OBJ_VA_PM['HORA']).do(run, VIRGINIA_EVENING)
#schedule.every().day.at(VARIABLES.OBJ_NJ_PM['HORA']).do(run, NEW_JERSEY_EVENING)
#schedule.every().day.at(VARIABLES.OBJ_NC_PM['HORA']).do(run, NORTH_CAROLINA_EVENING)
#schedule.every().day.at(VARIABLES.OBJ_GA_NIGHT['HORA']).do(run, GEORGIA_NIGHT)
#schedule.every().day.at(VARIABLES.OBJ_MD_PM['HORA']).do(run, MARYLAND_EVENING)

# LOTERIA DOMINIACANA EN MEGA Y RAPIDITA --------------------------------------------------------------0---
#schedule.every().day.at(VARIABLES.OBJ_PRIMERA_PM['HORA']).do(run, PRIMERA_PM_PLATATAFORMA_MEGA)
#schedule.every().day.at(VARIABLES.OBJ_PRIMERA_PM['HORA']).do(run, PRIMERA_PM_PLATATAFORMA_RAPI)
schedule.every().day.at(VARIABLES.OBJ_KING_AM['HORA']).do(run, KING_LOTTERY_AM_PLATATAFORMA_MEGA)
schedule.every().day.at(VARIABLES.OBJ_KING_PM['HORA']).do(run, KING_LOTTERY_PM_PLATATAFORMA_MEGA)
#schedule.every().day.at(VARIABLES.OBJ_GEORGIA_RD_AM['HORA']).do(run, GEORGIA_AM_PLATAFORMA_MEGA)
#schedule.every().day.at(VARIABLES.OBJ_GEORGIA_RD_PM['HORA']).do(run, GEORGIA_PM_PLATAFORMA_MEGA)
#schedule.every().day.at(VARIABLES.OBJ_GEORGIA_RD_NIGHT['HORA']).do(run, GEORGIA_NIGHT_PLATAFORMA_MEGA)
#schedule.every().day.at(VARIABLES.OBJ_NEW_JERSEY_AM_RD['HORA']).do(run, NEW_JERSEY_AM_PLATAFORMA_MEGA)
#schedule.every().day.at(VARIABLES.OBJ_NEW_JERSEY_PM_RD['HORA']).do(run, NEW_JERSEY_PM_PLATAFORMA_MEGA)

# OTRAS LOTERIA PARA PREMIAR EN LOTEDOM ---------------------------------------------------------
schedule.every().day.at(VARIABLES.OBJ_NEW_YORK_RD_PM['HORA']).do(run, NEW_YORK_PM_LOTEDOM)
schedule.every().day.at(VARIABLES.OBJ_NEW_YORK_RD_PM['HORA']).do(run, NEW_YORK_PM_LOTEDOM_2)

schedule.every().day.at(VARIABLES.OBJ_FLORIDA_RD_PM['HORA']).do(run, FLORIDA_PM_LOTEDOM)
schedule.every().day.at(VARIABLES.OBJ_FLORIDA_RD_PM['HORA']).do(run, FLORIDA_PM_LOTEDOM_2)

schedule.every().sunday.at(VARIABLES.OBJ_LOTEKA['HORA']).do(run, LOTEKA_PM_LOTEDOM)
schedule.every().sunday.at(VARIABLES.OBJ_PRIMERA_PM['HORA']).do(run, PRIMERA_PM_LOTEDOM)
#schedule.every().sunday.at(VARIABLES.OBJ_ANGUILLA_PM['HORA']).do(run, ANGUILA_PM_LOTEDOM)

#PREMIOS SANCHEZ PICKS AM --------------------------------------------------------------------------
#schedule.every().day.at(VARIABLES.OBJ_MD_AM['HORA']).do(run, SANCHEZ_MARYLAND_MIDDAY)
#schedule.every().day.at(VARIABLES.OBJ_NH_AM['HORA']).do(run, SANCHEZ_NEW_HAMPSHIRE_MIDDAY)
#schedule.every().day.at(VARIABLES.OBJ_ME_AM['HORA']).do(run, SANCHEZ_MAINE_MIDDAY )
#schedule.every().day.at(VARIABLES.OBJ_VT_AM['HORA']).do(run, SANCHEZ_VERMOMT_MIDDAY )
#schedule.every().day.at(VARIABLES.OBJ_GA_AM['HORA']).do(run, SANCHEZ_GEORGIA_MIDDAY)
#schedule.every().day.at(VARIABLES.OBJ_NJ_AM['HORA']).do(run, SANCHEZ_NEW_JERSEY_MIDDAY)
#schedule.every().day.at(VARIABLES.OBJ_FL_AM['HORA']).do(run, SANCHEZ_FLORIDA_MIDDAY)
#schedule.every().day.at(VARIABLES.OBJ_CT_AM['HORA']).do(run, SANCHEZ_CONNECTICUT_MIDDAY)
#schedule.every().day.at(VARIABLES.OBJ_IL_AM['HORA']).do(run, SANCHEZ_ILLINOIS_MIDDAY)
#schedule.every().day.at(VARIABLES.OBJ_NY_AM['HORA']).do(run, SANCHEZ_NEW_YORK_MIDDAY)

#PREMIOS SANCHEZ PICKS PM --------------------------------------------------------------------------
#schedule.every().day.at(VARIABLES.OBJ_MD_PM['HORA']).do(run, SANCHEZ_MARYLAND_EVENING)
#schedule.every().day.at(VARIABLES.OBJ_GA_PM['HORA']).do(run, SANCHEZ_GEORGIA_EVENING)
#schedule.every().day.at(VARIABLES.OBJ_ME_PM['HORA']).do(run, SANCHEZ_MAINE_EVENING)
#schedule.every().day.at(VARIABLES.OBJ_VT_PM['HORA']).do(run, SANCHEZ_VERMOMT_EVENING )
#schedule.every().day.at(VARIABLES.OBJ_NH_PM['HORA']).do(run, SANCHEZ_NEW_HAMPSHIRE_EVENING )
##!schedule.every().day.at(VARIABLES.OBJ_CA_PM['HORA']).do(run, SANCHEZ_CALIFORNIA_EVENING )
#schedule.every().day.at(VARIABLES.OBJ_FL_PM['HORA']).do(run, SANCHEZ_FLORIDA_EVENING)
#schedule.every().day.at(VARIABLES.OBJ_IL_PM['HORA']).do(run, SANCHEZ_ILLINOIS_EVENING)
#schedule.every().day.at(VARIABLES.OBJ_NY_PM['HORA']).do(run, SANCHEZ_NEW_YORK_EVENING)
#schedule.every().day.at(VARIABLES.OBJ_GA_NIGHT['HORA']).do(run, SANCHEZ_GEORGIA_NIGHT)
#schedule.every().day.at(VARIABLES.OBJ_NJ_PM['HORA']).do(run, SANCHEZ_NEW_JERSEY_EVENING)
#schedule.every().day.at(VARIABLES.OBJ_CT_PM['HORA']).do(run, SANCHEZ_CONNECTICUT_EVENING)

#PREMIOS SANCHEZ DOMINICANAS AM --------------------------------------------------------------------------
#schedule.every().day.at(VARIABLES.OBJ_KING_AM['HORA']).do(run, SANCHEZ_KING_LOTERRY_AM)
##schedule.every().day.at(VARIABLES.OBJ_ANGUILLA_AM['HORA']).do(run, SANCHEZ_ANGUILA_AM)
##schedule.every().day.at(VARIABLES.OBJ_ANGUILLA_MD['HORA']).do(run, SANCHEZ_ANGUILA_MD)
#schedule.every().day.at(VARIABLES.OBJ_PRIMERA_AM['HORA']).do(run, SANCHEZ_PRIMERA_AM)
#schedule.every().day.at(VARIABLES.OBJ_LA_SUERTE['HORA']).do(run, SANCHEZ_LA_SUERTE_AM)
#schedule.every().day.at(VARIABLES.OBJ_REAL['HORA']).do(run, SANCHEZ_REAL)
#schedule.every().day.at(VARIABLES.OBJ_LOTEDOM['HORA']).do(run, SANCHEZ_LOTEDOM)
#schedule.every().day.at(VARIABLES.OBJ_GANAMAS['HORA']).do(run, SANCHEZ_GANAMAS)
#
##PREMIOS SANCHEZ DOMINICANAS PM --------------------------------------------------------------------------
#schedule.every().day.at(VARIABLES.OBJ_KING_PM['HORA']).do(run, SANCHEZ_KING_LOTERRY_PM)
##schedule.every().day.at(VARIABLES.OBJ_ANGUILLA_TARDE['HORA']).do(run, SANCHEZ_ANGUILA_TARDE)
##schedule.every().day.at(VARIABLES.OBJ_ANGUILLA_PM['HORA']).do(run, SANCHEZ_ANGILA_PM)
#schedule.every().day.at(VARIABLES.OBJ_PRIMERA_PM['HORA']).do(run, SANCHEZ_PRIMERA_PM)
#schedule.every().day.at(VARIABLES.OBJ_NACIONAL['HORA']).do(run, SANCHEZ_NACIONAL)
#schedule.every().day.at(VARIABLES.OBJ_LEIDSA['HORA']).do(run, SANCHEZ_LEIDSA)
#schedule.every().day.at(VARIABLES.OBJ_LOTEKA['HORA']).do(run, SANCHEZ_LOTEKA)
#schedule.every().sunday.at("15:55:00").do(run, SANCHEZ_LEIDSA)
#schedule.every().sunday.at("18:05:00").do(run, SANCHEZ_NACIONAL)
#
#
##PREMIOS AMERICANAS AM PERO COMO DOMINICANA SANCHEZ -----------------------------------------------------------------------
# schedule.every().day.at(VARIABLES.OBJ_FLORIDA_RD_AM['HORA']).do(run, SANCHEZ_FLORIDA_RD_AM)
#schedule.every().day.at(VARIABLES.OBJ_MARYLAND_AM_RD['HORA']).do(run, SANCHEZ_MARYLAND_RD_AM )
#schedule.every().day.at(VARIABLES.OBJ_MAINE_AM_RD['HORA']).do(run, SANCHEZ_MAINE_RD_AM)
#schedule.every().day.at(VARIABLES.OBJ_NEW_HAMPSHIRE_AM_RD['HORA']).do(run, SANCHEZ_NEW_HAMPSHIRE_RD_AM)
#schedule.every().day.at(VARIABLES.OBJ_VERMONT_AM_RD['HORA']).do(run, SANCHEZ_VERMONT_RD_AM)
#schedule.every().day.at(VARIABLES.OBJ_GEORGIA_RD_AM['HORA']).do(run, SANCHEZ_GEORGIA_RD_AM)
#schedule.every().day.at(VARIABLES.OBJ_NEW_JERSEY_AM_RD['HORA']).do(run, SANCHEZ_NEW_JERSEY_RD_AM)
#schedule.every().day.at(VARIABLES.OBJ_ILLINOIS_AM_RD['HORA']).do(run, SANCHEZ_ILLINOIS_RD_AM)
#schedule.every().day.at(VARIABLES.OBJ_CONNECTICUT_AM_RD['HORA']).do(run, SANCHEZ_CONNECTICUT_RD_AM)
#schedule.every().day.at(VARIABLES.OBJ_NEW_YORK_RD_AM['HORA']).do(run, SANCHEZ_NEW_YORK_RD_AM)
#
##PREMIOS AMERICANAS PM PERO COMO DOMINICANA SANCHEZ -----------------------------------------------------------------------
#schedule.every().day.at(VARIABLES.OBJ_MARYLAND_PM_RD['HORA']).do(run, SANCHEZ_MARYLAND_RD_PM )
#schedule.every().day.at(VARIABLES.OBJ_VERMONT_PM_RD['HORA']).do(run, SANCHEZ_VERMONT_RD_PM)
#schedule.every().day.at(VARIABLES.OBJ_NEW_HAMPSHIRE_PM_RD['HORA']).do(run, SANCHEZ_NEW_HAMPSHIRE_RD_PM)
#schedule.every().day.at(VARIABLES.OBJ_MAINE_PM_RD['HORA']).do(run, SANCHEZ_MAINE_RD_PM)
#schedule.every().day.at(VARIABLES.OBJ_GEORGIA_RD_PM['HORA']).do(run, SANCHEZ_GEORGIA_RD_PM)
#schedule.every().day.at(VARIABLES.OBJ_CALIFORNIA_RD_PM['HORA']).do(run, SANCHEZ_CALIFORNIA_RD_PM)
#schedule.every().day.at(VARIABLES.OBJ_FLORIDA_RD_PM['HORA']).do(run, SANCHEZ_FLORIDA_RD_PM)
#schedule.every().day.at(VARIABLES.OBJ_ILLINOIS_PM_RD['HORA']).do(run, SANCHEZ_ILLINOIS_RD_PM)
#schedule.every().day.at(VARIABLES.OBJ_NEW_YORK_RD_PM['HORA']).do(run, SANCHEZ_NEW_YORK_RD_PM)
#schedule.every().day.at(VARIABLES.OBJ_NEW_JERSEY_PM_RD['HORA']).do(run, SANCHEZ_NEW_JERSEY_RD_PM)
#schedule.every().day.at(VARIABLES.OBJ_CONNECTICUT_PM_RD['HORA']).do(run, SANCHEZ_CONNECTICUT_RD_PM)
#schedule.every().day.at(VARIABLES.OBJ_GEORGIA_RD_NIGHT['HORA']).do(run, SANCHEZ_GEORGIA_RD_NIGHT)
#
##PREMIOS SUPER PALES SANCHEZ ---------------------------------------------------------------------------------------
#schedule.every().day.at(VARIABLES.OBJ_SP_REAL_PRIMERA['HORA']).do(run, SANCHEZ_SP_REAL_PRIMERA)
#schedule.every().day.at(VARIABLES.OBJ_SP_PRIMERA_GANAMAS['HORA']).do(run, SANCHEZ_SP_PRIMERA_GANAMAS)
#schedule.every().day.at(VARIABLES.OBJ_SP_NYAM_REAL['HORA']).do(run, SANCHEZ_SP_NYAM_REAL)
#schedule.every().day.at(VARIABLES.OBJ_SP_REAL_GANAMAS['HORA']).do(run,SANCHEZ_SP_REAl_GANAMAS )
#schedule.every().day.at(VARIABLES.OBJ_SP_NYAM_FLAM['HORA']).do(run, SANCHEZ_SP_NYAM_FLAM)
#schedule.every().day.at(VARIABLES.OBJ_SP_NYAM_GANAMAS['HORA']).do(run,SANCHEZ_SP_NYAM_GANAMAS )
#schedule.every().day.at(VARIABLES.OBJ_SP_NYAM_LOTEKA['HORA']).do(run,SANCHEZ_SP_NYAM_LOTEKA )
#schedule.every().day.at(VARIABLES.OBJ_SP_GANAMAS_LOTEKA['HORA']).do(run,SANCHEZ_SP_GANAMAS_LOTEKA )
#schedule.every().day.at(VARIABLES.OBJ_SP_LOTEKA_NACIONAL['HORA']).do(run, SANCHEZ_SP_LOTEKA_NACIONAL)
#schedule.every().day.at(VARIABLES.OBJ_SP_NACIONAL_LEIDSA['HORA']).do(run, SANCHEZ_SP_NACIONAL_LEIDSA)
#schedule.every().day.at(VARIABLES.OBJ_SP_NYPM_NACIONAL['HORA']).do(run, SANCHEZ_SP_NYPM_NACIONAL)
#schedule.every().day.at(VARIABLES.OBJ_SP_NYPM_FLPM['HORA']).do(run, SANCHEZ_SP_NYPM_FLPM )
#
##! LOTERIAS RARAS
#schedule.every().day.at(VARIABLES.OBJ_MA_AM_RD['HORA']).do(run, MASSACHUSETTS_SANCHEZ_AM )
#schedule.every().day.at(VARIABLES.OBJ_MA_PM_RD['HORA']).do(run, MASSACHUSETTS_SANCHEZ_PM )
#schedule.every().day.at(VARIABLES.OBJ_CA_PM['HORA']).do(run, SANCHEZ_CALIFORNIA_EVENING )

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