from Datos_Loterias.PAGINA_USA import *

#! ---------------------------------------------------------------------------------------------------------------------------------
NH_AM_PAGES = URL_BASE
NH_AM_PICK3 = 'https://www.lotteryusa.com/new-hampshire/midday-3/'
NH_AM_PICK4 = 'https://www.lotteryusa.com/new-hampshire/midday-4/'

NH_PM_PAGES = URL_BASE
NH_PM_PICK3 = 'https://www.lotteryusa.com/new-hampshire/pick-3/'
NH_PM_PICK4 = 'https://www.lotteryusa.com/new-hampshire/pick-4/'

NEW_HAMPSHIRE_LOTTERYUSA = {

    'URL_MIDDAY'       : [NH_AM_PAGES, NH_AM_PICK3, NH_AM_PICK4],
    'URL_EVENING'       : [NH_PM_PAGES,NH_PM_PICK3, NH_PM_PICK4  ],

    "PICK3_MIDDAY"     : [P3_FECHA,P3_NU1,P3_NU2,P3_NU3],
    "PICK4_MIDDAY"     : [P4_FECHA,P4_NU1,P4_NU2,P4_NU3,P4_NU4],

    "PICK3_EVENING"     : [P3_FECHA,P3_NU1,P3_NU2,P3_NU3],
    "PICK4_EVENING"     : [P4_FECHA,P4_NU1,P4_NU2,P4_NU3,P4_NU4],

    "MODALIDAD"         : MODALIDAD_PICK3_4
}

#! ----------------------------------------------------------------------------------------------------------------------------------

NEW_HAMPSHIRE_TODO = [NEW_HAMPSHIRE_LOTTERYUSA, NEW_HAMPSHIRE_LOTTERYUSA ]