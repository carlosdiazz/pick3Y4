from Datos_Loterias.PAGINA_USA import *

#! ---------------------------------------------------------------------------------------------------------------------------------
VT_AM_PAGES = URL_BASE
VT_AM_PICK3 = 'https://www.lotteryusa.com/vermont/midday-3/'
VT_AM_PICK4 = 'https://www.lotteryusa.com/vermont/midday-4/'

VT_PM_PAGES = URL_BASE
VT_PM_PICK3 = 'https://www.lotteryusa.com/vermont/pick-3/'
VT_PM_PICK4 = 'https://www.lotteryusa.com/vermont/pick-4/'

VERMONT_LOTTERYUSA = {

    'URL_MIDDAY'       : [VT_AM_PAGES, VT_AM_PICK3, VT_AM_PICK4],
    'URL_EVENING'       : [VT_PM_PAGES, VT_PM_PICK3, VT_PM_PICK4],

    "PICK3_MIDDAY"     : [P3_FECHA,P3_NU1,P3_NU2,P3_NU3],
    "PICK4_MIDDAY"     : [P4_FECHA,P4_NU1,P4_NU2,P4_NU3,P4_NU4],

    "PICK3_EVENING"     : [P3_FECHA,P3_NU1,P3_NU2,P3_NU3],
    "PICK4_EVENING"     : [P4_FECHA,P4_NU1,P4_NU2,P4_NU3,P4_NU4],

    "MODALIDAD"         : MODALIDAD_PICK3_4
}

#! ----------------------------------------------------------------------------------------------------------------------------------

VERMONT_TODO = [VERMONT_LOTTERYUSA, VERMONT_LOTTERYUSA ]