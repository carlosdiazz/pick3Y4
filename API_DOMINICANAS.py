# ESTE ES EL ARCHIVO QUE FUNCIONA COMO UNA API PARA BUSCAR LOS NUMEROS GANADORES DE LA LOTERIAS TRADICIONALES DOMINICANA
#CUANDO SE INSTANCIA UNA CLASE SE MANDA UN ARREGLO DE LA LOTERIA A BUCAR CON SUS PAXTH Y SE USA LA FUNCION DE DECOLVER NUMEROS DE ESTA CLASE
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromiumService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.utils import ChromeType
from selenium.webdriver.common.by import By
import time
from Funciones_Especiales import Validar_Fecha_Hoy, solo_undigito

class API_DOMINICANA():

    def __init__(self):
        print("Se Instancio una nueva clase DE API DOMINICANAS PARA BUSCAR NUMEROS")

    def Navegador(self,ARR):
        self.chrome_options = webdriver.ChromeOptions()
        self.chrome_options.add_experimental_option('excludeSwitches', ['enable-automation'])
        self.chrome_options.add_argument("--headless")
        self.driver = webdriver.Chrome(service=ChromiumService(ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install()),options=self.chrome_options)
        self.driver.delete_all_cookies()
        self.driver.get(ARR['URL'][0])
        self.driver.set_page_load_timeout(360)

    def devolver_numeros(self, ARR):
        try:
            self.Navegador(ARR)
            time.sleep(40) #AQUI DURO $) SEGUNDO PARA ESPERAR QUE LOS ANUNCIONS SE CIERREN EN LA SUERTE Y LEIDSA
            NUMEROS = self.BUSCAR_NUMEROS(ARR)

            if(NUMEROS):
                self.driver.quit()
                return {
                    "NU1"   :   NUMEROS[0],
                    "NU2"   :   NUMEROS[1],
                    "NU3"   :   NUMEROS[2],
                }
            else:
                self.driver.quit()
                return False
        except:
            print('Paso una EXCEPT en el archivo API_DOMINICANA_PICk')
            return False

    def BUSCAR_NUMEROS(self,ARR):
        try:
            self.driver.get(ARR['URL'][1])
            time.sleep(40)

            FECHA = self.driver.find_element(By.XPATH, ARR['NUMEROS'][0]).text;self.driver.implicitly_wait(20)
            if(Validar_Fecha_Hoy(FECHA)):
                NUMERO_1 = self.driver.find_element(By.XPATH, ARR['NUMEROS'][1]).text;self.driver.implicitly_wait(20);time.sleep(3)
                NUMERO_2 = self.driver.find_element(By.XPATH, ARR['NUMEROS'][2]).text;self.driver.implicitly_wait(20);time.sleep(3)
                NUMERO_3 = self.driver.find_element(By.XPATH, ARR['NUMEROS'][3]).text;self.driver.implicitly_wait(20);time.sleep(3)

                NUMERO_1 = solo_undigito(NUMERO_1)
                NUMERO_2 = solo_undigito(NUMERO_2)
                NUMERO_3 = solo_undigito(NUMERO_3)

                #! FUNCION para impedir que me publique 00 00 00, es un error de ANGUILA ------------------------------
                if(NUMERO_1 == '00' and NUMERO_2 == '00' and NUMERO_3 == '00'):
                    return False
                if(NUMERO_1 == '' or NUMERO_2 == '' or NUMERO_3 == ''):
                    return False
                else:
                    return [NUMERO_1,NUMERO_2,NUMERO_3]

            else:
                return False
        except:
            return False