#IMPORTACIONES DOMINICANAS
from DATOS_Loterias_Dominicana.ANGUILA import ANGUILA
from DATOS_Loterias_Dominicana.GANAMAS import GANAMAS
from DATOS_Loterias_Dominicana.KING_LOTTERY_DIA import KING_LOTTERY_DIA
from DATOS_Loterias_Dominicana.KING_LOTTERY_NOCHE import KING_LOTTERY_NOCHE
from DATOS_Loterias_Dominicana.LA_SUERTE import LA_SUERTE
from DATOS_Loterias_Dominicana.LEIDSA import LEIDSA
from DATOS_Loterias_Dominicana.LOTEDOM import LOTEDOM
from DATOS_Loterias_Dominicana.LOTEKA import LOTEKA
from DATOS_Loterias_Dominicana.NACIONAL import NACIONAL
from DATOS_Loterias_Dominicana.PRIMERA_DIA import PRIMERA_DIA
from DATOS_Loterias_Dominicana.PRIMERA_NOCHE import PRIMERA_NOCHE
from DATOS_Loterias_Dominicana.REAL import REAL
#IMPORTACIONES AMERICANAS
from Datos_Loterias.CONNECTICUT import CONNECTICUT_TODO
from Datos_Loterias.FLORIDA import FLORIDA_TODO
from Datos_Loterias.GEORGIA import GEORGIA_TODO
from Datos_Loterias.MARYLAND import MARYLAND_TODO
from Datos_Loterias.NEW_JERSEY import NEW_JERSEY_TODO
from Datos_Loterias.NEW_YORK import NEW_YORK_TODO
from Datos_Loterias.NORTH_CAROLINE import NORTH_CAROLINA_TODO
from Datos_Loterias.PENNSYLVANIA import PENNSYLVANIA_TODO
from Datos_Loterias.SOUTH_CAROLINA import SOUTH_CAROLINA_TODO
from Datos_Loterias.VIRGINIA import VIRGINIA_TODO
from Datos_Loterias.WASHINGTON_DC import WASHINGTON_DC_TODO


#AQUI AGREGO LAS DIFERENTES LOTERIAS CON SU NOMBRES Y HORARIO PARA BUSCAR Y PREMIAR
#?SI MEZCLADA ES TRUE, MEZCLARA LAS LOTERIAS AMERICANA EN DOMINICANA TAMBIEN
EVENING         =   'EVENING'
MIDDAY          =   'MIDDAY'
MODALIDAD       =   'AMERICANA'  #Esta variable la uso para identificar en varias parte del codigo que esta loteria es Pick3 y Pick4
MODALIDAD_RD    =   'DOMINICANA' #Esta variable la uso para identificar en varias parte del codigo que esta loteria es Dominicana
ARREGLO         =   'ARREGLO_XPATH'

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
#? ----------------------------------------
OBJ_NJ_AM = {
    'LOTERIA'       :   'NEW JERSEY',
    'HORA'          :   '13:10:00',
    "SORTEO"        :   MIDDAY,
    "MODALIDAD"     :   MODALIDAD,
    'MEZCLADA'      :   False,
    'ARREGLO_XPATH' :   NEW_JERSEY_TODO
}

OBJ_NJ_PM = {
    'LOTERIA'       :   'NEW JERSEY',
    'HORA'          :   '23:00:00',
    "SORTEO"        :   EVENING,
    "MODALIDAD"     :   MODALIDAD,
    'MEZCLADA'      :   False,
    'ARREGLO_XPATH' :   NEW_JERSEY_TODO
}
#? ----------------------------------------
OBJ_CT_AM = {
    'LOTERIA'       :   'CONNECTICUT',
    'HORA'          :   '14:00:00',
    "SORTEO"        :   MIDDAY,
    "MODALIDAD"     :   MODALIDAD,
    'MEZCLADA'      :   False,
    'ARREGLO_XPATH' :   CONNECTICUT_TODO
}

OBJ_CT_PM = {
    'LOTERIA'       :   'CONNECTICUT',
    'HORA'          :   '23:00:00',
    "SORTEO"        :   EVENING,
    "MODALIDAD"     :   MODALIDAD,
    'MEZCLADA'      :   False,
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
    'MEZCLADA'      :   False,
    'ARREGLO_XPATH' :   GEORGIA_TODO
}

OBJ_GA_PM = {
    'LOTERIA'       :   'GEORGIA',
    'HORA'          :   '19:00:00',
    "SORTEO"        :   EVENING,
    "MODALIDAD"     :   MODALIDAD,
    'MEZCLADA'      :   False,
    'ARREGLO_XPATH' :   GEORGIA_TODO
}
OBJ_GA_NIGHT = {
    'LOTERIA'       :   'GEORGIA',
    'HORA'          :   '23:30:00',
    "SORTEO"        :   'NIGHT',
    "MODALIDAD"     :   MODALIDAD,
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
    'MEZCLADA'      :   False,
    'ARREGLO_XPATH' :   MARYLAND_TODO
}

OBJ_MD_PM = {
    'LOTERIA'       :   'MARYLAND',
    'HORA'          :   '20:10:00',
    "SORTEO"        :   EVENING,
    "MODALIDAD"     :   MODALIDAD,
    'MEZCLADA'      :   False,
    'ARREGLO_XPATH' :   MARYLAND_TODO
}
#? ----------------------------------------
OBJ_GANAMAS = {
    'LOTERIA'       :   'GANAMAS',
    'SORTEO'        :   'GANAMAS',
    'HORA'          :   '14:35:00',
    "MODALIDAD"     :   MODALIDAD_RD,
    'MEZCLADA'      :   False,
    'ARREGLO_XPATH' :   GANAMAS
}
#? ----------------------------------------
OBJ_KING_AM = {
    'LOTERIA'       :   'KING LOTTERY',
    'SORTEO'        :   'KING LOTTERY DIA',
    'HORA'          :   '12:30:00',
    "MODALIDAD"     :   MODALIDAD_RD,
    'MEZCLADA'      :   False,
    'ARREGLO_XPATH' :   KING_LOTTERY_DIA
}

OBJ_KING_PM = {
    'LOTERIA'       :   'KING LOTTERY',
    'SORTEO'        :   'KING LOTTERY NOCHE',
    'HORA'          :   '19:30:00',
    "MODALIDAD"     :   MODALIDAD_RD,
    'MEZCLADA'      :   False,
    'ARREGLO_XPATH' :   KING_LOTTERY_NOCHE
}
#? ----------------------------------------
OBJ_LA_SUERTE = {
    'LOTERIA'       :   'LA SUERTE',
    'SORTEO'        :   'LA SUERTE',
    'HORA'          :   '12:30:00',
    "MODALIDAD"     :   MODALIDAD_RD,
    'MEZCLADA'      :   False,
    'ARREGLO_XPATH' :   LA_SUERTE
}
#? ----------------------------------------
OBJ_LEIDSA = {
    'LOTERIA'       :   'LEIDSA',
    'SORTEO'        :   'LEIDSA',
    'HORA'          :   '20:55:00',
    "MODALIDAD"     :   MODALIDAD_RD,
    'MEZCLADA'      :   False,
    'ARREGLO_XPATH' :   LEIDSA
}
#? ----------------------------------------
OBJ_LOTEDOM = {
    'LOTERIA'       :   'LOTEDOM',
    'SORTEO'        :   'LOTEDOM',
    'HORA'          :   '14:00:00',
    "MODALIDAD"     :   MODALIDAD_RD,
    'MEZCLADA'      :   False,
    'ARREGLO_XPATH' :   LOTEDOM
}
#? ----------------------------------------
OBJ_LOTEKA = {
    'LOTERIA'       :   'LOTEKA',
    'SORTEO'        :   'LOTEKA',
    'HORA'          :   '20:00:00',
    "MODALIDAD"     :   MODALIDAD_RD,
    'MEZCLADA'      :   False,
    'ARREGLO_XPATH' :   LOTEKA
}
#? ----------------------------------------
OBJ_NACIONAL = {
    'LOTERIA'       :   'NACIONAL',
    'SORTEO'        :   'NACIONAL NOCHE',
    'HORA'          :   '20:55:00',
    "MODALIDAD"     :   MODALIDAD_RD,
    'MEZCLADA'      :   False,
    'ARREGLO_XPATH' :   NACIONAL
}
#? ----------------------------------------
OBJ_PRIMERA_AM = {
    'LOTERIA'       :   'PRIMERA',
    'SORTEO'        :   'PRIMERA DIA',
    'HORA'          :   '12:00:00',
    "MODALIDAD"     :   MODALIDAD_RD,
    'MEZCLADA'      :   False,
    'ARREGLO_XPATH' :   PRIMERA_DIA
}

OBJ_PRIMERA_PM = {
    'LOTERIA'       :   'PRIMERA',
    'SORTEO'        :   'PRIMERA NOCHE',
    'HORA'          :   '20:00:00',
    "MODALIDAD"     :   MODALIDAD_RD,
    'MEZCLADA'      :   False,
    'ARREGLO_XPATH' :   PRIMERA_NOCHE
}
#? ----------------------------------------
OBJ_REAL = {
    'LOTERIA'       :   'REAL',
    'SORTEO'        :   'REAL',
    'HORA'          :   '13:00:00',
    "MODALIDAD"     :   MODALIDAD_RD,
    'MEZCLADA'      :   False,
    'ARREGLO_XPATH' :   REAL
}
#? ----------------------------------------
OBJ_ANGUILLA_AM = {
    'LOTERIA'       :   'ANGUILLA',
    'SORTEO'        :   'ANGUILLA AM',
    'HORA'          :   '10:00:00',
    "MODALIDAD"     :   MODALIDAD_RD,
    'MEZCLADA'      :   False,
    'ARREGLO_XPATH' :   ANGUILA
}

OBJ_ANGUILLA_MD = {
    'LOTERIA'       :   'ANGUILLA',
    'SORTEO'        :   'ANGUILLA MEDIO DIA',
    'HORA'          :   '13:00:00',
    "MODALIDAD"     :   MODALIDAD_RD,
    'MEZCLADA'      :   False,
    'ARREGLO_XPATH' :   ANGUILA
}

OBJ_ANGUILLA_TARDE = {
    'LOTERIA'       :   'ANGUILLA',
    'SORTEO'        :   'ANGUILLA TARDE',
    'HORA'          :   '18:00:00',
    "MODALIDAD"     :   MODALIDAD_RD,
    'MEZCLADA'      :   False,
    'ARREGLO_XPATH' :   ANGUILA
}

OBJ_ANGUILLA_PM = {
    'LOTERIA'       :   'ANGUILLA',
    'SORTEO'        :   'ANGUILLA PM',
    'HORA'          :   '21:00:00',
    "MODALIDAD"     :   MODALIDAD_RD,
    'MEZCLADA'      :   False,
    'ARREGLO_XPATH' :   ANGUILA
}

#! PREMIAR LOTERIA AMERICANA EN PLATAFORMA
OBJ_NEW_YORK_RD_AM = {
    'LOTERIA'       :   'NEW YORK',
    'SORTEO'        :   MIDDAY,
    'HORA'          :   '14:30:00',
    "MODALIDAD"     :   MODALIDAD_RD,
    'MEZCLADA'      :   False
}

OBJ_FLORIDA_RD_AM = {
    'LOTERIA'       :   'FLORIDA',
    'SORTEO'        :   MIDDAY,
    'HORA'          :   '14:30:00',
    "MODALIDAD"     :   MODALIDAD_RD,
    'MEZCLADA'      :   False
}