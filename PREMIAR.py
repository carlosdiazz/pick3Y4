from re import M
import time
from VARIABLES import MODALIDAD, MODALIDAD_RD
from Funciones_Especiales import fecha, CONSULTAR_NUMEROS_API, saber_sorteo, sendNotification, Convertir_nombre_loteria, Convertir_nombre_sorteo, Response
from PUBLICAR_EN_LOTENET import PUBLICAR_EN_LOTENET
from config import BOT_PREMIAR as BOT_MEGA, INTENTOS, TIEMPO_A_ESPERAR, URL_API_NODE_LAMERICANA, URL_API_NODE_LDOMINICANA
class PREMIAR():

    def __init__(self, obj, PLATAFORMA, USER):
        self.loteria            =   obj['LOTERIA']
        self.sorteo             =   obj['SORTEO']
        self.MODALIDAD          =   obj['MODALIDAD']
        self.USER_PLATAFORMA    =   USER
        self.PLATAFORMA         =   PLATAFORMA
        print('-------- Se Instancio una clase Para premiar en plataformas ---------')

    def PUBLICAR_PICK3(self):
        OBJ_3 = {
                'loteria'           :   'PICK 3',
                'fecha'             :   self.loteria_a_publicar['fecha'],
                "sorteo"            :   self.loteria_a_publicar['loteria'] +" "+saber_sorteo(self.loteria_a_publicar['sorteo']),
                'numeros_ganadores' :   self.loteria_a_publicar['numeros_ganadores']['PICK3'],
                'MODALIDAD'         :   self.MODALIDAD
                }
        return PUBLICAR_EN_LOTENET(self.USER_PLATAFORMA, self.PLATAFORMA ).publicar(OBJ_3)


    def PUBLICAR_PICK4(self):
        arrp4 = {
                'loteria'           :   'PICK 4',
                'fecha'             :   self.loteria_a_publicar['fecha'],
                "sorteo"            :   self.loteria_a_publicar['loteria'] +" "+saber_sorteo(self.loteria_a_publicar['sorteo']),
                'numeros_ganadores' :   self.loteria_a_publicar['numeros_ganadores']['PICK4'],
                'MODALIDAD'         :   self.MODALIDAD
            }
        return PUBLICAR_EN_LOTENET(self.USER_PLATAFORMA, self.PLATAFORMA ).publicar(arrp4)


    def PUBLICAR_TRADICIONALES(self):
        tradicionales = {
                'loteria'           :   Convertir_nombre_loteria(self.PLATAFORMA['NAME'],self.loteria),
                'fecha'             :   self.loteria_a_publicar['fecha'],
                "sorteo"            :   Convertir_nombre_sorteo(self.PLATAFORMA['NAME'], self.sorteo, self.loteria),
                'numeros_ganadores' :   self.loteria_a_publicar['numeros_ganadores'],
                'MODALIDAD'         :   self.MODALIDAD
            }
        return PUBLICAR_EN_LOTENET(self.USER_PLATAFORMA, self.PLATAFORMA ).publicar(tradicionales)


    def premiar(self):

        print(f'SE ESTA INICIALIZANDO LA PREMIACION DE PLATAFORMAS PARA {self.loteria} {self.sorteo}')
        #? Con esta funcion buscare los numeros ganadores
        pick_3_premiar = False
        pick_4_premiar = False
        premios_dominicanos = False
        message = ''
        message_picks = ''
        self.fecha = fecha('%d-%m-%Y')

        if(self.MODALIDAD == MODALIDAD):
                self.URI_PETICION = URL_API_NODE_LAMERICANA
        elif(self.MODALIDAD == MODALIDAD_RD):
            self.URI_PETICION = URL_API_NODE_LDOMINICANA

        for intentos in range(INTENTOS):

            CONSULTA = CONSULTAR_NUMEROS_API(self.URI_PETICION,self.loteria,self.sorteo,self.fecha)

            if(CONSULTA['ERROR'] == False):

                if(CONSULTA['NUMEROS']):
                    self.loteria_a_publicar = CONSULTA['NUMEROS']

                    if(self.MODALIDAD == MODALIDAD):

                        if(pick_3_premiar == False):
                            publicar_pick_3 = self.PUBLICAR_PICK3()
                            if(publicar_pick_3['StatusError'] == False and publicar_pick_3['Status'] == True):
                                message_picks += publicar_pick_3['Message']
                                pick_3_premiar = True
                            else:
                                message = publicar_pick_3['Message']
                                print(message)

                        if(pick_4_premiar == False):
                            publicar_pick_4 = self.PUBLICAR_PICK4()
                            if(publicar_pick_4['StatusError'] == False and publicar_pick_4['Status'] == True):
                                message_picks += publicar_pick_4['Message']
                                pick_4_premiar = True
                            else:
                                message = publicar_pick_4['Message']
                                print(message)


                        if(pick_3_premiar and pick_4_premiar):
                            message_enviar = f'SE PREMIO CORRECTAMENTE EN PLATAFORMA: {self.PLATAFORMA["NAME"]}\n\nLOTERIA: {self.loteria}\n\nSORTEO: {self.sorteo} \n\nFECHA: {self.fecha}\n\nMESSAGE:\n\n{message_picks}'
                            print(message_enviar)
                            sendNotification(False, message_enviar, BOT_MEGA['TOKEN'] )
                            break
                        else:
                            print('UNO DE LOS PICKS NO SE PREMIO SE INTENTARA DE NUEVO')
                            time.sleep(TIEMPO_A_ESPERAR)

                    elif(self.MODALIDAD == MODALIDAD_RD):

                        if(premios_dominicanos == False):
                            premiar_dominicanos =self.PUBLICAR_TRADICIONALES()
                            if(premiar_dominicanos['StatusError'] == False and premiar_dominicanos['Status'] == True):
                                message_picks = premiar_dominicanos['Message']
                                premios_dominicanos = True
                            else:
                                message = premiar_dominicanos['Message']
                                print(message)

                        if(premios_dominicanos):
                            message_a_enviar = f'SE PREMIO CORRECTAMENTE EN PLATAFORMA: {self.PLATAFORMA["NAME"]} \n\nLOTERIA: {self.loteria}\n\nSORTEO: {self.sorteo} \n\nFECHA: {self.fecha} \n\nMESSAGE:\n\n{message_picks}'
                            print(message_a_enviar)
                            sendNotification(False, message_a_enviar, BOT_MEGA['TOKEN'] )
                            break
                        else:
                            print("PREMIOS DOMINICANO NO SE PREMIO SE INTETARA DE NUEVO")
                            time.sleep(TIEMPO_A_ESPERAR)
                    else:
                        print("NO DEBERIA DE LLEGAR AQUI ES UNA NUEVA MODALIDAD DE NUEMROS")
                        time.sleep(TIEMPO_A_ESPERAR)
                else:
                    message = CONSULTA['MESSAGE']
                    print(message + f' INTENTOS #: {intentos}')
                    time.sleep(TIEMPO_A_ESPERAR)
            else:
                message = CONSULTA['MESSAGE']
                print(message + f' INTENTOS #: {intentos}')
                time.sleep(TIEMPO_A_ESPERAR)

        if(self.MODALIDAD == MODALIDAD):
            if(pick_3_premiar == False or pick_4_premiar == False):
                message_a_enviar = f'\n\nNO SE PREMIO\n\nEN PLATAFORMA: {self.PLATAFORMA["NAME"]}\n\nLOTERIA: {self.loteria} \n\nSORTEO: {self.sorteo} \n\nERROR: {message}'
                sendNotification(True, message_a_enviar, BOT_MEGA['TOKEN'])

        elif(self.MODALIDAD == MODALIDAD_RD):
            if(premios_dominicanos == False):
                message_a_enviar = f'\n\nNO SE PREMIO\n\nEN PLATAFORMA: {self.PLATAFORMA["NAME"]}\n\nLOTERIA: {self.loteria} \n\nSORTEO: {self.sorteo} \n\nERROR: {message}'
                sendNotification(True, message_a_enviar, BOT_MEGA['TOKEN'])

