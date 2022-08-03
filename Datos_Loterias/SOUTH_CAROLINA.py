from Datos_Loterias.PAGINA_USA import *
#! ---------------------------------------------------------------------------------------------------------------------------------
SC_AM_PAGES = URL_BASE
SC_AM_PICK3 = 'https://www.lotteryusa.com/south-carolina/midday-pick-3/'
SC_AM_PICK4 = 'https://www.lotteryusa.com/south-carolina/midday-pick-4/'

SC_PM_PAGES = URL_BASE
SC_PM_PICK3 = 'https://www.lotteryusa.com/south-carolina/pick-3/'
SC_PM_PICK4 = 'https://www.lotteryusa.com/south-carolina/pick-4/'

SOUTH_CAROLINA_LOTTERYUSA = {

    'URL_MIDDAY'       : [SC_AM_PAGES,SC_AM_PICK3, SC_AM_PICK4],
    'URL_EVENING'       : [SC_PM_PAGES,SC_PM_PICK3,SC_PM_PICK4],

    "PICK3_MIDDAY"     : [P3_FECHA,P3_NU1,P3_NU2,P3_NU3],
    "PICK4_MIDDAY"     : [P4_FECHA,P4_NU1,P4_NU2,P4_NU3,P4_NU4],

    "PICK3_EVENING"     : [P3_FECHA,P3_NU1,P3_NU2,P3_NU3],
    "PICK4_EVENING"     : [P4_FECHA,P4_NU1,P4_NU2,P4_NU3,P4_NU4]
}

#! ----------------------------------------------------------------------------------------------------------------------------------

SOUTH_CAROLINA_TODO = [SOUTH_CAROLINA_LOTTERYUSA,SOUTH_CAROLINA_LOTTERYUSA ]