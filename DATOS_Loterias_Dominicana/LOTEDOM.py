from DATOS_Loterias_Dominicana.LOTERIAS_DOMINICAS_PAGES import *

PAGES       = 'https://lotedom.com/'
FECHA       = '/html/body/app-root/app-layout/div/div[2]/div/app-inicio/div/div[2]/div[1]/div[1]/div'
NU_1        = '/html/body/app-root/app-layout/div/div[2]/div/app-inicio/div/div[2]/div[1]/div[2]/div/div/div[2]/div[1]/div[2]/div[1]/span[2]'
NU_2        = '/html/body/app-root/app-layout/div/div[2]/div/app-inicio/div/div[2]/div[1]/div[2]/div/div/div[2]/div[1]/div[2]/div[2]/span[2]'
NU_3        = '/html/body/app-root/app-layout/div/div[2]/div/app-inicio/div/div[2]/div[1]/div[2]/div/div/div[2]/div[1]/div[2]/div[3]/span[2]'

LOTEDOM = {
    'URL' : [PAGES, PAGES],
    'NUMEROS' : [FECHA, NU_1, NU_2, NU_3 ]
}

url_pages2='https://loteriasdominicanas.com/lotedom/quiniela'

LOTEDOM_PAGE_2 = {
    'URL'       : [PAGES_URL, url_pages2 ],
    'NUMEROS'   : [FECHA_XPATH,NUMERO_1_XPATH, NUMERO_2_XPATH,NUMERO_3_XPATH]
}

LOTEDOM_TODO =[LOTEDOM,LOTEDOM_PAGE_2]