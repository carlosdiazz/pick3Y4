# selenium 4
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromiumService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.utils import ChromeType
from selenium.webdriver.common.by import By
import time

from Funciones_Especiales import fecha, CONSULTAR_NUMEROS_API, saber_sorteo
from config import user_desarrollo
from Datos_Loterias.DATOS_PLATAFORMA import PLATAFORMA_MEGA
class Publicar_En_Plataformas():

    def __init__(self, user, plataforma, Loteria):
        self.plataforma_url = plataforma['URL']
        self.input_user = plataforma['Input_User']
        self.input_pass = plataforma['Input_Password']
        self.button_login = plataforma['Boton_Login']
        self.input_loteria = plataforma['Input_Loteria']
        self.input_sorteo = plataforma['Input_Sorteo']
        self.Seleccionar_Loteria = plataforma['Seleccionar_Loteria']
        self.Loteria_que_se_selecciono = plataforma['Loteria_que_se_selecciono']
        self.Input_premio = plataforma['Input_premio']
        self.boton_premiar = plataforma['Boton_Premiar']

        self.plataforma_user = user['USER']
        self.plataforma_pass = user['PASS']
        self.plataforma_url_premios = plataforma['URL']+plataforma['URL_PREMIOS']

        self.loteria = Loteria['loteria']
        self.sorteo = Loteria['sorteo']
        self.numeros_ganadores = Loteria['numeros_ganadores']
        self.fecha = Loteria['fecha']

        print("Se Instancio una nueva clase Para Premiar")

    def Navegador(self):
        self.chrome_options = webdriver.ChromeOptions()
        self.chrome_options.add_experimental_option('excludeSwitches', ['enable-automation'])
        self.chrome_options.accept_insecure_certs=True
        self.chrome_options.add_argument("--headless")
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
        time.sleep(2)

    def colocar_premios(self):
        try:
            self.driver.get(self.plataforma_url_premios)
            time.sleep(2)
            input_loteria = self.driver.find_element(by=By.XPATH, value=self.input_loteria );self.driver.implicitly_wait(20)
            input_loteria.send_keys(self.loteria)
            time.sleep(2)
            input_sorteo = self.driver.find_element(by=By.XPATH, value=self.input_sorteo );self.driver.implicitly_wait(20)
            input_sorteo.send_keys(self.sorteo)
            time.sleep(2)
            input_seleccionar_loteria = self.driver.find_element(by=By.XPATH, value=self.Seleccionar_Loteria );self.driver.implicitly_wait(20)
            input_seleccionar_loteria.click()
            time.sleep(2)
            Loteria_que_se_selecciono = self.driver.find_element(by=By.XPATH, value=self.Loteria_que_se_selecciono ).text;self.driver.implicitly_wait(20)
            if(Loteria_que_se_selecciono.endswith(self.sorteo)):
                input_numeros_ganadores = self.driver.find_element(by=By.XPATH, value=self.Input_premio );self.driver.implicitly_wait(20)
                input_numeros_ganadores.send_keys(self.numeros_ganadores)
                time.sleep(1)
                boton_premiar = self.driver.find_element(by=By.XPATH, value=self.boton_premiar );self.driver.implicitly_wait(20)
                boton_premiar.click()
                time.sleep(4)
                print("Se premio Correctamente")
                return True
            else:
                return False

        except:
            return False

    def publicar(self):

        try:
            if(self.fecha == fecha('%d-%m-%Y')):
                self.Navegador()
                self.iniciar_seccion()
                saber_premio = self.colocar_premios()

                if(saber_premio):
                    #SE PREMIO CORRECTAMENTE
                    self.driver.quit()
                    return True

                else:
                    self.driver.quit()
                    return False
            else:
                #VINO CON UNA FECHA QUE NO ES DE HOY
                return False
        except:
            return False


class Buscar_Numeros_Premiar():
    
    def __init__(self, obj):
        self.loteria = obj['LOTERIA']
        self.sorteo = obj['SORTEO']

    def buscar(self):
        #? Con esta funcion buscare los numeros ganadores
        self.fecha = fecha('%d-%m-%Y')
        numeros = CONSULTAR_NUMEROS_API(self.loteria,self.sorteo,self.fecha)
        if(numeros['error'] == False):
            loteria_a_publicar = numeros['message'][0]

            arrp3 = {
                'loteria'           :   'PICK 3',
                'fecha'             :   loteria_a_publicar['fecha'],
                "sorteo"            :   loteria_a_publicar['loteria'] +" "+saber_sorteo(loteria_a_publicar['sorteo']),
                'numeros_ganadores' :   loteria_a_publicar['numeros_ganadores']['PICK3']
            }

            arrp4 = {
                'loteria'           :   'PICK 4',
                'fecha'             :   loteria_a_publicar['fecha'],
                "sorteo"            :   loteria_a_publicar['loteria'] +" "+saber_sorteo(loteria_a_publicar['sorteo']),
                'numeros_ganadores' :   loteria_a_publicar['numeros_ganadores']['PICK4']
            }

            publicar_P3 = Publicar_En_Plataformas(user_desarrollo, PLATAFORMA_MEGA,arrp3 ).publicar()
            publicar_P4 = Publicar_En_Plataformas(user_desarrollo, PLATAFORMA_MEGA,arrp4 ).publicar()
            if(publicar_P3 and publicar_P4):
                print(f"SE PREMIO CORRECTAMENTE LA LOTERIA: {self.loteria }CON EL SORTEO: {self.sorteo}")
            else:
                print(f"NOOOOOOOO SE PREMIO LA LOTERIA: {self.loteria }CON EL SORTEO: {self.sorteo}")

        else:
            print(f"NO SE PREMIO ESTA LOTERIA: {self.loteria} COn este sorteo {self.sorteo}")