from Datos_Loterias.PAGINA_USA import *
#! ---------------------------------------------------------------------------------------------------------------------------------
FL_AM_PAGES = URL_BASE
FL_AM_PICK2 = 'https://www.lotteryusa.com/florida/pick-2-midday/'
FL_AM_PICK3 = 'https://www.lotteryusa.com/florida/midday-pick-3/'
FL_AM_PICK4 = 'https://www.lotteryusa.com/florida/midday-pick-4/'

FL_PM_PAGES = URL_BASE
FL_PM_PICK2 = 'https://www.lotteryusa.com/florida/pick-2/'
FL_PM_PICK3 = 'https://www.lotteryusa.com/florida/pick-3/'
FL_PM_PICK4 = 'https://www.lotteryusa.com/florida/pick-4/'


#! SI LLEVA PICK2 el link se coloca al final
FLORIDA_LOTTERYUSA = {

    'URL_MIDDAY'       : [FL_AM_PAGES,FL_AM_PICK3,FL_AM_PICK4,FL_AM_PICK2],
    'URL_EVENING'       : [FL_PM_PAGES,FL_PM_PICK3,FL_PM_PICK4, FL_PM_PICK2],

    "PICK2_MIDDAY"      : [P3_FECHA,P3_NU1,P3_NU2],
    "PICK3_MIDDAY"     : [P3_FECHA,P3_NU1,P3_NU2,P3_NU3],
    "PICK4_MIDDAY"     : [P4_FECHA,P4_NU1,P4_NU2,P4_NU3,P4_NU4 ],

    "PICK2_EVENING"     : [P3_FECHA,P3_NU1,P3_NU2],
    "PICK3_EVENING"     : [P3_FECHA,P3_NU1,P3_NU2,P3_NU3],
    "PICK4_EVENING"     : [P4_FECHA,P4_NU1,P4_NU2,P4_NU3,P4_NU4 ],

    "MODALIDAD"         : MODALIDAD_PICK2_3_4
}

#! OTRA PAGINA

URL         =   'https://www.flalottery.com/'
URL_PICK_3  =   'https://www.flalottery.com/pick3'
URL_PICK_4  =   'https://www.flalottery.com/pick4'
URL_PICK_2  =   'https://www.flalottery.com/pick2'

FECHA               =   '/html/body/div[3]/div[3]/section[2]/div/div[2]/div[1]/p[2]'
NUMERO_1            =   '/html/body/div[3]/div[3]/section[2]/div/div[2]/div[1]/p[3]/span[1]'
NUMERO_2            =   '/html/body/div[3]/div[3]/section[2]/div/div[2]/div[1]/p[3]/span[3]'
NUMERO_3            =   '/html/body/div[3]/div[3]/section[2]/div/div[2]/div[1]/p[3]/span[5]'
NUMERO_4            =   '/html/body/div[3]/div[3]/section[2]/div/div[2]/div[1]/p[3]/span[7]'

#!TENGO QUE ARREGLA FLORIDA SEGUNDA PAGINA PAXTH SON DIFERENTES EN PICK3 Y PICK4
FLORIDA_PAGE_2 = {

    'URL_MIDDAY' : [URL, URL_PICK_3, URL_PICK_4, URL_PICK_2],
    'URL_EVENING' : [URL, URL_PICK_3, URL_PICK_4, URL_PICK_2],

    'PICK4_MIDDAY' : [FECHA,NUMERO_1,NUMERO_2],
    'PICK3_MIDDAY' : [FECHA,NUMERO_1,NUMERO_2,NUMERO_3 ],
    'PICK4_MIDDAY' : [FECHA,NUMERO_1,NUMERO_2,NUMERO_3,NUMERO_4 ],


    'PICK2_EVENING' : [
        '/html/body/div[3]/div[3]/section[2]/div/div[2]/div[3]/p[2]',
        '/html/body/div[3]/div[3]/section[2]/div/div[2]/div[3]/p[3]/span[1]',
        '/html/body/div[3]/div[3]/section[2]/div/div[2]/div[3]/p[3]/span[3]'
    ],
    'PICK3_EVENING' : [
        '/html/body/div[3]/div[3]/section[2]/div/div[2]/div[3]/div[1]/p[2]',
        '/html/body/div[3]/div[3]/section[2]/div/div[2]/div[3]/div[1]/p[3]/span[1]',
        '/html/body/div[3]/div[3]/section[2]/div/div[2]/div[3]/div[1]/p[3]/span[3]',
        '/html/body/div[3]/div[3]/section[2]/div/div[2]/div[3]/div[1]/p[3]/span[5]'
        ],
    'PICK4_EVENING' : [
        '/html/body/div[3]/div[3]/section[2]/div/div[2]/div[3]/p[2]',
        '/html/body/div[3]/div[3]/section[2]/div/div[2]/div[3]/p[3]/span[1]',
        '/html/body/div[3]/div[3]/section[2]/div/div[2]/div[3]/p[3]/span[3]',
        '/html/body/div[3]/div[3]/section[2]/div/div[2]/div[3]/p[3]/span[5]',
        '/html/body/div[3]/div[3]/section[2]/div/div[2]/div[3]/p[3]/span[7]'
    ],

    "MODALIDAD"         : MODALIDAD_PICK2_3_4
}


#! ----------------------------------------------------------------------------------------------------------------------------------

FLORIDA_TODO = [FLORIDA_LOTTERYUSA,FLORIDA_LOTTERYUSA]