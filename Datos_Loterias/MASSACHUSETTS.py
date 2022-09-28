
#!NO TOMAR ESTO COMO REFERENCIA YA QUE EL MODELU DE JUEGO EN ESTA LOTERIA ES DIFERENTE

from Datos_Loterias.PAGINA_USA import *

#! ---------------------------------------------------------------------------------------------------------------------------------
MASSACHUSETTS_AM_PAGES = URL_BASE
MASSACHUSETTS_AM_PICK3 = 'https://www.lotteryusa.com/massachusetts/midday-numbers/'
MASSACHUSETTS_AM_PICK4 = 'https://www.lotteryusa.com/massachusetts/midday-numbers/'
MASSACHUSETTS_AM_PICK2 = 'https://www.lotteryusa.com/massachusetts/midday-numbers/'

MASSACHUSETTS_PM_PAGES = URL_BASE
MASSACHUSETTS_PM_PICK2 = 'https://www.lotteryusa.com/massachusetts/numbers/'
MASSACHUSETTS_PM_PICK3 = 'https://www.lotteryusa.com/massachusetts/numbers/'
MASSACHUSETTS_PM_PICK4 = 'https://www.lotteryusa.com/massachusetts/numbers/'

MASSACHUSETTS_LOTTERYUSA = {

    'URL_MIDDAY'       : [MASSACHUSETTS_AM_PAGES,MASSACHUSETTS_AM_PICK3,MASSACHUSETTS_AM_PICK4, MASSACHUSETTS_AM_PICK2],
    'URL_EVENING'       : [MASSACHUSETTS_PM_PAGES,MASSACHUSETTS_PM_PICK3,MASSACHUSETTS_PM_PICK4, MASSACHUSETTS_PM_PICK2],

    "PICK2_MIDDAY"     : [P4_FECHA,P4_NU3,P4_NU4],
    "PICK3_MIDDAY"     : [P3_FECHA,P3_NU1,P3_NU2,P3_NU3],
    "PICK4_MIDDAY"     : [P4_FECHA,P4_NU1,P4_NU2,P4_NU3,P4_NU4],

    "PICK2_EVENING"     : [P4_FECHA,P4_NU3,P4_NU4],
    "PICK3_EVENING"     : [P3_FECHA,P3_NU1,P3_NU2,P3_NU3],
    "PICK4_EVENING"     : [P4_FECHA,P4_NU1,P4_NU2,P4_NU3,P4_NU4],

    "MODALIDAD"         : MODALIDAD_PICK2_3_4
}

#! ----------------------------------------------------------------------------------------------------------------------------------

MASSACHUSETTS_TODO = [MASSACHUSETTS_LOTTERYUSA, MASSACHUSETTS_LOTTERYUSA ]