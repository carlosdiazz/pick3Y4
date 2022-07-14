# selenium 4
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromiumService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.utils import ChromeType
from selenium.webdriver.common.by import By
import time
from Funciones_Especiales import Validar_Fecha_Hoy, comprobar_pick3,comprobar_pick4

class API():

    def __init__(self):
        print("Se Instancio una nueva clase")

    def Navegador(self,ARR):
        self.chrome_options = webdriver.ChromeOptions()
        self.chrome_options.add_experimental_option('excludeSwitches', ['enable-automation'])
        self.chrome_options.add_argument("--headless")
        self.driver = webdriver.Chrome(service=ChromiumService(ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install()),options=self.chrome_options)
        self.driver.delete_all_cookies()
        self.driver.get(ARR['URL'][0])
        self.driver.set_page_load_timeout(30)

    def devolver_numeros(self, ARR):
        try:
            self.Navegador(ARR)
            pick3 = comprobar_pick3(self.PICK3(ARR))
            pick4 = comprobar_pick4(self.PICK4(ARR))

            if(pick3 and pick4):
                return {
                    "PICK3":pick3,
                    "PICK4":pick4
                }
            else:
                return False
        except:
            return False

    def PICK3(self,arrP3):
        try:
            self.driver.delete_all_cookies()
            self.driver.get(arrP3['URL'][1])
            self.driver.implicitly_wait(20)
            time.sleep(4)
            fecha_p3 = self.driver.find_element(By.XPATH, arrP3['PICK3'][0]).text;self.driver.implicitly_wait(20)
            time.sleep(4)
            if(Validar_Fecha_Hoy(fecha_p3)):
                nu_p3_1 = self.driver.find_element(By.XPATH, arrP3['PICK3'][1]).text;self.driver.implicitly_wait(20)
                nu_p3_2 = self.driver.find_element(By.XPATH, arrP3['PICK3'][2]).text;self.driver.implicitly_wait(20)
                nu_p3_3 = self.driver.find_element(By.XPATH, arrP3['PICK3'][3]).text;self.driver.implicitly_wait(20)
                return [nu_p3_1,nu_p3_2,nu_p3_3]
            else:
                return False
        except:
                return False

    def PICK4(self,arrP4):
        try:
            self.driver.get(arrP4['URL'][2])
            self.driver.implicitly_wait(20)
            time.sleep(4)
            fecha_p3 = self.driver.find_element(By.XPATH, arrP4['PICK4'][0]).text;self.driver.implicitly_wait(20)
            time.sleep(4)
            if(Validar_Fecha_Hoy(fecha_p3)):

                num_p4_1 = self.driver.find_element(By.XPATH, arrP4['PICK4'][1]).text;self.driver.implicitly_wait(20)
                num_p4_2 = self.driver.find_element(By.XPATH, arrP4['PICK4'][2]).text;self.driver.implicitly_wait(20)
                num_p4_3 = self.driver.find_element(By.XPATH, arrP4['PICK4'][3]).text;self.driver.implicitly_wait(20)
                num_p4_4 = self.driver.find_element(By.XPATH, arrP4['PICK4'][4]).text;self.driver.implicitly_wait(20)
                return [num_p4_1,num_p4_2,num_p4_3,num_p4_4]
            else:
                return False
        except:
                return False
