from DATOS_Loterias_Dominicana.LOTERIAS_DOMINICAS_PAGES import *

PAGES       = 'https://laprimera.do/'
FECHA       = '/html/body/div/div/div/div[1]/div[1]/div/div[4]/div/div[1]/div/div[3]/div[2]/div'
NU_1        = '/html/body/div/div/div/div[1]/div[1]/div/div[4]/div/div[1]/div/div[3]/div[1]/div/div/div[1]/span'
NU_2        = '/html/body/div/div/div/div[1]/div[1]/div/div[4]/div/div[1]/div/div[3]/div[1]/div/div/div[2]/span'
NU_3        = '/html/body/div/div/div/div[1]/div[1]/div/div[4]/div/div[1]/div/div[3]/div[1]/div/div/div[3]/span'

PRIMERA_DIA = {
    'URL' : [PAGES, PAGES],
    'NUMEROS' : [FECHA, NU_1, NU_2, NU_3 ]
}

url_pages2 = 'https://loteriasdominicanas.com/la-primera/quiniela-medio-dia'

PRIMERA_DIA_PAGE_2 = {
    'URL'       : [PAGES_URL, url_pages2 ],
    'NUMEROS'   : [FECHA_XPATH,NUMERO_1_XPATH, NUMERO_2_XPATH,NUMERO_3_XPATH]
}

PRIMERA_DIA_TODO = [PRIMERA_DIA,PRIMERA_DIA_PAGE_2 ]