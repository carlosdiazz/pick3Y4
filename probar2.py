
URL_Plantillas = 'https://sanchez.orkapi.net/operaciones/sorteo_plantillas/'
XPATH_boton_loto4 = '/html/body/div[2]/div/div/div/div[2]/div[1]/div/div[2]/div/table/tbody/tr[14]/td'
XPATH_martes ="/html/body/div[2]/div/div/div/div[2]/div[2]/div/div[2]/div/div/ul/li[6]/a"
                #='/html/body/div[2]/div/div/div/div[2]/div[2]/div/div[2]/div/div/ul/li[6]/a'

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromiumService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.utils import ChromeType
from selenium.webdriver.common.by import By
from Datos_Loterias.DATOS_PLATAFORMA import PLATAFORMA_SANCHEZ
import time

class desactivar_sorteos():

    def __init__(self, plataforma):
        self.plataforma_url             =   plataforma['URL']
        self.input_user                 =   plataforma['Input_User']
        self.input_pass                 =   plataforma['Input_Password']
        self.button_login               =   plataforma['Boton_Login']
        self.plataforma_user            =   'ADMIN'
        self.plataforma_pass            =   '12121212'


        print("Se Instancio una nueva clase Para Premiar")

    def Navegador(self):
        try:
            self.chrome_options = webdriver.ChromeOptions()
            self.chrome_options.add_experimental_option('excludeSwitches', ['enable-automation'])
            self.chrome_options.accept_insecure_certs=True
            self.driver = webdriver.Chrome(service=ChromiumService(ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install()),options=self.chrome_options)
            self.driver.delete_all_cookies()
            self.driver.get(self.plataforma_url)
            self.driver.set_page_load_timeout(30)

        except:
            print("error")

    def desactivar_picks(self):
        try:
            self.Navegador()
            self.iniciar_seccion()

            for i in range(40):
                try:
                    self.driver.get(URL_Plantillas) #Aqyu viy a la urkl de plantilla
                    time.sleep(1)
                    loteria_elegir = self.driver.find_element(by=By.XPATH, value=XPATH_boton_loto4 );self.driver.implicitly_wait(20)
                    time.sleep(1)
                    loteria_elegir.click()
                    time.sleep(1)
                    elegir_dia = self.driver.find_element(by=By.XPATH, value=XPATH_martes );self.driver.implicitly_wait(20)
                    time.sleep(1)
                    elegir_dia.click()
                    time.sleep(1)
                    url_xpath= f'/html/body/div[2]/div/div/div/div[2]/div[2]/div/div[2]/div/div/div/div[6]/table-sorteo-plantilla/table/tbody/tr[{i+1}]/td[5]/crud-toolbar/div/a[2]'
                    print(url_xpath)
                    loteriaXpath = self.driver.find_element(by=By.XPATH, value=url_xpath )
                    time.sleep(1)
                    loteriaXpath.click()
                    time.sleep(1)
                    click_desactivar = '/html/body/div[2]/div/div/div/form/div[1]/div[1]/div[1]/div[1]/h3/div/div/div/span[2]'
                    desactivar_sorteo = self.driver.find_element(by=By.XPATH, value=click_desactivar )
                    time.sleep(1)
                    desactivar_sorteo.click()
                    time.sleep(1)
                    click_actualziar = '/html/body/div[2]/div/div/div/form/div[2]/div/div/crudbuttons/div/div/button[1]'
                    desactivar_sorteo = self.driver.find_element(by=By.XPATH, value=click_actualziar )
                    time.sleep(1)
                    desactivar_sorteo.click()
                    time.sleep(1)
                except Exception as e: print(e)
                    #print("error")
                    
        except:
            return "Paso algo"

    def iniciar_seccion(self):

        try:
            input_user = self.driver.find_element(by=By.XPATH, value=self.input_user );self.driver.implicitly_wait(20)
            input_user.send_keys(self.plataforma_user)
            input_pass = self.driver.find_element(by=By.XPATH, value=self.input_pass );self.driver.implicitly_wait(20)
            input_pass.send_keys(self.plataforma_pass)
            button_login = self.driver.find_element(by=By.XPATH, value=self.button_login );self.driver.implicitly_wait(20)
            button_login.click()
            time.sleep(2)

        except:
            return (True, '\n\nNo se pudo hacer login\n\n', False)


    #def buscar_loterias(self):
    #    try:
    #        self.driver.get(self.plataforma_url_premios)
    #        time.sleep(5)
    #        #COLOCAR FECHA
    #        input_fecha = self.driver.find_element(by=By.XPATH, value=self.Input_fecha );self.driver.implicitly_wait(20)
    #        input_fecha.send_keys(self.fecha)
    #        time.sleep(5)
#
    #        #COLOCAR LOTERIA
    #        input_loteria = self.driver.find_element(by=By.XPATH, value=self.input_loteria );self.driver.implicitly_wait(20)
    #        input_loteria.send_keys(self.loteria)
    #        time.sleep(3)
#
    #        #COLOCAR SORTEO
    #        input_sorteo = self.driver.find_element(by=By.XPATH, value=self.input_sorteo );self.driver.implicitly_wait(20)
    #        input_sorteo.send_keys(self.sorteo)
    #        time.sleep(3)
#
    #        #SELECCIONAR LOTERIA
    #        input_seleccionar_loteria = self.driver.find_element(by=By.XPATH, value=self.Seleccionar_Loteria );self.driver.implicitly_wait(20)
    #        input_seleccionar_loteria.click()
    #        time.sleep(3)
#
    #        #LOTERIA SELECIONADA
    #        Loteria_que_se_selecciono = self.driver.find_element(by=By.XPATH, value=self.Loteria_que_se_selecciono ).text;self.driver.implicitly_wait(20)
#
    #        #VALIDAR QUE SEA LA LOTERIA CORRECTA
    #        if(Loteria_que_se_selecciono.endswith(self.sorteo)):
    #            return Response(False, "\n\nEsta es la loteria que se selecciono\n\n", False)
    #        else:
    #            return Response(True, '\n\nNo se pudo validar el sorteo de la plataforma\n\n', False)
#
    #    except:
    #        return Response(True, '\n\nNo se pudo encontrar la direccion de la loteria o del sorteo en plataforma\n\n', False)
#



    #def colocar_tradicionales(self):
    #    try:
    #        input_numero_1 = self.driver.find_element(by=By.XPATH, value=self.Input_premio1 );self.driver.implicitly_wait(20)
    #        if(input_numero_1.is_enabled()):
    #            input_numero_1.send_keys(self.numeros_ganadores['NU1'])
    #            time.sleep(2)
#
    #            input_numero_2 = self.driver.find_element(by=By.XPATH, value=self.Input_premio2 );self.driver.implicitly_wait(20)
    #            input_numero_2.send_keys(self.numeros_ganadores['NU2'])
    #            time.sleep(2)
#
    #            input_numero_3 = self.driver.find_element(by=By.XPATH, value=self.Input_premio3 );self.driver.implicitly_wait(20)
    #            input_numero_3.send_keys(self.numeros_ganadores['NU3'])
    #            time.sleep(2)
#
    #            boton_premiar = self.driver.find_element(by=By.XPATH, value=self.boton_premiar );self.driver.implicitly_wait(20)
    #            boton_premiar.click()
    #            time.sleep(4)
    #            self.driver.quit()
    #            message=(f"\n\nLOTERIA => {self.loteria}\nSORTEO => {self.sorteo}\n\nNUMEROS => {self.numeros_ganadores['NU1']}-{self.numeros_ganadores['NU2']}-{self.numeros_ganadores['NU3']}\n\n")
    #            return Response(False, message, True)
    #        else:
    #            self.driver.quit()
    #            return Response(False, f'\n\nEsta loteria esta Premiada {self.loteria} sorteo: {self.sorteo}\n\n', True)
    #    except:
    #        return Response(True, f'\n\nNo se pudo premiar esta loteria: {self.loteria} sorteo: {self.sorteo}\n\n', False)


print(desactivar_sorteos(PLATAFORMA_SANCHEZ).desactivar_picks())