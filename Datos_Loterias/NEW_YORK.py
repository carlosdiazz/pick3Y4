from DATOS_Loterias_Dominicana.PRIMERA_DIA import FECHA
from Datos_Loterias.PAGINA_USA import *

NY_AM_PAGES     = URL_BASE
NY_AM_PICK3     = 'https://www.lotteryusa.com/new-york/midday-numbers/'
NY_AM_PICK4     = 'https://www.lotteryusa.com/new-york/midday-win-4/'

NY_PM_PAGES     = URL_BASE
NY_PM_PICK3     = 'https://www.lotteryusa.com/new-york/numbers/'
NY_PM_PICK4     = 'https://www.lotteryusa.com/new-york/win-4/'

NEW_YORK_LOTTERYUSA_PAGE_1 = {

    'URL_MIDDAY' : [NY_AM_PAGES, NY_AM_PICK3, NY_AM_PICK4],
    'URL_EVENING' : [NY_PM_PAGES, NY_PM_PICK3, NY_PM_PICK4],

    'PICK3_MIDDAY' : [P3_FECHA,P3_NU1,P3_NU2,P3_NU3 ],
    'PICK4_MIDDAY' : [P4_FECHA,P4_NU1,P4_NU2,P4_NU3,P4_NU4 ],

    'PICK3_EVENING' : [P3_FECHA,P3_NU1,P3_NU2,P3_NU3 ],
    'PICK4_EVENING' : [P4_FECHA,P4_NU1,P4_NU2,P4_NU3,P4_NU4 ]
}
#! OTRA PAGINA

URL         =   'https://nylottery.ny.gov/'
URL_PICK_3  =   'https://nylottery.ny.gov/draw-game?game=numbers'
URL_PICK_4  =   'https://nylottery.ny.gov/draw-game?game=win4'

FECHA       =   '/html/body/div/div[1]/div[4]/main/div/div[1]/div[1]/div[2]/div/div[1]/div[1]/p/span'
NUMERO_1    =   '/html/body/div/div[1]/div[4]/main/div/div[1]/div[1]/div[2]/div/div[1]/div[1]/div/div/div[1]'
NUMERO_2    =   '/html/body/div/div[1]/div[4]/main/div/div[1]/div[1]/div[2]/div/div[1]/div[1]/div/div/div[2]'
NUMERO_3    =   '/html/body/div/div[1]/div[4]/main/div/div[1]/div[1]/div[2]/div/div[1]/div[1]/div/div/div[3]'
NUMERO_4    =   '/html/body/div/div[1]/div[4]/main/div/div[1]/div[1]/div[2]/div/div[1]/div[1]/div/div/div[4]'


NEW_YORK_LOTTERYUSA_PAGE_2 = {

    'URL_MIDDAY' : [URL, URL_PICK_3, URL_PICK_4],
    'URL_EVENING' : [URL, URL_PICK_3, URL_PICK_4],

    'PICK3_MIDDAY' : [FECHA,NUMERO_1,NUMERO_2,NUMERO_3 ],
    'PICK4_MIDDAY' : [FECHA,NUMERO_1,NUMERO_2,NUMERO_3,NUMERO_4 ],

    'PICK3_EVENING' : [FECHA,NUMERO_1,NUMERO_2,NUMERO_3 ],
    'PICK4_EVENING' : [FECHA,NUMERO_1,NUMERO_2,NUMERO_3,NUMERO_4 ]
}


NEW_YORK_TODO = [NEW_YORK_LOTTERYUSA_PAGE_1,NEW_YORK_LOTTERYUSA_PAGE_2 ]