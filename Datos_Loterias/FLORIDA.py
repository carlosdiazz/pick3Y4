from Datos_Loterias.PAGINA_USA import *
#! ---------------------------------------------------------------------------------------------------------------------------------
FL_AM_PAGES = URL_BASE
FL_AM_PICK3 = 'https://www.lotteryusa.com/florida/midday-pick-3/'
FL_AM_PICK4 = 'https://www.lotteryusa.com/florida/midday-pick-4/'

FL_PM_PAGES = URL_BASE
FL_PM_PICK3 = 'https://www.lotteryusa.com/florida/pick-3/'
FL_PM_PICK4 = 'https://www.lotteryusa.com/florida/pick-4/'

FLORIDA_LOTTERYUSA = {

    'URL_MIDDAY'       : [FL_AM_PAGES,FL_AM_PICK3,FL_AM_PICK4],
    'URL_EVENING'       : [FL_PM_PAGES,FL_PM_PICK3,FL_PM_PICK4],

    "PICK3_MIDDAY"     : [P3_FECHA,P3_NU1,P3_NU2,P3_NU3],
    "PICK4_MIDDAY"     : [P4_FECHA,P4_NU1,P4_NU2,P4_NU3,P4_NU4 ],

    "PICK3_EVENING"     : [P3_FECHA,P3_NU1,P3_NU2,P3_NU3],
    "PICK4_EVENING"     : [P4_FECHA,P4_NU1,P4_NU2,P4_NU3,P4_NU4 ]
}

#! ----------------------------------------------------------------------------------------------------------------------------------

FLORIDA_TODO = [FLORIDA_LOTTERYUSA ]