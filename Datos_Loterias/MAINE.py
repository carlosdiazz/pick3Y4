from Datos_Loterias.PAGINA_USA import *

#! ---------------------------------------------------------------------------------------------------------------------------------
ME_AM_PAGES = URL_BASE
ME_AM_PICK3 = 'https://www.lotteryusa.com/maine/midday-3/'
ME_AM_PICK4 = 'https://www.lotteryusa.com/maine/midday-4/'

ME_PM_PAGES = URL_BASE
ME_PM_PICK3 = 'https://www.lotteryusa.com/maine/pick-3/'
ME_PM_PICK4 = 'https://www.lotteryusa.com/maine/pick-4/'

MAINE_LOTTERYUSA = {

    'URL_MIDDAY'       : [ME_AM_PAGES,ME_AM_PICK3,ME_AM_PICK4 ],
    'URL_EVENING'       : [ME_PM_PAGES,ME_PM_PICK3,ME_PM_PICK4  ],

    "PICK3_MIDDAY"     : [P3_FECHA,P3_NU1,P3_NU2,P3_NU3],
    "PICK4_MIDDAY"     : [P4_FECHA,P4_NU1,P4_NU2,P4_NU3,P4_NU4],

    "PICK3_EVENING"     : [P3_FECHA,P3_NU1,P3_NU2,P3_NU3],
    "PICK4_EVENING"     : [P4_FECHA,P4_NU1,P4_NU2,P4_NU3,P4_NU4]
}

#! ----------------------------------------------------------------------------------------------------------------------------------

MAINE_TODO = [MAINE_LOTTERYUSA, MAINE_LOTTERYUSA ]