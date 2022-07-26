#AQUI AGREGO LAS DIFERENTES LOTERIAS CON SU NOMBRES Y HORARIO PARA BUSCAR Y PREMIAR
#?SI MEZCLADA ES TRUE, MEZCLARA LAS LOTERIAS AMERICANA EN DOMINICANA TAMBIEN
EVENING         =   'EVENING'
MIDDAY          =   'MIDDAY'
MODALIDAD       =   'AMERICANA'  #Esta variable la uso para identificar en varias parte del codigo que esta loteria es Pick3 y Pick4
MODALIDAD_RD    =   'DOMINICANA' #Esta variable la uso para identificar en varias parte del codigo que esta loteria es Dominicana

#? ----------------------------------------
OBJ_FL_AM = {
    'LOTERIA'       :   'FLORIDA',
    'HORA'          :   '13:30:00',
    "SORTEO"        :   MIDDAY,
    "MODALIDAD"     :   MODALIDAD,
    'MEZCLADA'      :   True
}

OBJ_FL_PM = {
    'LOTERIA'       :   'FLORIDA',
    'HORA'          :   '21:50:00',
    "SORTEO"        :   EVENING,
    "MODALIDAD"     :   MODALIDAD,
    'MEZCLADA'      :   True
}
#? ----------------------------------------
OBJ_NY_AM = {
    'LOTERIA'       :   'NEW YORK',
    'HORA'          :   '14:30:00',
    "SORTEO"        :   MIDDAY,
    "MODALIDAD"     :   MODALIDAD,
    'MEZCLADA'      :   True
}

OBJ_NY_PM = {
    'LOTERIA'       :   'NEW YORK',
    'HORA'          :   '22:30:00',
    "SORTEO"        :   EVENING,
    "MODALIDAD"     :   MODALIDAD,
    'MEZCLADA'      :   True
}
#? ----------------------------------------
OBJ_NJ_AM = {
    'LOTERIA'       :   'NEW JERSEY',
    'HORA'          :   '13:10:00',
    "SORTEO"        :   MIDDAY,
    "MODALIDAD"     :   MODALIDAD,
    'MEZCLADA'      :   False
}

OBJ_NJ_PM = {
    'LOTERIA'       :   'NEW JERSEY',
    'HORA'          :   '23:00:00',
    "SORTEO"        :   EVENING,
    "MODALIDAD"     :   MODALIDAD,
    'MEZCLADA'      :   False
}
#? ----------------------------------------
OBJ_CT_AM = {
    'LOTERIA'       :   'CONNECTICUT',
    'HORA'          :   '14:00:00',
    "SORTEO"        :   MIDDAY,
    "MODALIDAD"     :   MODALIDAD,
    'MEZCLADA'      :   False
}

OBJ_CT_PM = {
    'LOTERIA'       :   'CONNECTICUT',
    'HORA'          :   '23:00:00',
    "SORTEO"        :   EVENING,
    "MODALIDAD"     :   MODALIDAD,
    'MEZCLADA'      :   False
}
#? ----------------------------------------
OBJ_VA_AM = {
    'LOTERIA'       :   'VIRGINIA',
    'HORA'          :   '14:00:00',
    "SORTEO"        :   MIDDAY,
    "MODALIDAD"     :   MODALIDAD,
    'MEZCLADA'      :   False
}

OBJ_VA_PM = {
    'LOTERIA'       :   'VIRGINIA',
    'HORA'          :   '23:00:00',
    "SORTEO"        :   EVENING,
    "MODALIDAD"     :   MODALIDAD,
    'MEZCLADA'      :   False
}
#? ----------------------------------------
OBJ_DC_AM = {
    'LOTERIA'       :   'WASHINGTON D.C',
    'HORA'          :   '14:00:00',
    "SORTEO"        :   MIDDAY,
    "MODALIDAD"     :   MODALIDAD,
    'MEZCLADA'      :   False
}

OBJ_DC_PM = {
    'LOTERIA'       :   'WASHINGTON D.C',
    'HORA'          :   '20:00:00',
    "SORTEO"        :   EVENING,
    "MODALIDAD"     :   MODALIDAD,
    'MEZCLADA'      :   False
}
#? ----------------------------------------
OBJ_PA_AM = {
    'LOTERIA'       :   'PENNSYLVANIA',
    'HORA'          :   '14:00:00',
    "SORTEO"        :   MIDDAY,
    "MODALIDAD"     :   MODALIDAD,
    'MEZCLADA'      :   False
}

OBJ_PA_PM = {
    'LOTERIA'       :   'PENNSYLVANIA',
    'HORA'          :   '19:00:00',
    "SORTEO"        :   EVENING,
    "MODALIDAD"     :   MODALIDAD,
    'MEZCLADA'      :   False
}
#? ----------------------------------------
OBJ_SC_AM = {
    'LOTERIA'       :   'SOUTH CAROLINA',
    'HORA'          :   '13:00:00',
    "SORTEO"        :   MIDDAY,
    "MODALIDAD"     :   MODALIDAD,
    'MEZCLADA'      :   False
}

OBJ_SC_PM = {
    'LOTERIA'       :   'SOUTH CAROLINA',
    'HORA'          :   '19:00:00',
    "SORTEO"        :   EVENING,
    "MODALIDAD"     :   MODALIDAD,
    'MEZCLADA'      :   False
}
#? ----------------------------------------
OBJ_NC_AM = {
    'LOTERIA'       :   'NORTH CAROLINA',
    'HORA'          :   '15:00:00',
    "SORTEO"        :   MIDDAY,
    "MODALIDAD"     :   MODALIDAD,
    'MEZCLADA'      :   False
}

OBJ_NC_PM = {
    'LOTERIA'       :   'NORTH CAROLINA',
    'HORA'          :   '23:30:00',
    "SORTEO"        :   EVENING,
    "MODALIDAD"     :   MODALIDAD,
    'MEZCLADA'      :   False
}
#? ----------------------------------------
OBJ_GA_AM = {
    'LOTERIA'       :   'GEORGIA',
    'HORA'          :   '12:50:00',
    "SORTEO"        :   MIDDAY,
    "MODALIDAD"     :   MODALIDAD,
    'MEZCLADA'      :   False
}

OBJ_GA_PM = {
    'LOTERIA'       :   'GEORGIA',
    'HORA'          :   '19:00:00',
    "SORTEO"        :   EVENING,
    "MODALIDAD"     :   MODALIDAD,
    'MEZCLADA'      :   False
}
OBJ_GA_NIGHT = {
    'LOTERIA'       :   'GEORGIA',
    'HORA'          :   '23:30:00',
    "SORTEO"        :   'NIGHT',
    "MODALIDAD"     :   MODALIDAD,
    'MEZCLADA'      :   False
}
#? ----------------------------------------
OBJ_GANAMAS = {
    'LOTERIA'       :   'GANAMAS',
    'SORTEO'        :   'GANAMAS',
    'HORA'          :   '14:30:00',
    "MODALIDAD"     :   MODALIDAD_RD,
    'MEZCLADA'      :   False
}
#? ----------------------------------------
OBJ_KING_AM = {
    'LOTERIA'       :   'KING LOTTERY',
    'SORTEO'        :   'KING LOTTERY DIA',
    'HORA'          :   '12:30:00',
    "MODALIDAD"     :   MODALIDAD_RD,
    'MEZCLADA'      :   False
}

OBJ_KING_PM = {
    'LOTERIA'       :   'KING LOTTERY',
    'SORTEO'        :   'KING LOTTERY NOCHE',
    'HORA'          :   '19:30:00',
    "MODALIDAD"     :   MODALIDAD_RD,
    'MEZCLADA'      :   False
}
#? ----------------------------------------
OBJ_LA_SUERTE = {
    'LOTERIA'       :   'LA SUERTE',
    'SORTEO'        :   'LA SUERTE',
    'HORA'          :   '12:30:00',
    "MODALIDAD"     :   MODALIDAD_RD,
    'MEZCLADA'      :   False
}
#? ----------------------------------------
OBJ_LEIDSA = {
    'LOTERIA'       :   'LEIDSA',
    'SORTEO'        :   'LEIDSA',
    'HORA'          :   '20:55:00',
    "MODALIDAD"     :   MODALIDAD_RD,
    'MEZCLADA'      :   False
}
#? ----------------------------------------
OBJ_LOTEDOM = {
    'LOTERIA'       :   'LOTEDOM',
    'SORTEO'        :   'LOTEDOM',
    'HORA'          :   '14:00:00',
    "MODALIDAD"     :   MODALIDAD_RD,
    'MEZCLADA'      :   False
}
#? ----------------------------------------
OBJ_LOTEKA = {
    'LOTERIA'       :   'LOTEKA',
    'SORTEO'        :   'LOTEKA',
    'HORA'          :   '20:00:00',
    "MODALIDAD"     :   MODALIDAD_RD,
    'MEZCLADA'      :   False
}
#? ----------------------------------------
OBJ_NACIONAL = {
    'LOTERIA'       :   'NACIONAL',
    'SORTEO'        :   'NACIONAL NOCHE',
    'HORA'          :   '20:55:00',
    "MODALIDAD"     :   MODALIDAD_RD,
    'MEZCLADA'      :   False
}
#? ----------------------------------------
OBJ_PRIMERA_AM = {
    'LOTERIA'       :   'PRIMERA',
    'SORTEO'        :   'PRIMERA DIA',
    'HORA'          :   '12:00:00',
    "MODALIDAD"     :   MODALIDAD_RD,
    'MEZCLADA'      :   False
}

OBJ_PRIMERA_PM = {
    'LOTERIA'       :   'PRIMERA',
    'SORTEO'        :   'PRIMERA NOCHE',
    'HORA'          :   '20:00:00',
    "MODALIDAD"     :   MODALIDAD_RD,
    'MEZCLADA'      :   False
}
#? ----------------------------------------
OBJ_REAL = {
    'LOTERIA'       :   'REAL',
    'SORTEO'        :   'REAL',
    'HORA'          :   '13:00:00',
    "MODALIDAD"     :   MODALIDAD_RD,
    'MEZCLADA'      :   False
}
#? ----------------------------------------
OBJ_ANGUILLA_AM = {
    'LOTERIA'       :   'ANGUILLA',
    'SORTEO'        :   'ANGUILLA AM',
    'HORA'          :   '10:00:00',
    "MODALIDAD"     :   MODALIDAD_RD,
    'MEZCLADA'      :   False
}

OBJ_ANGUILLA_MD = {
    'LOTERIA'       :   'ANGUILLA',
    'SORTEO'        :   'ANGUILLA MEDIO DIA',
    'HORA'          :   '13:00:00',
    "MODALIDAD"     :   MODALIDAD_RD,
    'MEZCLADA'      :   False
}

OBJ_ANGUILLA_TARDE = {
    'LOTERIA'       :   'ANGUILLA',
    'SORTEO'        :   'ANGUILLA TARDE',
    'HORA'          :   '18:00:00',
    "MODALIDAD"     :   MODALIDAD_RD,
    'MEZCLADA'      :   False
}

OBJ_ANGUILLA_PM = {
    'LOTERIA'       :   'ANGUILLA',
    'SORTEO'        :   'ANGUILLA PM',
    'HORA'          :   '21:00:00',
    "MODALIDAD"     :   MODALIDAD_RD,
    'MEZCLADA'      :   False
}