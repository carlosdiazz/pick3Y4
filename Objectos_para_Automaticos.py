from Buscar_premios import Buscar_Premio
import VARIABLES
from PREMIAR import PREMIAR
from Datos_Loterias.DATOS_PLATAFORMA import PLATAFORMA_LOTEDOM, PLATAFORMA_MEGA, USER_LOTEDOM, USER_MEGALOTTERY, PLATAFORMA_RAPI, USER_RAPIDITA, PLATAFORMA_DEV, USER_DESARROLLO, USER_MEGALOTTERY_SIN_CONFIRMAR

#! BUSCAR PREMIOS DE LOTERIAS
#LOTERIAS AM ----------------------------------------------------------------

LOTERY_FLORIDA_AM               =   Buscar_Premio(VARIABLES.OBJ_FL_AM).Buscar_numeros_ganadores
LOTERY_NEW_YORK_AM              =   Buscar_Premio(VARIABLES.OBJ_NY_AM).Buscar_numeros_ganadores
LOTERY_NEW_JERSEY_AM            =   Buscar_Premio(VARIABLES.OBJ_NJ_AM).Buscar_numeros_ganadores
LOTERY_CONNECTICUT_AM           =   Buscar_Premio(VARIABLES.OBJ_CT_AM).Buscar_numeros_ganadores
LOTERY_VIRGINIA_AM              =   Buscar_Premio(VARIABLES.OBJ_VA_AM).Buscar_numeros_ganadores
LOTERY_WASHINGTON_DC_AM         =   Buscar_Premio(VARIABLES.OBJ_DC_AM).Buscar_numeros_ganadores
LOTERY_PENNSYLVANIA_AM          =   Buscar_Premio(VARIABLES.OBJ_PA_AM).Buscar_numeros_ganadores
LOTERY_SOUTH_CAROLINA_AM        =   Buscar_Premio(VARIABLES.OBJ_SC_AM2).Buscar_numeros_ganadores
LOTERY_NORTH_CAROLINA_AM        =   Buscar_Premio(VARIABLES.OBJ_NC_AM).Buscar_numeros_ganadores
LOTERY_GEORGIA_AM               =   Buscar_Premio(VARIABLES.OBJ_GA_AM).Buscar_numeros_ganadores
LOTERY_MARYLAND_AM              =   Buscar_Premio(VARIABLES.OBJ_MD_AM).Buscar_numeros_ganadores

#LOTERIAS PM -------------------------------------------------------------
LOTERY_FLORIDA_PM               =   Buscar_Premio(VARIABLES.OBJ_FL_PM).Buscar_numeros_ganadores
LOTERY_NEW_YORK_PM              =   Buscar_Premio(VARIABLES.OBJ_NY_PM).Buscar_numeros_ganadores
LOTERY_NEW_JERSEY_PM            =   Buscar_Premio(VARIABLES.OBJ_NJ_PM).Buscar_numeros_ganadores
LOTERY_CONNECTICUT_PM           =   Buscar_Premio(VARIABLES.OBJ_CT_PM).Buscar_numeros_ganadores
LOTERY_VIRGINIA_PM              =   Buscar_Premio(VARIABLES.OBJ_VA_PM).Buscar_numeros_ganadores
LOTERY_WASHINGTON_DC_PM         =   Buscar_Premio(VARIABLES.OBJ_DC_PM).Buscar_numeros_ganadores
LOTERY_PENNSYLVANIA_PM          =   Buscar_Premio(VARIABLES.OBJ_PA_PM).Buscar_numeros_ganadores
LOTERY_SOUTH_CAROLINA_PM        =   Buscar_Premio(VARIABLES.OBJ_SC_PM2).Buscar_numeros_ganadores
LOTERY_NORTH_CAROLINA_PM        =   Buscar_Premio(VARIABLES.OBJ_NC_PM).Buscar_numeros_ganadores
LOTERY_GEORGIA_PM               =   Buscar_Premio(VARIABLES.OBJ_GA_PM).Buscar_numeros_ganadores
LOTERY_GEORGIA_NIGHT            =   Buscar_Premio(VARIABLES.OBJ_GA_NIGHT).Buscar_numeros_ganadores
LOTERY_MARYLAND_PM              =   Buscar_Premio(VARIABLES.OBJ_MD_PM).Buscar_numeros_ganadores

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


#! PREMIAR PLATAFORMAS


#LOTERIAS AM
FLORIDA_MIDDAY                      =   PREMIAR(VARIABLES.OBJ_FL_AM, PLATAFORMA_MEGA, USER_MEGALOTTERY).premiar
MARYLAND_MIDDAY                     =   PREMIAR(VARIABLES.OBJ_MD_AM, PLATAFORMA_MEGA, USER_MEGALOTTERY).premiar
NEW_YORK_MIDDAY                     =   PREMIAR(VARIABLES.OBJ_NY_AM, PLATAFORMA_MEGA, USER_MEGALOTTERY).premiar
VIRGINIA_MIDDAY                     =   PREMIAR(VARIABLES.OBJ_VA_AM, PLATAFORMA_MEGA, USER_MEGALOTTERY).premiar
GEORGIA_MIDDAY                      =   PREMIAR(VARIABLES.OBJ_GA_AM, PLATAFORMA_MEGA, USER_MEGALOTTERY).premiar
NEW_JERSEY_MIDDAY                   =   PREMIAR(VARIABLES.OBJ_NJ_AM, PLATAFORMA_MEGA, USER_MEGALOTTERY).premiar
SOUTH_CAROLINA_MIDDAY               =   PREMIAR(VARIABLES.OBJ_SC_AM2, PLATAFORMA_MEGA, USER_MEGALOTTERY).premiar
PENNSYLVANIA_MIDDAY                 =   PREMIAR(VARIABLES.OBJ_PA_AM, PLATAFORMA_MEGA, USER_MEGALOTTERY).premiar
WASHINGTON_DC_MIDDAY                =   PREMIAR(VARIABLES.OBJ_DC_AM, PLATAFORMA_MEGA, USER_MEGALOTTERY).premiar
CONNECTICUT_MIDDAY                  =   PREMIAR(VARIABLES.OBJ_CT_AM, PLATAFORMA_MEGA, USER_MEGALOTTERY).premiar
NORTH_CAROLINA_MIDDAY               =   PREMIAR(VARIABLES.OBJ_NC_AM, PLATAFORMA_MEGA, USER_MEGALOTTERY).premiar

#LOTERIAS PM
SOUTH_CAROLINA_EVENING              =   PREMIAR(VARIABLES.OBJ_SC_PM2, PLATAFORMA_MEGA, USER_MEGALOTTERY).premiar
GEORGIA_EVENING                     =   PREMIAR(VARIABLES.OBJ_GA_PM, PLATAFORMA_MEGA, USER_MEGALOTTERY).premiar
MARYLAND_EVENING                    =   PREMIAR(VARIABLES.OBJ_MD_PM, PLATAFORMA_MEGA, USER_MEGALOTTERY).premiar
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
PRIMERA_PM_PLATATAFORMA_MEGA        =   PREMIAR(VARIABLES.OBJ_PRIMERA_PM, PLATAFORMA_MEGA, USER_MEGALOTTERY_SIN_CONFIRMAR).premiar
KING_LOTTERY_AM_PLATATAFORMA_MEGA   =   PREMIAR(VARIABLES.KING_LOTTERY_DIA, PLATAFORMA_MEGA, USER_MEGALOTTERY_SIN_CONFIRMAR).premiar
KING_LOTTERY_PM_PLATATAFORMA_MEGA   =   PREMIAR(VARIABLES.KING_LOTTERY_NOCHE, PLATAFORMA_MEGA, USER_MEGALOTTERY_SIN_CONFIRMAR).premiar

#LOTERIAS TRADICIONALES RAPIDITA -------------------------------------------------------------------
PRIMERA_PM_PLATATAFORMA_RAPI        =   PREMIAR(VARIABLES.OBJ_PRIMERA_PM, PLATAFORMA_RAPI, USER_RAPIDITA).premiar

#LOTERIAS TRADICIONALES DESARROLLO -------------------------------------------------------------------
NEW_YORK_AM_PLATAFORMA_DEV          =   PREMIAR(VARIABLES.OBJ_NEW_YORK_RD_AM, PLATAFORMA_DEV, USER_DESARROLLO).premiar
FLORIDA_AM_PLATAFORMA_DEV           =   PREMIAR(VARIABLES.OBJ_FLORIDA_RD_AM, PLATAFORMA_DEV, USER_DESARROLLO).premiar

#LOTERIAS EN LOTEDOM ---------------------------------------------------------------------------------
NEW_YORK_PM_LOTEDOM                 = PREMIAR(VARIABLES.OBJ_NEW_YORK_RD_PM, PLATAFORMA_LOTEDOM, USER_LOTEDOM).premiar
FLORIDA_PM_LOTEDOM                  = PREMIAR(VARIABLES.OBJ_FLORIDA_RD_PM, PLATAFORMA_LOTEDOM, USER_LOTEDOM).premiar