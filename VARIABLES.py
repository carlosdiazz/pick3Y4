#IMPORTACIONES DOMINICANAS
from DATOS_Loterias_Dominicana.ANGUILA_AM import ANGUILA_AM_TODO
from DATOS_Loterias_Dominicana.GANAMAS import GANAMAS_TODO
from DATOS_Loterias_Dominicana.KING_LOTTERY_DIA import KING_LOTTERY_DIA_TODO
from DATOS_Loterias_Dominicana.KING_LOTTERY_NOCHE import KING_LOTTERY_NOCHE_TODO
from DATOS_Loterias_Dominicana.LA_SUERTE import LA_SUERTE_TODO
from DATOS_Loterias_Dominicana.LEIDSA import LEIDSA_TODO
from DATOS_Loterias_Dominicana.LOTEDOM import LOTEDOM_TODO
from DATOS_Loterias_Dominicana.LOTEKA import LOTEKA_TODO
from DATOS_Loterias_Dominicana.NACIONAL import NACIONAL_TODO
from DATOS_Loterias_Dominicana.PRIMERA_DIA import PRIMERA_DIA_TODO
from DATOS_Loterias_Dominicana.PRIMERA_NOCHE import PRIMERA_NOCHE_TODO
from DATOS_Loterias_Dominicana.REAL import REAL_TODO
from DATOS_Loterias_Dominicana.ANGUILA_MD import ANGUILA_MD_TODO
from DATOS_Loterias_Dominicana.ANGUILA_TARDE import ANGUILA_TARDE_TODO
from DATOS_Loterias_Dominicana.ANGUILA_PM import ANGUILA_PM_TODO

#IMPORTACIONES AMERICANAS
from Datos_Loterias.CONNECTICUT import CONNECTICUT_TODO
from Datos_Loterias.FLORIDA import FLORIDA_TODO
from Datos_Loterias.GEORGIA import GEORGIA_TODO
from Datos_Loterias.ILLINOIS import ILLINOIS_TODO
from Datos_Loterias.MAINE import MAINE_TODO
from Datos_Loterias.MARYLAND import MARYLAND_TODO
from Datos_Loterias.NEW_HAMPSHIRE import NEW_HAMPSHIRE_TODO
from Datos_Loterias.NEW_JERSEY import NEW_JERSEY_TODO
from Datos_Loterias.NEW_YORK import NEW_YORK_TODO
from Datos_Loterias.NORTH_CAROLINE import NORTH_CAROLINA_TODO
from Datos_Loterias.PENNSYLVANIA import PENNSYLVANIA_TODO
from Datos_Loterias.SOUTH_CAROLINA import SOUTH_CAROLINA_TODO
from Datos_Loterias.VIRGINIA import VIRGINIA_TODO
from Datos_Loterias.Vermont import VERMONT_TODO
from Datos_Loterias.WASHINGTON_DC import WASHINGTON_DC_TODO

#AQUI AGREGO LAS DIFERENTES LOTERIAS CON SU NOMBRES Y HORARIO PARA BUSCAR Y PREMIAR
#?SI MEZCLADA ES TRUE, MEZCLARA LAS LOTERIAS AMERICANA EN DOMINICANA TAMBIEN
EVENING         =   'EVENING'
MIDDAY          =   'MIDDAY'
MODALIDAD       =   'AMERICANA'  #Esta variable la uso para identificar en varias parte del codigo que esta loteria es Pick3 y Pick4
MODALIDAD_RD    =   'DOMINICANA' #Esta variable la uso para identificar en varias parte del codigo que esta loteria es Dominicana
MODALIDAD_PALE  =   'PALE'       #Esta variable la uso para identificar en varias parte del codigo que esta loteria es un pale
ARREGLO         =   'ARREGLO_XPATH'

#SI pongo mezclada true, es para la loteria americana convertirla en loterias tradicionales dominicanas

#? ----------------------------------------
OBJ_FL_AM = {
    'LOTERIA'       :   'FLORIDA',
    'HORA'          :   '13:30:00',
    "SORTEO"        :   MIDDAY,
    "MODALIDAD"     :   MODALIDAD,
    'MEZCLADA'      :   True,
    'ARREGLO_XPATH' :   FLORIDA_TODO
}

OBJ_FL_PM = {
    'LOTERIA'       :   'FLORIDA',
    'HORA'          :   '21:50:00',
    "SORTEO"        :   EVENING,
    "MODALIDAD"     :   MODALIDAD,
    'MEZCLADA'      :   True,
    'ARREGLO_XPATH' :   FLORIDA_TODO
}

OBJ_FLORIDA_RD_AM = {
    'LOTERIA'       :   'FLORIDA',
    'SORTEO'        :   MIDDAY,
    'HORA'          :   '14:30:00',
    "MODALIDAD"     :   MODALIDAD_RD,
    'MEZCLADA'      :   False
}

OBJ_FLORIDA_RD_PM = {
    'LOTERIA'       :   'FLORIDA',
    'SORTEO'        :   EVENING,
    'HORA'          :   '22:00:00',
    "MODALIDAD"     :   MODALIDAD_RD,
    'MEZCLADA'      :   False
}

#? ----------------------------------------
OBJ_NY_AM = {
    'LOTERIA'       :   'NEW YORK',
    'HORA'          :   '14:35:00',
    "SORTEO"        :   MIDDAY,
    "MODALIDAD"     :   MODALIDAD,
    'MEZCLADA'      :   True,
    'ARREGLO_XPATH' :   NEW_YORK_TODO
}

OBJ_NY_PM = {
    'LOTERIA'       :   'NEW YORK',
    'HORA'          :   '22:30:00',
    "SORTEO"        :   EVENING,
    "MODALIDAD"     :   MODALIDAD,
    'MEZCLADA'      :   True,
    'ARREGLO_XPATH' :   NEW_YORK_TODO
}

OBJ_NEW_YORK_RD_AM = {
    'LOTERIA'       :   'NEW YORK',
    'SORTEO'        :   MIDDAY,
    'HORA'          :   '14:30:00',
    "MODALIDAD"     :   MODALIDAD_RD,
    'MEZCLADA'      :   False
}

OBJ_NEW_YORK_RD_PM = {
    'LOTERIA'       :   'NEW YORK',
    'SORTEO'        :   EVENING,
    'HORA'          :   '22:35:00',
    "MODALIDAD"     :   MODALIDAD_RD,
    'MEZCLADA'      :   False
}

#? ----------------------------------------
OBJ_NJ_AM = {
    'LOTERIA'       :   'NEW JERSEY',
    'HORA'          :   '13:10:00',
    "SORTEO"        :   MIDDAY,
    "MODALIDAD"     :   MODALIDAD,
    'MEZCLADA'      :   True,
    'ARREGLO_XPATH' :   NEW_JERSEY_TODO
}

OBJ_NJ_PM = {
    'LOTERIA'       :   'NEW JERSEY',
    'HORA'          :   '23:00:00',
    "SORTEO"        :   EVENING,
    "MODALIDAD"     :   MODALIDAD,
    'MEZCLADA'      :   True,
    'ARREGLO_XPATH' :   NEW_JERSEY_TODO
}

OBJ_NEW_JERSEY_AM_RD = {
    'LOTERIA'       :   'NEW JERSEY',
    'HORA'          :   '13:10:00',
    "SORTEO"        :   MIDDAY,
    "MODALIDAD"     :   MODALIDAD_RD,
    'MEZCLADA'      :   True,
    'ARREGLO_XPATH' :   NEW_JERSEY_TODO
}

OBJ_NEW_JERSEY_PM_RD = {
    'LOTERIA'       :   'NEW JERSEY',
    'HORA'          :   '23:00:00',
    "SORTEO"        :   EVENING,
    "MODALIDAD"     :   MODALIDAD_RD,
    'MEZCLADA'      :   True,
    'ARREGLO_XPATH' :   NEW_JERSEY_TODO
}

#? ----------------------------------------
OBJ_CT_AM = {
    'LOTERIA'       :   'CONNECTICUT',
    'HORA'          :   '14:00:00',
    "SORTEO"        :   MIDDAY,
    "MODALIDAD"     :   MODALIDAD,
    'MEZCLADA'      :   True,
    'ARREGLO_XPATH' :   CONNECTICUT_TODO
}

OBJ_CT_PM = {
    'LOTERIA'       :   'CONNECTICUT',
    'HORA'          :   '23:00:00',
    "SORTEO"        :   EVENING,
    "MODALIDAD"     :   MODALIDAD,
    'MEZCLADA'      :   True,
    'ARREGLO_XPATH' :   CONNECTICUT_TODO
}

OBJ_CONNECTICUT_AM_RD = {
    'LOTERIA'       :   'CONNECTICUT',
    'HORA'          :   '14:00:00',
    "SORTEO"        :   MIDDAY,
    "MODALIDAD"     :   MODALIDAD_RD,
    'MEZCLADA'      :   True,
    'ARREGLO_XPATH' :   CONNECTICUT_TODO
}

OBJ_CONNECTICUR_PM_RD = {
    'LOTERIA'       :   'CONNECTICUT',
    'HORA'          :   '23:00:00',
    "SORTEO"        :   EVENING,
    "MODALIDAD"     :   MODALIDAD_RD,
    'MEZCLADA'      :   True,
    'ARREGLO_XPATH' :   CONNECTICUT_TODO
}


#? ----------------------------------------
OBJ_VA_AM = {
    'LOTERIA'       :   'VIRGINIA',
    'HORA'          :   '14:00:00',
    "SORTEO"        :   MIDDAY,
    "MODALIDAD"     :   MODALIDAD,
    'MEZCLADA'      :   False,
    'ARREGLO_XPATH' :   VIRGINIA_TODO
}

OBJ_VA_PM = {
    'LOTERIA'       :   'VIRGINIA',
    'HORA'          :   '23:00:00',
    "SORTEO"        :   EVENING,
    "MODALIDAD"     :   MODALIDAD,
    'MEZCLADA'      :   False,
    'ARREGLO_XPATH' :   VIRGINIA_TODO
}
#? ----------------------------------------
OBJ_DC_AM = {
    'LOTERIA'       :   'WASHINGTON D.C',
    'HORA'          :   '14:00:00',
    "SORTEO"        :   MIDDAY,
    "MODALIDAD"     :   MODALIDAD,
    'MEZCLADA'      :   False,
    'ARREGLO_XPATH' :   WASHINGTON_DC_TODO
}

OBJ_DC_PM = {
    'LOTERIA'       :   'WASHINGTON D.C',
    'HORA'          :   '20:00:00',
    "SORTEO"        :   EVENING,
    "MODALIDAD"     :   MODALIDAD,
    'MEZCLADA'      :   False,
    'ARREGLO_XPATH' :   WASHINGTON_DC_TODO
}
#? ----------------------------------------
OBJ_PA_AM = {
    'LOTERIA'       :   'PENNSYLVANIA',
    'HORA'          :   '14:00:00',
    "SORTEO"        :   MIDDAY,
    "MODALIDAD"     :   MODALIDAD,
    'MEZCLADA'      :   False,
    'ARREGLO_XPATH' :   PENNSYLVANIA_TODO
}

OBJ_PA_PM = {
    'LOTERIA'       :   'PENNSYLVANIA',
    'HORA'          :   '19:00:00',
    "SORTEO"        :   EVENING,
    "MODALIDAD"     :   MODALIDAD,
    'MEZCLADA'      :   False,
    'ARREGLO_XPATH' :   PENNSYLVANIA_TODO
}
#? ----------------------------------------
OBJ_NC_AM = {
    'LOTERIA'       :   'NORTH CAROLINA',
    'HORA'          :   '15:00:00',
    "SORTEO"        :   MIDDAY,
    "MODALIDAD"     :   MODALIDAD,
    'MEZCLADA'      :   False,
    'ARREGLO_XPATH' :   NORTH_CAROLINA_TODO
}

OBJ_NC_PM = {
    'LOTERIA'       :   'NORTH CAROLINA',
    'HORA'          :   '23:30:00',
    "SORTEO"        :   EVENING,
    "MODALIDAD"     :   MODALIDAD,
    'MEZCLADA'      :   False,
    'ARREGLO_XPATH' :   NORTH_CAROLINA_TODO
}
#? ----------------------------------------
OBJ_GA_AM = {
    'LOTERIA'       :   'GEORGIA',
    'HORA'          :   '12:50:00',
    "SORTEO"        :   MIDDAY,
    "MODALIDAD"     :   MODALIDAD,
    'MEZCLADA'      :   True,
    'ARREGLO_XPATH' :   GEORGIA_TODO
}

OBJ_GA_PM = {
    'LOTERIA'       :   'GEORGIA',
    'HORA'          :   '19:00:00',
    "SORTEO"        :   EVENING,
    "MODALIDAD"     :   MODALIDAD,
    'MEZCLADA'      :   True,
    'ARREGLO_XPATH' :   GEORGIA_TODO
}
OBJ_GA_NIGHT = {
    'LOTERIA'       :   'GEORGIA',
    'HORA'          :   '23:30:00',
    "SORTEO"        :   'NIGHT',
    "MODALIDAD"     :   MODALIDAD,
    'MEZCLADA'      :   True,
    'ARREGLO_XPATH' :   GEORGIA_TODO
}

OBJ_GEORGIA_RD_AM = {
    'LOTERIA'       :   'GEORGIA',
    'HORA'          :   '12:50:00',
    "SORTEO"        :   MIDDAY,
    "MODALIDAD"     :   MODALIDAD_RD,
    'MEZCLADA'      :   False,
    'ARREGLO_XPATH' :   GEORGIA_TODO
}

OBJ_GEORGIA_RD_PM = {
    'LOTERIA'       :   'GEORGIA',
    'HORA'          :   '19:00:00',
    "SORTEO"        :   EVENING,
    "MODALIDAD"     :   MODALIDAD_RD,
    'MEZCLADA'      :   False,
    'ARREGLO_XPATH' :   GEORGIA_TODO
}
OBJ_GEORGIA_RD_NIGHT = {
    'LOTERIA'       :   'GEORGIA',
    'HORA'          :   '23:30:00',
    "SORTEO"        :   'NIGHT',
    "MODALIDAD"     :   MODALIDAD_RD,
    'MEZCLADA'      :   False,
    'ARREGLO_XPATH' :   GEORGIA_TODO
}

#? ----------------------------------------
OBJ_SC_AM2 = {
    'LOTERIA'       :   'SOUTH CAROLINA',
    'HORA'          :   '13:10:00',
    "SORTEO"        :   MIDDAY,
    "MODALIDAD"     :   MODALIDAD,
    'MEZCLADA'      :   False,
    'ARREGLO_XPATH' :   SOUTH_CAROLINA_TODO
}

OBJ_SC_PM2 = {
    'LOTERIA'       :   'SOUTH CAROLINA',
    'HORA'          :   '19:10:00',
    "SORTEO"        :   EVENING,
    "MODALIDAD"     :   MODALIDAD,
    'MEZCLADA'      :   False,
    'ARREGLO_XPATH' :   SOUTH_CAROLINA_TODO
}
#? ----------------------------------------
OBJ_MD_AM = {
    'LOTERIA'       :   'MARYLAND',
    'HORA'          :   '12:40:00',
    "SORTEO"        :   MIDDAY,
    "MODALIDAD"     :   MODALIDAD,
    'MEZCLADA'      :   True,
    'ARREGLO_XPATH' :   MARYLAND_TODO
}

OBJ_MD_PM = {
    'LOTERIA'       :   'MARYLAND',
    'HORA'          :   '20:10:00',
    "SORTEO"        :   EVENING,
    "MODALIDAD"     :   MODALIDAD,
    'MEZCLADA'      :   True,
    'ARREGLO_XPATH' :   MARYLAND_TODO
}

OBJ_MARYLAND_AM_RD = {
    'LOTERIA'       :   'MARYLAND',
    'HORA'          :   '12:40:00',
    "SORTEO"        :   MIDDAY,
    "MODALIDAD"     :   MODALIDAD_RD,
    'MEZCLADA'      :   True,
    'ARREGLO_XPATH' :   MARYLAND_TODO
}

OBJ_MARYLAND_PM_RD = {
    'LOTERIA'       :   'MARYLAND',
    'HORA'          :   '20:10:00',
    "SORTEO"        :   EVENING,
    "MODALIDAD"     :   MODALIDAD_RD,
    'MEZCLADA'      :   True,
    'ARREGLO_XPATH' :   MARYLAND_TODO
}

#? ----------------------------------------
OBJ_VT_AM = {
    'LOTERIA'       :   'VERMONT',
    'HORA'          :   '13:10:00',
    "SORTEO"        :   MIDDAY,
    "MODALIDAD"     :   MODALIDAD,
    'MEZCLADA'      :   True,
    'ARREGLO_XPATH' :   VERMONT_TODO
}

OBJ_VT_PM = {
    'LOTERIA'       :   'VERMONT',
    'HORA'          :   '19:10:00',
    "SORTEO"        :   EVENING,
    "MODALIDAD"     :   MODALIDAD,
    'MEZCLADA'      :   True,
    'ARREGLO_XPATH' :   VERMONT_TODO
}

OBJ_VERMONT_AM_RD = {
    'LOTERIA'       :   'VERMONT',
    'HORA'          :   '13:10:00',
    "SORTEO"        :   MIDDAY,
    "MODALIDAD"     :   MODALIDAD_RD,
    'MEZCLADA'      :   True,
    'ARREGLO_XPATH' :   VERMONT_TODO
}

OBJ_VERMONT_PM_RD = {
    'LOTERIA'       :   'VERMONT',
    'HORA'          :   '19:10:00',
    "SORTEO"        :   EVENING,
    "MODALIDAD"     :   MODALIDAD_RD,
    'MEZCLADA'      :   True,
    'ARREGLO_XPATH' :   VERMONT_TODO
}


#? ----------------------------------------
OBJ_NH_AM = {
    'LOTERIA'       :   'NEW HAMPSHIRE',
    'HORA'          :   '13:10:00',
    "SORTEO"        :   MIDDAY,
    "MODALIDAD"     :   MODALIDAD,
    'MEZCLADA'      :   True,
    'ARREGLO_XPATH' :   NEW_HAMPSHIRE_TODO
}

OBJ_NH_PM = {
    'LOTERIA'       :   'NEW HAMPSHIRE',
    'HORA'          :   '19:10:00',
    "SORTEO"        :   EVENING,
    "MODALIDAD"     :   MODALIDAD,
    'MEZCLADA'      :   True,
    'ARREGLO_XPATH' :   NEW_HAMPSHIRE_TODO
}

OBJ_NEW_HAMPSHIRE_AM_RD = {
    'LOTERIA'       :   'NEW HAMPSHIRE',
    'HORA'          :   '13:10:00',
    "SORTEO"        :   MIDDAY,
    "MODALIDAD"     :   MODALIDAD_RD,
    'MEZCLADA'      :   True,
    'ARREGLO_XPATH' :   NEW_HAMPSHIRE_TODO
}

OBJ_NEW_HAMPSHIRE_PM_RD = {
    'LOTERIA'       :   'NEW HAMPSHIRE',
    'HORA'          :   '19:10:00',
    "SORTEO"        :   EVENING,
    "MODALIDAD"     :   MODALIDAD_RD,
    'MEZCLADA'      :   True,
    'ARREGLO_XPATH' :   NEW_HAMPSHIRE_TODO
}


#? ----------------------------------------
OBJ_ME_AM = {
    'LOTERIA'       :   'MAINE',
    'HORA'          :   '13:10:00',
    "SORTEO"        :   MIDDAY,
    "MODALIDAD"     :   MODALIDAD,
    'MEZCLADA'      :   True,
    'ARREGLO_XPATH' :   MAINE_TODO
}

OBJ_ME_PM = {
    'LOTERIA'       :   'MAINE',
    'HORA'          :   '19:10:00',
    "SORTEO"        :   EVENING,
    "MODALIDAD"     :   MODALIDAD,
    'MEZCLADA'      :   True,
    'ARREGLO_XPATH' :   MAINE_TODO
}

OBJ_MAINE_AM_RD = {
    'LOTERIA'       :   'MAINE',
    'HORA'          :   '13:10:00',
    "SORTEO"        :   MIDDAY,
    "MODALIDAD"     :   MODALIDAD_RD,
    'MEZCLADA'      :   True,
    'ARREGLO_XPATH' :   MAINE_TODO
}

OBJ_MAINE_PM_RD = {
    'LOTERIA'       :   'MAINE',
    'HORA'          :   '19:10:00',
    "SORTEO"        :   EVENING,
    "MODALIDAD"     :   MODALIDAD_RD,
    'MEZCLADA'      :   True,
    'ARREGLO_XPATH' :   MAINE_TODO
}


#? ----------------------------------------
OBJ_IL_AM = {
    'LOTERIA'       :   'ILLINOIS',
    'HORA'          :   '13:50:00',
    "SORTEO"        :   MIDDAY,
    "MODALIDAD"     :   MODALIDAD,
    'MEZCLADA'      :   True,
    'ARREGLO_XPATH' :   ILLINOIS_TODO
}

OBJ_IL_PM = {
    'LOTERIA'       :   'ILLINOIS',
    'HORA'          :   '21:30:00',
    "SORTEO"        :   EVENING,
    "MODALIDAD"     :   MODALIDAD,
    'MEZCLADA'      :   True,
    'ARREGLO_XPATH' :   ILLINOIS_TODO
}

OBJ_ILLINOIS_AM_RD = {
    'LOTERIA'       :   'ILLINOIS',
    'HORA'          :   '13:50:00',
    "SORTEO"        :   MIDDAY,
    "MODALIDAD"     :   MODALIDAD_RD,
    'MEZCLADA'      :   True,
    'ARREGLO_XPATH' :   ILLINOIS_TODO
}

OBJ_ILLINOIS_PM_RD = {
    'LOTERIA'       :   'ILLINOIS',
    'HORA'          :   '21:30:00',
    "SORTEO"        :   EVENING,
    "MODALIDAD"     :   MODALIDAD_RD,
    'MEZCLADA'      :   True,
    'ARREGLO_XPATH' :   ILLINOIS_TODO
}

#! LOTERIAS DOMINICANA --------------------------------------------------------------------------------
OBJ_GANAMAS = {
    'LOTERIA'       :   'GANAMAS',
    'SORTEO'        :   'GANAMAS',
    'HORA'          :   '14:35:00',
    "MODALIDAD"     :   MODALIDAD_RD,
    'MEZCLADA'      :   False,
    'ARREGLO_XPATH' :   GANAMAS_TODO
}
#? ----------------------------------------
OBJ_KING_AM = {
    'LOTERIA'       :   'KING LOTTERY',
    'SORTEO'        :   'KING LOTTERY DIA',
    'HORA'          :   '12:30:00',
    "MODALIDAD"     :   MODALIDAD_RD,
    'MEZCLADA'      :   False,
    'ARREGLO_XPATH' :   KING_LOTTERY_DIA_TODO
}

OBJ_KING_PM = {
    'LOTERIA'       :   'KING LOTTERY',
    'SORTEO'        :   'KING LOTTERY NOCHE',
    'HORA'          :   '19:30:00',
    "MODALIDAD"     :   MODALIDAD_RD,
    'MEZCLADA'      :   False,
    'ARREGLO_XPATH' :   KING_LOTTERY_NOCHE_TODO
}
#? ----------------------------------------
OBJ_LA_SUERTE = {
    'LOTERIA'       :   'LA SUERTE',
    'SORTEO'        :   'LA SUERTE',
    'HORA'          :   '12:30:00',
    "MODALIDAD"     :   MODALIDAD_RD,
    'MEZCLADA'      :   False,
    'ARREGLO_XPATH' :   LA_SUERTE_TODO
}
#? ----------------------------------------
OBJ_LEIDSA = {
    'LOTERIA'       :   'LEIDSA',
    'SORTEO'        :   'LEIDSA',
    'HORA'          :   '20:55:00',
    "MODALIDAD"     :   MODALIDAD_RD,
    'MEZCLADA'      :   False,
    'ARREGLO_XPATH' :   LEIDSA_TODO
}
#? ----------------------------------------
OBJ_LOTEDOM = {
    'LOTERIA'       :   'LOTEDOM',
    'SORTEO'        :   'LOTEDOM',
    'HORA'          :   '14:00:00',
    "MODALIDAD"     :   MODALIDAD_RD,
    'MEZCLADA'      :   False,
    'ARREGLO_XPATH' :   LOTEDOM_TODO
}
#? ----------------------------------------
OBJ_LOTEKA = {
    'LOTERIA'       :   'LOTEKA',
    'SORTEO'        :   'LOTEKA',
    'HORA'          :   '20:00:00',
    "MODALIDAD"     :   MODALIDAD_RD,
    'MEZCLADA'      :   False,
    'ARREGLO_XPATH' :   LOTEKA_TODO
}
#? ----------------------------------------
OBJ_NACIONAL = {
    'LOTERIA'       :   'NACIONAL',
    'SORTEO'        :   'NACIONAL NOCHE',
    'HORA'          :   '20:55:00',
    "MODALIDAD"     :   MODALIDAD_RD,
    'MEZCLADA'      :   False,
    'ARREGLO_XPATH' :   NACIONAL_TODO
}
#? ----------------------------------------
OBJ_PRIMERA_AM = {
    'LOTERIA'       :   'PRIMERA',
    'SORTEO'        :   'PRIMERA DIA',
    'HORA'          :   '12:00:00',
    "MODALIDAD"     :   MODALIDAD_RD,
    'MEZCLADA'      :   False,
    'ARREGLO_XPATH' :   PRIMERA_DIA_TODO
}

OBJ_PRIMERA_PM = {
    'LOTERIA'       :   'PRIMERA',
    'SORTEO'        :   'PRIMERA NOCHE',
    'HORA'          :   '20:00:00',
    "MODALIDAD"     :   MODALIDAD_RD,
    'MEZCLADA'      :   False,
    'ARREGLO_XPATH' :   PRIMERA_NOCHE_TODO
}
#? ----------------------------------------
OBJ_REAL = {
    'LOTERIA'       :   'REAL',
    'SORTEO'        :   'REAL',
    'HORA'          :   '13:00:00',
    "MODALIDAD"     :   MODALIDAD_RD,
    'MEZCLADA'      :   False,
    'ARREGLO_XPATH' :   REAL_TODO
}
#? ----------------------------------------
OBJ_ANGUILLA_AM = {
    'LOTERIA'       :   'ANGUILLA',
    'SORTEO'        :   'ANGUILLA AM',
    'HORA'          :   '10:00:00',
    "MODALIDAD"     :   MODALIDAD_RD,
    'MEZCLADA'      :   False,
    'ARREGLO_XPATH' :   ANGUILA_AM_TODO
}

OBJ_ANGUILLA_MD = {
    'LOTERIA'       :   'ANGUILLA',
    'SORTEO'        :   'ANGUILLA MEDIO DIA',
    'HORA'          :   '13:00:00',
    "MODALIDAD"     :   MODALIDAD_RD,
    'MEZCLADA'      :   False,
    'ARREGLO_XPATH' :   ANGUILA_MD_TODO
}

OBJ_ANGUILLA_TARDE = {
    'LOTERIA'       :   'ANGUILLA',
    'SORTEO'        :   'ANGUILLA TARDE',
    'HORA'          :   '18:00:00',
    "MODALIDAD"     :   MODALIDAD_RD,
    'MEZCLADA'      :   False,
    'ARREGLO_XPATH' :   ANGUILA_TARDE_TODO
}

OBJ_ANGUILLA_PM = {
    'LOTERIA'       :   'ANGUILLA',
    'SORTEO'        :   'ANGUILLA PM',
    'HORA'          :   '21:00:00',
    "MODALIDAD"     :   MODALIDAD_RD,
    'MEZCLADA'      :   False,
    'ARREGLO_XPATH' :   ANGUILA_PM_TODO
}

OBJ_SP_PRIMERA_GANAMAS = {
    'LOTERIA'       :   'SUPER PALE',
    'SORTEO'        :   'PRIMERA Y GANAMAS',
    'HORA'          :   '14:50:00',
    'MODALIDAD'     :   MODALIDAD_PALE,
    'MEZCLADA'      :   False,
    'ARREGLO_XPATH' :   False
}

OBJ_SP_REAL_PRIMERA = {
    'LOTERIA'       :   'SUPER PALE',
    'SORTEO'        :   'REAL Y PRIMERA',
    'HORA'          :   '13:10:00',
    'MODALIDAD'     :   MODALIDAD_PALE,
    'MEZCLADA'      :   False,
    'ARREGLO_XPATH' :   False
}

OBJ_SP_NYAM_REAL = {
    'LOTERIA'       :   'SUPER PALE',
    'SORTEO'        :   'NEWYORK AM Y REAL',
    'HORA'          :   '14:50:00',
    'MODALIDAD'     :   MODALIDAD_PALE,
    'MEZCLADA'      :   False,
    'ARREGLO_XPATH' :   False
}

OBJ_SP_REAL_GANAMAS = {
    'LOTERIA'       :   'SUPER PALE',
    'SORTEO'        :   'REAL Y GANAMAS',
    'HORA'          :   '14:50:00',
    'MODALIDAD'     :   MODALIDAD_PALE,
    'MEZCLADA'      :   False,
    'ARREGLO_XPATH' :   False
}

OBJ_SP_NYAM_FLAM = {
    'LOTERIA'       :   'SUPER PALE',
    'SORTEO'        :   'NEWYORK AM Y FLORIDA AM',
    'HORA'          :   '14:50:00',
    'MODALIDAD'     :   MODALIDAD_PALE,
    'MEZCLADA'      :   False,
    'ARREGLO_XPATH' :   False
}

OBJ_SP_NYAM_LOTEKA = {
    'LOTERIA'       :   'SUPER PALE',
    'SORTEO'        :   'NEWYORK AM Y LOTEKA',
    'HORA'          :   '20:10:00',
    'MODALIDAD'     :   MODALIDAD_PALE,
    'MEZCLADA'      :   False,
    'ARREGLO_XPATH' :   False
}

OBJ_SP_NYAM_GANAMAS = {
    'LOTERIA'       :   'SUPER PALE',
    'SORTEO'        :   'NEWYORK AM Y GANAMAS',
    'HORA'          :   '14:50:00',
    'MODALIDAD'     :   MODALIDAD_PALE,
    'MEZCLADA'      :   False,
    'ARREGLO_XPATH' :   False
}

OBJ_SP_GANAMAS_LOTEKA = {
    'LOTERIA'       :   'SUPER PALE',
    'SORTEO'        :   'GANAMAS Y LOTEKA',
    'HORA'          :   '20:10:00',
    'MODALIDAD'     :   MODALIDAD_PALE,
    'MEZCLADA'      :   False,
    'ARREGLO_XPATH' :   False
}

OBJ_SP_NACIONAL_LEIDSA = {
    'LOTERIA'       :   'SUPER PALE',
    'SORTEO'        :   'NACIONAL Y LEIDSA',
    'HORA'          :   '21:10:00',
    'MODALIDAD'     :   MODALIDAD_PALE,
    'MEZCLADA'      :   False,
    'ARREGLO_XPATH' :   False
}

OBJ_SP_LOTEKA_NACIONAL = {
    'LOTERIA'       :   'SUPER PALE',
    'SORTEO'        :   'LOTEKA Y NACIONAL',
    'HORA'          :   '21:20:00',
    'MODALIDAD'     :   MODALIDAD_PALE,
    'MEZCLADA'      :   False,
    'ARREGLO_XPATH' :   False
}

OBJ_SP_NYPM_NACIONAL = {
    'LOTERIA'       :   'SUPER PALE',
    'SORTEO'        :   'NEWYORK PM Y NACIONAL',
    'HORA'          :   '22:50:00',
    'MODALIDAD'     :   MODALIDAD_PALE,
    'MEZCLADA'      :   False,
    'ARREGLO_XPATH' :   False
}

OBJ_SP_NYPM_FLPM = {
    'LOTERIA'       :   'SUPER PALE',
    'SORTEO'        :   'NEWYORK PM Y FLORIDA PM',
    'HORA'          :   '22:50:00',
    'MODALIDAD'     :   MODALIDAD_PALE,
    'MEZCLADA'      :   False,
    'ARREGLO_XPATH' :   False
}