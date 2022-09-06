from DATOS_Loterias_Dominicana.LOTERIAS_DOMINICAS_PAGES import *

PAGES       = 'https://www.kinglotterysxm.com/'
RESULTADO   = 'https://www.kinglotterysxm.com/sorteo/sxm-noche-quiniela/'
FECHA       = '/html/body/main/section/div[1]/div/div[1]/div/div[3]/span'
NU_1        = '/html/body/main/section/div[1]/div/div[1]/div/div[2]/span[1]'
NU_2        = '/html/body/main/section/div[1]/div/div[1]/div/div[2]/span[2]'
NU_3        = '/html/body/main/section/div[1]/div/div[1]/div/div[2]/span[3]'

KING_LOTTERY_NOCHE = {
    'URL' : [PAGES, RESULTADO],
    'NUMEROS' : [FECHA, NU_1, NU_2, NU_3 ]
}

url_pages2 = 'https://loteriasdominicanas.com/king-lottery/quiniela-noche'

KING_LOTTERY_NOCHE_PAGE_2 = {
    'URL'       : [PAGES_URL, url_pages2 ],
    'NUMEROS'   : [FECHA_XPATH,NUMERO_1_XPATH, NUMERO_2_XPATH,NUMERO_3_XPATH]
}

KING_LOTTERY_NOCHE_TODO = [KING_LOTTERY_NOCHE, KING_LOTTERY_NOCHE_PAGE_2]