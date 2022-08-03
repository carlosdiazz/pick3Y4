from Datos_Loterias.PAGINA_USA import *
#! ---------------------------------------------------------------------------------------------------------------------------------
MD_AM_PAGES = URL_BASE
MD_AM_PICK3 = 'https://www.lotteryusa.com/maryland/midday-pick-3/'
MD_AM_PICK4 = 'https://www.lotteryusa.com/maryland/midday-pick-4/'

MD_PM_PAGES = URL_BASE
MD_PM_PICK3 = 'https://www.lotteryusa.com/maryland/pick-3/'
MD_PM_PICK4 = 'https://www.lotteryusa.com/maryland/pick-4/'

MARYLAND_LOTTERYUSA = {

    'URL_MIDDAY'       : [MD_AM_PAGES,MD_AM_PICK3,MD_AM_PICK4],
    'URL_EVENING'       : [MD_PM_PAGES,MD_PM_PICK3,MD_PM_PICK4],

    "PICK3_MIDDAY"     : [P3_FECHA,P3_NU1,P3_NU2,P3_NU3],
    "PICK4_MIDDAY"     : [P4_FECHA,P4_NU1,P4_NU2,P4_NU3,P4_NU4],

    "PICK3_EVENING"     : [P3_FECHA,P3_NU1,P3_NU2,P3_NU3],
    "PICK4_EVENING"     : [P4_FECHA,P4_NU1,P4_NU2,P4_NU3,P4_NU4]
}

#! ----------------------------------------------------------------------------------------------------------------------------------

MARYLAND_TODO = [MARYLAND_LOTTERYUSA,MARYLAND_LOTTERYUSA ]