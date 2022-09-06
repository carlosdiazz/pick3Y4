from DATOS_Loterias_Dominicana.LOTERIAS_DOMINICAS_PAGES import *

PAGES       = 'https://www.leidsa.com/'
FECHA       = '/html/body/div/section[2]/div/div[3]/div[3]/div/div[1]/p'
NU_1        = '/html/body/div/section[2]/div/div[3]/div[3]/div/div[2]/table/tbody/tr[1]/td'
NU_2        = '/html/body/div/section[2]/div/div[3]/div[3]/div/div[2]/table/tbody/tr[2]/td'
NU_3        = '/html/body/div/section[2]/div/div[3]/div[3]/div/div[2]/table/tbody/tr[3]/td'

LEIDSA = {
    'URL' : [PAGES, PAGES],
    'NUMEROS' : [FECHA, NU_1, NU_2, NU_3 ]
}

url_pages2 = 'https://loteriasdominicanas.com/leidsa/quiniela-pale'

LEIDSA_PAGE_2 = {
    'URL'       : [PAGES_URL, url_pages2 ],
    'NUMEROS'   : [FECHA_XPATH,NUMERO_1_XPATH, NUMERO_2_XPATH,NUMERO_3_XPATH]
}

LEIDSA_TODO = [LEIDSA,LEIDSA_PAGE_2]