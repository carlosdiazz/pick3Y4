from Datos_Loterias.PAGINA_USA import *

#! ---------------------------------------------------------------------------------------------------------------------------------
GA_AM_PAGES = URL_BASE
GA_AM_PICK3 = 'https://www.lotteryusa.com/georgia/midday-3/'
GA_AM_PICK4 = 'https://www.lotteryusa.com/georgia/midday-4/'

GA_PM_PAGES = URL_BASE
GA_PM_PICK3 = 'https://www.lotteryusa.com/georgia/cash-3-evening/'
GA_PM_PICK4 = 'https://www.lotteryusa.com/georgia/cash-4-evening/'

GA_NIGHT_PAGES = URL_BASE
GA_NIGHT_PICK3 = 'https://www.lotteryusa.com/georgia/cash-3/'
GA_NIGHT_PICK4 = 'https://www.lotteryusa.com/georgia/cash-4/'

GEORGIA_LOTTERYUSA = {

    'URL_MIDDAY'        : [GA_AM_PAGES,GA_AM_PICK3,GA_AM_PICK4],
    'URL_EVENING'       : [GA_PM_PAGES,GA_PM_PICK3,GA_PM_PICK4 ],
    'URL_NIGHT'         : [GA_NIGHT_PAGES,GA_NIGHT_PICK3,GA_NIGHT_PICK4],

    "PICK3_MIDDAY"      : [P3_FECHA,P3_NU1,P3_NU2,P3_NU3],
    "PICK4_MIDDAY"      : [P4_FECHA,P4_NU1,P4_NU2,P4_NU3,P4_NU4],

    "PICK3_EVENING"     : [P3_FECHA,P3_NU1,P3_NU2,P3_NU3],
    "PICK4_EVENING"     : [P4_FECHA,P4_NU1,P4_NU2,P4_NU3,P4_NU4],

    "PICK3_NIGHT"       : [P3_FECHA,P3_NU1,P3_NU2,P3_NU3],
    "PICK4_NIGHT"       : [P4_FECHA,P4_NU1,P4_NU2,P4_NU3,P4_NU4]
}

#! ----------------------------------------------------------------------------------------------------------------------------------

GEORGIA_TODO = [GEORGIA_LOTTERYUSA ]