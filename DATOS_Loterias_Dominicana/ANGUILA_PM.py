from DATOS_Loterias_Dominicana.LOTERIAS_DOMINICAS_PAGES import *

Pages = 'https://anguillalottery.ai/'
Fecha = '/html/body/div[4]/div/div[2]/div[1]/div[1]/div'
NU_1 = '/html/body/div[4]/div/div[2]/div[1]/div[2]/span[1]'
NU_2 = '/html/body/div[4]/div/div[2]/div[1]/div[2]/span[2]'
NU_3 = '/html/body/div[4]/div/div[2]/div[1]/div[2]/span[3]'

ANGUILA_PM = {
    'URL'       :   [Pages, Pages],
    'NUMEROS'   :   [Fecha, NU_1, NU_2, NU_3 ]
}

url_pages2 = 'https://loteriasdominicanas.com/anguila/anguila-noche'

ANGUILA_PM_PAGE_2 = {
    'URL'       : [PAGES_URL, url_pages2 ],
    'NUMEROS'   : [FECHA_XPATH,NUMERO_1_XPATH, NUMERO_2_XPATH,NUMERO_3_XPATH]
}

ANGUILA_PM_TODO = [ANGUILA_PM,ANGUILA_PM]