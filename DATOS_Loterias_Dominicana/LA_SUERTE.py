from DATOS_Loterias_Dominicana.LOTERIAS_DOMINICAS_PAGES import *

PAGES       = 'https://lasuertedominicana.com/app/index.php/front/index'
FECHA       = '/html/body/div[2]/div[3]/main/div/div[2]/div/p'
NU_1        = '/html/body/div[2]/div[3]/main/div/div[2]/div/div/div[1]/span'
NU_2        = '/html/body/div[2]/div[3]/main/div/div[2]/div/div/div[2]/span'
NU_3        = '/html/body/div[2]/div[3]/main/div/div[2]/div/div/div[3]/span'

LA_SUERTE = {
    'URL' : [PAGES, PAGES ],
    'NUMEROS' : [FECHA, NU_1, NU_2, NU_3 ]
}

url_pages2 = 'https://loteriasdominicanas.com/la-suerte-dominicana/quiniela'

LA_SUERTE_PAGE_2 = {
    'URL'       : [PAGES_URL, url_pages2 ],
    'NUMEROS'   : [FECHA_XPATH,NUMERO_1_XPATH, NUMERO_2_XPATH,NUMERO_3_XPATH]
}

#! CAMBIAR AQUI ESTOY TOMANDO LOS NUMEROS DE LOTERIAS DOMINICANAS
LA_SUERTE_TODO = [LA_SUERTE_PAGE_2, LA_SUERTE_PAGE_2]