from DATOS_Loterias_Dominicana.LOTERIAS_DOMINICAS_PAGES import *

PAGES = 'https://www.kinglotterysxm.com/'
RESULTADO = 'https://www.kinglotterysxm.com/sorteo/sxm-medio-dia-quiniela/'
FECHA = '/html/body/main/section/div[1]/div/div[1]/div/div[3]/span'
NU1 = '/html/body/main/section/div[1]/div/div[1]/div/div[2]/span[1]'
NU2 = '/html/body/main/section/div[1]/div/div[1]/div/div[2]/span[2]'
NU3 = '/html/body/main/section/div[1]/div/div[1]/div/div[2]/span[3]'

KING_LOTTERY_DIA = {
    'URL' : [PAGES, RESULTADO],
    'NUMEROS' : [FECHA, NU1, NU2, NU3 ]
}

url_pages2 = 'https://loteriasdominicanas.com/king-lottery/quiniela-dia'

KING_LOTTERY_DIA_PAGE_2 = {
    'URL'       : [PAGES_URL, url_pages2 ],
    'NUMEROS'   : [FECHA_XPATH,NUMERO_1_XPATH, NUMERO_2_XPATH,NUMERO_3_XPATH]
}

KING_LOTTERY_DIA_TODO = [KING_LOTTERY_DIA, KING_LOTTERY_DIA_PAGE_2]