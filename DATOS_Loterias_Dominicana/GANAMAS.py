from DATOS_Loterias_Dominicana.LOTERIAS_DOMINICAS_PAGES import *

PAGES       = 'https://loterianacional.gob.do/index.php'
FECHA       = '/html/body/div[1]/div[2]/div[1]/div[2]/div/div/div[1]/table[2]/tbody/tr[1]/td[2]/span'
NU1         = '/html/body/div[1]/div[2]/div[1]/div[2]/div/div/div[1]/table[2]/tbody/tr[2]/td[1]/span'
NU2         = '/html/body/div[1]/div[2]/div[1]/div[2]/div/div/div[1]/table[2]/tbody/tr[2]/td[2]/span'
NU3         = '/html/body/div[1]/div[2]/div[1]/div[2]/div/div/div[1]/table[2]/tbody/tr[2]/td[3]/span'

GANAMAS = {
    'URL' : [PAGES,PAGES ],
    'NUMEROS' : [FECHA, NU1, NU2, NU3 ]
}

url_pages2 = 'https://loteriasdominicanas.com/loteria-nacional/gana-mas'

GANAMAS_PAGE_2 = {
    'URL'       : [PAGES_URL, url_pages2 ],
    'NUMEROS'   : [FECHA_XPATH,NUMERO_1_XPATH, NUMERO_2_XPATH,NUMERO_3_XPATH]
}

GANAMAS_TODO =[GANAMAS,GANAMAS_PAGE_2]