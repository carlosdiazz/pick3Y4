from Datos_Loterias.PAGINA_USA import *

#! ---------------------------------------------------------------------------------------------------------------------------------
IL_AM_PAGES = URL_BASE
IL_AM_PICK3 = 'https://www.lotteryusa.com/illinois/midday-3/'
IL_AM_PICK4 = 'https://www.lotteryusa.com/illinois/midday-4/'

IL_PM_PAGES = URL_BASE
IL_PM_PICK3 = 'https://www.lotteryusa.com/illinois/daily-3/'
IL_PM_PICK4 = 'https://www.lotteryusa.com/illinois/daily-4/'

ILLINOIS_LOTTERYUSA = {

    'URL_MIDDAY'       : [IL_AM_PAGES, IL_AM_PICK3, IL_AM_PICK4],
    'URL_EVENING'       : [IL_PM_PAGES, IL_PM_PICK3, IL_PM_PICK4 ],

    "PICK3_MIDDAY"     : [P3_FECHA,P3_NU1,P3_NU2,P3_NU3],
    "PICK4_MIDDAY"     : [P4_FECHA,P4_NU1,P4_NU2,P4_NU3,P4_NU4],

    "PICK3_EVENING"     : [P3_FECHA,P3_NU1,P3_NU2,P3_NU3],
    "PICK4_EVENING"     : [P4_FECHA,P4_NU1,P4_NU2,P4_NU3,P4_NU4]
}

#! ----------------------------------------------------------------------------------------------------------------------------------

ILLINOIS_TODO = [ILLINOIS_LOTTERYUSA, ILLINOIS_LOTTERYUSA ]