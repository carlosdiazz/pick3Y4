from Datos_Loterias.PAGINA_USA import *

NY_AM_PAGES     = URL_BASE
NY_AM_PICK3     = 'https://www.lotteryusa.com/new-york/midday-numbers/'
NY_AM_PICK4     = 'https://www.lotteryusa.com/new-york/midday-win-4/'

NY_PM_PAGES     = URL_BASE
NY_PM_PICK3     = 'https://www.lotteryusa.com/new-york/numbers/'
NY_PM_PICK4     = 'https://www.lotteryusa.com/new-york/win-4/'

NEW_YORK_LOTTERYUSA = {

    'URL_MIDDAY' : [NY_AM_PAGES, NY_AM_PICK3, NY_AM_PICK4],
    'URL_EVENING' : [NY_PM_PAGES, NY_PM_PICK3, NY_PM_PICK4],

    'PICK3_MIDDAY' : [P3_FECHA,P3_NU1,P3_NU2,P3_NU3 ],
    'PICK4_MIDDAY' : [P4_FECHA,P4_NU1,P4_NU2,P4_NU3,P4_NU4 ],

    'PICK3_EVENING' : [P3_FECHA,P3_NU1,P3_NU2,P3_NU3 ],
    'PICK4_EVENING' : [P4_FECHA,P4_NU1,P4_NU2,P4_NU3,P4_NU4 ]
}

NEW_YORK_TODO = [NEW_YORK_LOTTERYUSA ]