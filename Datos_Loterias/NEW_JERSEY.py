from Datos_Loterias.PAGINA_USA import *

NJ_AM_PAGES     = URL_BASE
NJ_AM_PICK3     = 'https://www.lotteryusa.com/new-jersey/midday-pick-3/'
NJ_AM_PICK4     = 'https://www.lotteryusa.com/new-jersey/midday-pick-4/'

NJ_PM_PAGES     = URL_BASE
NJ_PM_PICK3     = 'https://www.lotteryusa.com/new-jersey/pick-3/'
NJ_PM_PICK4     = 'https://www.lotteryusa.com/new-jersey/pick-4/'

NEW_JERSEY_LOTTERYUSA = {

    'URL_MIDDAY' : [NJ_AM_PAGES, NJ_AM_PICK3, NJ_AM_PICK4],
    'PICK3_MIDDAY' : [P3_FECHA,P3_NU1,P3_NU2,P3_NU3 ],
    'PICK4_MIDDAY' : [P4_FECHA,P4_NU1,P4_NU2,P4_NU3,P4_NU4 ],

    'URL_EVENING' : [NJ_PM_PAGES, NJ_PM_PICK3, NJ_PM_PICK4],
    'PICK3_EVENING' : [P3_FECHA,P3_NU1,P3_NU2,P3_NU3 ],
    'PICK4_EVENING' : [P4_FECHA,P4_NU1,P4_NU2,P4_NU3,P4_NU4 ]
}

NEW_JERSEY_TODO = [NEW_JERSEY_LOTTERYUSA,NEW_JERSEY_LOTTERYUSA ]