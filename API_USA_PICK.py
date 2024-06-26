# ESTE ES EL ARCHIVO QUE FUNCIONA COMO UNA API PARA BUSCAR LOS NUMEROS GANADORES DEL PICK 3 Y PICK 4
#CUANDO SE INSTANCIA UNA CLASE SE MANDA UN ARREGLO DE LA LOTERIA A BUCAR CON SUS PAXTH Y SE USA LA FUNCION DE DECOLVER NUMEROS DE ESTA CLASE
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromiumService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.utils import ChromeType
from selenium.webdriver.common.by import By
import time
from Funciones_Especiales import comprobar_pick2, comprobar_pick3,comprobar_pick4, Validar_Fecha_hoy2

class API_USA_PICK():

    def __init__(self):
        print("Se Instancio una nueva clase DE API AMERICANOS PARA BUSCAR NUMEROS")

    def Navegador(self,ARR):
        self.chrome_options = webdriver.ChromeOptions()
        self.chrome_options.add_experimental_option('excludeSwitches', ['enable-automation'])
        self.chrome_options.add_argument("--headless")
        self.driver = webdriver.Chrome(service=ChromiumService(ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install()),options=self.chrome_options)
        self.driver.delete_all_cookies()
        self.driver.get(ARR[f'URL_{self.sorteo}'][0])
        self.driver.set_page_load_timeout(360)

    def devolver_numeros(self, ARR,SORTEO,ARR_FECHA):
        self.sorteo     =   SORTEO
        self.ARR_FECHA  =   ARR_FECHA
        #! AQUI AGREGAR QUE ME LLEGUE SI EL NUMERO A BUSCAR ES EL PICK 3 o PICK 4 o EL PICK 
        #! ME LLEGARA DEL ARREGLO Y LUEGO SOLO VOY A BUSCAR LO QUE ME PIDAN
        try:
            if(ARR['MODALIDAD'] == 'PICK3_4'):
                self.Navegador(ARR)
                pick3 = comprobar_pick3(self.PICK3(ARR))
                pick4 = comprobar_pick4(self.PICK4(ARR))
                if(pick3 and pick4):
                    self.driver.quit()
                    return {
                        "PICK3":pick3,
                        "PICK4":pick4
                    }
                else:
                    self.driver.quit()
                    return False

            elif(ARR['MODALIDAD'] == 'PICK2_3_4'):
                self.Navegador(ARR)
                pick2 = comprobar_pick2(self.PICK2(ARR))
                pick3 = comprobar_pick3(self.PICK3(ARR))
                pick4 = comprobar_pick4(self.PICK4(ARR))
                if(pick3 and pick4 and pick2):
                    self.driver.quit()
                    return {
                        "PICK2":pick2,
                        "PICK3":pick3,
                        "PICK4":pick4
                    }
                else:
                    self.driver.quit()
                    return False
            else:
                print("AQUIIII")
                return False
        except:
            print('Paso una EXCEPT en el archivo API_USA_PICk')
            return False

    def PICK3(self,arrP3):
        try:
            self.driver.delete_all_cookies()
            self.driver.get(arrP3[f'URL_{self.sorteo}'][1])
            self.driver.implicitly_wait(20)
            time.sleep(4)
            fecha_p3 = self.driver.find_element(By.XPATH, arrP3[f'PICK3_{self.sorteo}'][0]).text;self.driver.implicitly_wait(20)
            time.sleep(4)
            #if(Validar_Fecha_Hoy(fecha_p3)): #?Antes validaba aqui
            if(Validar_Fecha_hoy2(self.ARR_FECHA, fecha_p3)):
                nu_p3_1 = self.driver.find_element(By.XPATH, arrP3[f'PICK3_{self.sorteo}'][1]).text;self.driver.implicitly_wait(20)
                nu_p3_2 = self.driver.find_element(By.XPATH, arrP3[f'PICK3_{self.sorteo}'][2]).text;self.driver.implicitly_wait(20)
                nu_p3_3 = self.driver.find_element(By.XPATH, arrP3[f'PICK3_{self.sorteo}'][3]).text;self.driver.implicitly_wait(20)
                pick3_arreglo = [nu_p3_1,nu_p3_2,nu_p3_3]
                if(len(pick3_arreglo)==3):
                    return pick3_arreglo
                else:
                    return False
            else:
                return False
        except:
                return False

    def PICK4(self,arrP4):
        try:
            self.driver.get(arrP4[f'URL_{self.sorteo}'][2])
            self.driver.implicitly_wait(20)
            time.sleep(4)
            fecha_p4 = self.driver.find_element(By.XPATH, arrP4[f'PICK4_{self.sorteo}'][0]).text;self.driver.implicitly_wait(20)
            time.sleep(4)
            #if(Validar_Fecha_Hoy(fecha_p4 )):#?Antes validaba aqui
            if(Validar_Fecha_hoy2(self.ARR_FECHA,fecha_p4 )):
                num_p4_1 = self.driver.find_element(By.XPATH, arrP4[f'PICK4_{self.sorteo}'][1]).text;self.driver.implicitly_wait(20)
                num_p4_2 = self.driver.find_element(By.XPATH, arrP4[f'PICK4_{self.sorteo}'][2]).text;self.driver.implicitly_wait(20)
                num_p4_3 = self.driver.find_element(By.XPATH, arrP4[f'PICK4_{self.sorteo}'][3]).text;self.driver.implicitly_wait(20)
                num_p4_4 = self.driver.find_element(By.XPATH, arrP4[f'PICK4_{self.sorteo}'][4]).text;self.driver.implicitly_wait(20)
                pick4_arreglo = [num_p4_1,num_p4_2,num_p4_3,num_p4_4]
                if(len(pick4_arreglo)==4):
                    return pick4_arreglo
                else:
                    return False
            else:
                return False
        except:
                return False

    def PICK2(self,arrP2):
        try:
            self.driver.get(arrP2[f'URL_{self.sorteo}'][3])
            self.driver.implicitly_wait(20)
            time.sleep(4)
            fecha_p2 = self.driver.find_element(By.XPATH, arrP2[f'PICK2_{self.sorteo}'][0]).text;self.driver.implicitly_wait(20)
            time.sleep(4)
            #if(Validar_Fecha_Hoy(fecha_p4 )):#?Antes validaba aqui
            if(Validar_Fecha_hoy2(self.ARR_FECHA,fecha_p2 )):
                num_p2_1 = self.driver.find_element(By.XPATH, arrP2[f'PICK2_{self.sorteo}'][1]).text;self.driver.implicitly_wait(20)
                num_p2_2 = self.driver.find_element(By.XPATH, arrP2[f'PICK2_{self.sorteo}'][2]).text;self.driver.implicitly_wait(20)
                pick2_arreglo = [num_p2_1,num_p2_2]
                if(len(pick2_arreglo)==2):
                    return pick2_arreglo
                else:
                    return False
            else:
                return False
        except:
                return False

