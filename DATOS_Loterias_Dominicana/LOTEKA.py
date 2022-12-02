from DATOS_Loterias_Dominicana.LOTERIAS_DOMINICAS_PAGES import *

PAGES       = 'https://loteka.com.do/'
FECHA       = '/html/body/div[7]/div[1]/div/div/div[1]/div[2]/div[4]/div[2]'
NU_1        = '/html/body/div[7]/div[1]/div/div/div[1]/div[2]/div[4]/div[3]/div[1]'
NU_2        = '/html/body/div[7]/div[1]/div/div/div[1]/div[2]/div[4]/div[3]/div[2]'
NU_3        = '/html/body/div[7]/div[1]/div/div/div[1]/div[2]/div[4]/div[3]/div[3]'

LOTEKA = {
    'URL' : [PAGES, PAGES],
    'NUMEROS' : [FECHA, NU_1, NU_2, NU_3 ]
}

url_pages2 = 'https://loteriasdominicanas.com/loteka/quiniela-mega-decenas'

LOTEKA_PAGE_2 = {
    'URL'       : [PAGES_URL, url_pages2 ],
    'NUMEROS'   : [FECHA_XPATH,NUMERO_1_XPATH, NUMERO_2_XPATH,NUMERO_3_XPATH]
}

LOTEKA_TODO = [LOTEKA,LOTEKA_PAGE_2]