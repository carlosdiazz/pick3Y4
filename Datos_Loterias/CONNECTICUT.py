from Datos_Loterias.PAGINA_USA import *
 #! ---------------------------------------------------------------------------------------------------------------------------------
CT_AM_PAGES = URL_BASE
CT_AM_PICK3 = 'https://www.lotteryusa.com/connecticut/midday-3/'
CT_AM_PICK4 = 'https://www.lotteryusa.com/connecticut/midday-4/'

CT_PM_PAGES = URL_BASE
CT_PM_PICK3 = 'https://www.lotteryusa.com/connecticut/play-3/'
CT_PM_PICK4 = 'https://www.lotteryusa.com/connecticut/play-4/'

CONNECTICUT_LOTTERYUSA = {

    'URL_MIDDAY'       : [CT_AM_PAGES,CT_AM_PICK3,CT_AM_PICK4],
    'URL_EVENING'       : [CT_PM_PAGES,CT_PM_PICK3,CT_PM_PICK4],

    "PICK3_MIDDAY"     : [P3_FECHA,P3_NU1,P3_NU2,P3_NU3],
    "PICK4_MIDDAY"     : [P4_FECHA,P4_NU1,P4_NU2,P4_NU3,P4_NU4],

    "PICK3_EVENING"     : [P3_FECHA,P3_NU1,P3_NU2,P3_NU3],
    "PICK4_EVENING"     : [P4_FECHA,P4_NU1,P4_NU2,P4_NU3,P4_NU4]
}

#! ----------------------------------------------------------------------------------------------------------------------------------

CONNECTICUT_TODO = [CONNECTICUT_LOTTERYUSA ]