from Datos_Loterias.PAGINA_USA import *
#! ---------------------------------------------------------------------------------------------------------------------------------
NC_AM_PAGES = URL_BASE
NC_AM_PICK3 = 'https://www.lotteryusa.com/north-carolina/midday-3/'
NC_AM_PICK4 = 'https://www.lotteryusa.com/north-carolina/midday-pick-4/'

NC_PM_PAGES = URL_BASE
NC_PM_PICK3 = 'https://www.lotteryusa.com/north-carolina/pick-3/'
NC_PM_PICK4 = 'https://www.lotteryusa.com/north-carolina/pick-4/'

NORTH_CAROLINA_LOTTERYUSA = {

    'URL_MIDDAY'       : [NC_AM_PAGES,NC_AM_PICK3, NC_AM_PICK4],
    'URL_EVENING'       : [NC_PM_PAGES,NC_PM_PICK3,NC_PM_PICK4],

    "PICK3_MIDDAY"     : [P3_FECHA,P3_NU1,P3_NU2,P3_NU3],
    "PICK4_MIDDAY"     : [P4_FECHA,P4_NU1,P4_NU2,P4_NU3,P4_NU4],

    "PICK3_EVENING"     : [P3_FECHA,P3_NU1,P3_NU2,P3_NU3],
    "PICK4_EVENING"     : [P4_FECHA,P4_NU1,P4_NU2,P4_NU3,P4_NU4],

    "MODALIDAD"         : MODALIDAD_PICK3_4
}

#! ----------------------------------------------------------------------------------------------------------------------------------

NORTH_CAROLINA_TODO = [NORTH_CAROLINA_LOTTERYUSA,NORTH_CAROLINA_LOTTERYUSA ]