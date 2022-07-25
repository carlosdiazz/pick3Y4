# eSTE ARCHIVO ES QUIEN PUBLICA LOS NUMEROS GANAODRES SOLO EN LA PLATAFORMA DE LOTENET , SE LE MANDARA UN OBJECTO DE USER, PLATAFORMA, Y LOTERIA
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromiumService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.utils import ChromeType
from selenium.webdriver.common.by import By
import time
from VARIABLES import MODALIDAD, MODALIDAD_RD

from Funciones_Especiales import fecha

class PUBLICAR_EN_LOTENET_PICK():

    def __init__(self, user, plataforma):
        self.plataforma_url             =   plataforma['URL']
        self.input_user                 =   plataforma['Input_User']
        self.input_pass                 =   plataforma['Input_Password']
        self.button_login               =   plataforma['Boton_Login']
        self.input_loteria              =   plataforma['Input_Loteria']
        self.input_sorteo               =   plataforma['Input_Sorteo']
        self.Seleccionar_Loteria        =   plataforma['Seleccionar_Loteria']
        self.Loteria_que_se_selecciono  =   plataforma['Loteria_que_se_selecciono']
        self.Input_premio               =   plataforma['Input_premio']

        self.Input_premio1              =   plataforma['Input_premio_Nu1']
        self.Input_premio2              =   plataforma['Input_premio_Nu2']
        self.Input_premio3              =   plataforma['Input_premio_Nu3']

        self.boton_premiar              =   plataforma['Boton_Premiar']
        self.Input_fecha                =   plataforma['Input_fecha']
        self.plataforma_url_premios     =   plataforma['URL']+plataforma['URL_PREMIOS']

        self.plataforma_user            =   user['USER']
        self.plataforma_pass            =   user['PASS']


        print("Se Instancio una nueva clase Para Premiar")

    def Navegador(self):
        self.chrome_options = webdriver.ChromeOptions()
        self.chrome_options.add_experimental_option('excludeSwitches', ['enable-automation'])
        self.chrome_options.accept_insecure_certs=True
        #self.chrome_options.add_argument("--headless") #!QUITAR ESTO
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


    def buscar_loterias(self):
        try:

            self.driver.get(self.plataforma_url_premios)
            time.sleep(5)
            #COLOCAR FECHA
            input_fecha = self.driver.find_element(by=By.XPATH, value=self.Input_fecha );self.driver.implicitly_wait(20)
            input_fecha.send_keys(self.fecha)
            time.sleep(5)

            #COLOCAR LOTERIA
            input_loteria = self.driver.find_element(by=By.XPATH, value=self.input_loteria );self.driver.implicitly_wait(20)
            input_loteria.send_keys(self.loteria)
            time.sleep(3)

            #COLOCAR SORTEO
            input_sorteo = self.driver.find_element(by=By.XPATH, value=self.input_sorteo );self.driver.implicitly_wait(20)
            input_sorteo.send_keys(self.sorteo)
            time.sleep(3)

            #SELECCIONAR LOTERIA
            input_seleccionar_loteria = self.driver.find_element(by=By.XPATH, value=self.Seleccionar_Loteria );self.driver.implicitly_wait(20)
            input_seleccionar_loteria.click()
            time.sleep(3)

            #LOTERIA SELECIONADA
            Loteria_que_se_selecciono = self.driver.find_element(by=By.XPATH, value=self.Loteria_que_se_selecciono ).text;self.driver.implicitly_wait(20)

            #VALIDAR QUE SEA LA LOTERIA CORRECTA
            if(Loteria_que_se_selecciono.endswith(self.sorteo)):
                if(self.MODALIDAD == MODALIDAD):
                    return self.colocar_picks()
                elif(self.MODALIDAD == MODALIDAD_RD):
                    return self.colocar_tradicionales()
            else:
                return False

        except:
            return False

    def colocar_picks(self):
        try:
            #! AGREGAR SI LA LOTERIA ESTA PREMIADA is_enabled()
            input_numeros_ganadores = self.driver.find_element(by=By.XPATH, value=self.Input_premio );self.driver.implicitly_wait(20)
            input_numeros_ganadores.send_keys(self.numeros_ganadores)
            time.sleep(3)
            boton_premiar = self.driver.find_element(by=By.XPATH, value=self.boton_premiar );self.driver.implicitly_wait(20)
            boton_premiar.click()
            time.sleep(4)
            print(f"SE PREMIO CORRECTAMENTE... LOTERIA => : {self.loteria} SORTEO => : {self.sorteo}")
            return True
        except:
            return False

    def colocar_tradicionales(self):
        try:
            #! AGREGAR SI LA LOTERIA ESTA PREMIADA is_enabled()
            input_numero_1 = self.driver.find_element(by=By.XPATH, value=self.Input_premio1 );self.driver.implicitly_wait(20)
            input_numero_1.send_keys(self.numeros_ganadores['NU1'])
            time.sleep(2)

            input_numero_2 = self.driver.find_element(by=By.XPATH, value=self.Input_premio2 );self.driver.implicitly_wait(20)
            input_numero_2.send_keys(self.numeros_ganadores['NU2'])
            time.sleep(2)

            input_numero_3 = self.driver.find_element(by=By.XPATH, value=self.Input_premio3 );self.driver.implicitly_wait(20)
            input_numero_3.send_keys(self.numeros_ganadores['NU3'])
            time.sleep(2)

            boton_premiar = self.driver.find_element(by=By.XPATH, value=self.boton_premiar );self.driver.implicitly_wait(20)
            boton_premiar.click()
            time.sleep(4)
            print(f"SE PREMIO CORRECTAMENTE... LOTERIA => : {self.loteria} SORTEO => : {self.sorteo}")
            return True
        except:
            return False


    def publicar(self,loteria):
        self.loteria            =   loteria['loteria']
        self.sorteo             =   loteria['sorteo']
        self.fecha              =   loteria['fecha']
        self.numeros_ganadores  =   loteria['numeros_ganadores']
        self.MODALIDAD          =   loteria['MODALIDAD']

        try:
            self.Navegador()
            self.iniciar_seccion()
            saber_premio = self.buscar_loterias()
            if(saber_premio):
                #SE PREMIO CORRECTAMENTE
                self.driver.quit()
                return True
            else:
                self.driver.quit()
                return False
        except:
            return False


