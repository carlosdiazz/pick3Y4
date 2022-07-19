# selenium 4
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromiumService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.utils import ChromeType
from selenium.webdriver.common.by import By
import time

class Publicar_En_Plataformas():

    def __init__(self, user, plataforma, Loteria):
        self.plataforma_url = plataforma['URL']
        self.input_user = plataforma['Input_User']
        self.input_pass = plataforma['Input_Password']
        self.button_login = plataforma['Boton_Login']
        
        
        self.plataforma_user = user['USER']
        self.plataforma_pass = user['PASS']
        self.plataforma_url_premios = plataforma['URL']+plataforma['URL_PREMIOS']
        
        self.loteria = Loteria['loteria']
        self.sorteo = Loteria['sorteo']
        self.numeros_ganadpres = Loteria['numeros_ganadores']
        
        print("Se Instancio una nueva clase")

    def Navegador(self):
        self.chrome_options = webdriver.ChromeOptions()
        self.chrome_options.add_experimental_option('excludeSwitches', ['enable-automation'])
        #self.chrome_options.add_argument("--headless")
        self.driver = webdriver.Chrome(service=ChromiumService(ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install()),options=self.chrome_options)
        self.driver.delete_all_cookies()
        self.driver.get(self.plataforma_url)
        self.driver.set_page_load_timeout(30)

    def iniciar_seccion(self):
        input_user = self.driver.find_element(by=By.XPATH, value=self.input_user );self.driver.implicitly_wait(20)
        input_user.send_keys(self.plataforma_user)
        input_pass = self.driver.find_element(by=By.XPATH, value=self.input_pass );self.driver.implicitly_wait(20)
        input_pass.send_keys(self.plataforma_pass)
        button_login = self.driver.find_element(by=By.XPATH, value=self.button_login );self.driver.implicitly_wait(20)
        button_login.click()
        time.sleep(5)
        


    def publicar(self,):

        try:
            self.Navegador()
            self.iniciar_seccion()
            self.driver.get(self.plataforma_url_premios)
            time.sleep(15)
            #else:
            #    self.driver.quit()
            #    return False
        except:
            return False


