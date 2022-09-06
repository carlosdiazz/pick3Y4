from DATOS_Loterias_Dominicana.LOTERIAS_DOMINICAS_PAGES import *

PAGES       = 'https://loterianacional.gob.do/index.php'
FECHA       = '/html/body/div[1]/div[2]/div[1]/div[2]/div/div/div[1]/table[3]/tbody/tr[1]/td[2]/span'
NU_1        = '/html/body/div[1]/div[2]/div[1]/div[2]/div/div/div[1]/table[3]/tbody/tr[2]/td[1]/span'
NU_2        = '/html/body/div[1]/div[2]/div[1]/div[2]/div/div/div[1]/table[3]/tbody/tr[2]/td[2]/span'
NU_3        = '/html/body/div[1]/div[2]/div[1]/div[2]/div/div/div[1]/table[3]/tbody/tr[2]/td[3]/span'

NACIONAL = {
    'URL' : [PAGES, PAGES ],
    'NUMEROS' : [FECHA, NU_1, NU_2, NU_3 ]
}

url_pages2 = 'https://loteriasdominicanas.com/loteria-nacional/quiniela'

NACIONAL_PAGE_2 = {
    'URL'       : [PAGES_URL, url_pages2 ],
    'NUMEROS'   : [FECHA_XPATH,NUMERO_1_XPATH, NUMERO_2_XPATH,NUMERO_3_XPATH]
}

NACIONAL_TODO = [NACIONAL,NACIONAL_PAGE_2 ]