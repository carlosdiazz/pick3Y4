from Datos_Loterias.PAGINA_USA import *

#! ---------------------------------------------------------------------------------------------------------------------------------
_AM_PAGES = URL_BASE
_AM_PICK3 = ''
_AM_PICK4 = ''

_PM_PAGES = URL_BASE
_PM_PICK3 = ''
_PM_PICK4 = ''

_LOTTERYUSA = {

    'URL_MIDDAY'       : [],
    'URL_EVENING'       : [],

    "PICK3_MIDDAY"     : [P3_FECHA,P3_NU1,P3_NU2,P3_NU3],
    "PICK4_MIDDAY"     : [P4_FECHA,P4_NU1,P4_NU2,P4_NU3,P4_NU4],

    "PICK3_EVENING"     : [P3_FECHA,P3_NU1,P3_NU2,P3_NU3],
    "PICK4_EVENING"     : [P4_FECHA,P4_NU1,P4_NU2,P4_NU3,P4_NU4],

    "MODALIDAD"         : MODALIDAD_PICK3_4
}

#! ----------------------------------------------------------------------------------------------------------------------------------

_TODO = [_LOTTERYUSA ]