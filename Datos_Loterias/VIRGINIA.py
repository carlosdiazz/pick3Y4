from Datos_Loterias.PAGINA_USA import *
#! ---------------------------------------------------------------------------------------------------------------------------------
VA_AM_PAGES = URL_BASE
VA_AM_PICK3 = 'https://www.lotteryusa.com/virginia/midday-3/'
VA_AM_PICK4 = 'https://www.lotteryusa.com/virginia/midday-4/'

VA_PM_PAGES = URL_BASE
VA_PM_PICK3 = 'https://www.lotteryusa.com/virginia/pick-3/'
VA_PM_PICK4 = 'https://www.lotteryusa.com/virginia/pick-4/'

VIRGINIA_LOTTERYUSA = {

    'URL_MIDDAY'       : [VA_AM_PAGES,VA_AM_PICK3,VA_AM_PICK4],
    'URL_EVENING'       : [VA_PM_PAGES,VA_PM_PICK3,VA_PM_PICK4],

    "PICK3_MIDDAY"     : [P3_FECHA,P3_NU1,P3_NU2,P3_NU3],
    "PICK4_MIDDAY"     : [P4_FECHA,P4_NU1,P4_NU2,P4_NU3,P4_NU4],

    "PICK3_EVENING"     : [P3_FECHA,P3_NU1,P3_NU2,P3_NU3],
    "PICK4_EVENING"     : [P4_FECHA,P4_NU1,P4_NU2,P4_NU3,P4_NU4],

    "MODALIDAD"         : MODALIDAD_PICK3_4
}

#! ----------------------------------------------------------------------------------------------------------------------------------

VIRGINIA_TODO = [VIRGINIA_LOTTERYUSA,VIRGINIA_LOTTERYUSA ]