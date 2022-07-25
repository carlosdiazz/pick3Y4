import time
from Funciones_Especiales import fecha, CONSULTAR_NUMEROS_API, saber_sorteo, sendNotification
from Datos_Loterias.DATOS_PLATAFORMA import PLATAFORMA_MEGA, user_desarrollo
from PUBLICAR_ORKAPI import PUBLICAR_EN_LOTENET_PICK
from config import BOT_PREMIAR_MEGALOTTERY as BOT_MEGA, INTENTOS, TIEMPO_A_ESPERAR
class PREMIAR():

    def __init__(self, obj):
        self.loteria            =   obj['LOTERIA']
        self.sorteo             =   obj['SORTEO']
        print('SE Instancio una clase Para premiar PICKS ---')

    def PUBLICAR_PICK3(self):
        OBJ_3 = {
                'loteria'           :   'PICK 3',
                'fecha'             :   self.loteria_a_publicar['fecha'],
                "sorteo"            :   self.loteria_a_publicar['loteria'] +" "+saber_sorteo(self.loteria_a_publicar['sorteo']),
                'numeros_ganadores' :   self.loteria_a_publicar['numeros_ganadores']['PICK3']
                }
        return PUBLICAR_EN_LOTENET_PICK(user_desarrollo, PLATAFORMA_MEGA ).publicar(OBJ_3)


    def PUBLICAR_PICK4(self):
        arrp4 = {
                'loteria'           :   'PICK 4',
                'fecha'             :   self.loteria_a_publicar['fecha'],
                "sorteo"            :   self.loteria_a_publicar['loteria'] +" "+saber_sorteo(self.loteria_a_publicar['sorteo']),
                'numeros_ganadores' :   self.loteria_a_publicar['numeros_ganadores']['PICK4']
            }
        return PUBLICAR_EN_LOTENET_PICK(user_desarrollo, PLATAFORMA_MEGA ).publicar(arrp4)


    def premiar(self): #COntrolar desde aqui la diferente manera de premiar loteria dominicana y amaericana

        print(f'SE ESTA INICIALIZANDO LA PREMIACION DE PLATAFORMAS PARA {self.loteria} {self.sorteo}')
        #? Con esta funcion buscare los numeros ganadores
        pick_3_premiar = False
        pick_4_premiar = False
        message = ''
        for intentos in range(INTENTOS):

            self.fecha = fecha('%d-%m-%Y') #! ? VALIDAR DATOS DESDE AQUI LA FECHA VALIDAR PREMIAR PICK #3Y PICK $4 --------------------------------------
            CONSULTA = CONSULTAR_NUMEROS_API(self.loteria,self.sorteo,self.fecha)

            if(CONSULTA['ERROR'] == False):

                if(CONSULTA['NUMEROS']):
                    self.loteria_a_publicar = CONSULTA['NUMEROS']

                    if(pick_3_premiar == False):
                        pick_3_premiar = self.PUBLICAR_PICK3()

                    if(pick_4_premiar == False):
                            pick_4_premiar = self.PUBLICAR_PICK4()

                    if(pick_3_premiar and pick_4_premiar):
                        message = f'SE PREMIO CORRECTAMENTE \n\nLOTERIA: {self.loteria}\n\nSORTEO: {self.sorteo} \n\nFECHA: {self.fecha}'
                        print(message)
                        sendNotification(message, BOT_MEGA['TOKEN'] )
                        break

                else:
                    message = CONSULTA['MESSAGE']
                    print(message + f' INTENTOS #: {intentos}')
                    time.sleep(TIEMPO_A_ESPERAR)
            else:
                message = CONSULTA['MESSAGE']
                print(message + f' INTENTOS #: {intentos}')
                time.sleep(TIEMPO_A_ESPERAR) #! AGREGA MAS TIEMPO AQUI

        if(pick_3_premiar == False or pick_4_premiar == False):
            message_a_enviar = f'NO SE PREMIO EN PLATAFORMA \n\nLOTERIA: {self.loteria} \n\nSORTEO: {self.sorteo} \n\nERROR: {message}'
            sendNotification(message_a_enviar, BOT_MEGA['TOKEN'])

