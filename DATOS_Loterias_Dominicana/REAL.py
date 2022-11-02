from DATOS_Loterias_Dominicana.LOTERIAS_DOMINICAS_PAGES import *

PAGES       = 'https://www.lotoreal.com.do/'
FECHA       = '/html/body/main/div[1]/div[2]/h2'
NU_1        = '/html/body/main/div[1]/div[2]/div[2]/div[1]/h2'
NU_2        = '/html/body/main/div[1]/div[2]/div[2]/div[2]/h2'
NU_3        = '/html/body/main/div[1]/div[2]/div[2]/div[3]/h2'

REAL = {
    'URL' : [PAGES,PAGES ],
    'NUMEROS' : [FECHA, NU_1, NU_2, NU_3 ]
}

url_pages2 = 'https://loteriasdominicanas.com/loto-real/quiniela'

REAL_PAGE_2 = {
    'URL'       : [PAGES_URL, url_pages2 ],
    'NUMEROS'   : [FECHA_XPATH,NUMERO_1_XPATH, NUMERO_2_XPATH,NUMERO_3_XPATH]
}

REAL_TODO = [REAL,REAL_PAGE_2]