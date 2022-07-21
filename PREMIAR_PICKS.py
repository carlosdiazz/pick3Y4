import time
from Funciones_Especiales import fecha, CONSULTAR_NUMEROS_API, saber_sorteo
from Datos_Loterias.DATOS_PLATAFORMA import PLATAFORMA_MEGA, user_desarrollo
from PUBLICAR_ORKAPI import PUBLICAR_EN_LOTENET_PICK

class PREMIAR_PICKS():

    def __init__(self, obj):
        self.loteria            =   obj['LOTERIA']
        self.sorteo             =   obj['SORTEO']
        self.intentos           =   0
        self.pick3_publicado    =   False
        self.pick4_publicado    =   False

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


    def buscar(self):
        #? Con esta funcion buscare los numeros ganadores

        self.fecha = fecha('%d-%m-%Y') #! ? VALIDAR DATOS DESDE AQUI LA FECHA VALIDAR PREMIAR PICK #3Y PICK $4 --------------------------------------
        CONSULTA = CONSULTAR_NUMEROS_API(self.loteria,self.sorteo,self.fecha)

        if(CONSULTA['ERROR'] == True):
            print(CONSULTA['MESSAGE'])
            self.intentos = self.intentos+1
            time.sleep(1)
            self.buscar()

        if(CONSULTA['NUMEROS']):
            self.loteria_a_publicar = CONSULTA['MESSAGE'][0] #AQUI MEL JSON QUE VIENE DE LA BASE DE DATO< CON LA FECHA, NOMBRE Y NUMEROS

            if(self.pick3_publicado == False):
                self.pick3_publicado = self.PUBLICAR_PICK3()

            if(self.pick4_publicado == False):
                self.pick4_publicado = self.PUBLICAR_PICK4()

            if(self.PUBLICAR_PICK3 and self.PUBLICAR_PICK4):
                self.intentos = 0
                self.pick3_publicado = False
                self.pick4_publicado = False
                print(f'SE PUBLICO EN LOTENET EL PICK 3 y PICK 4 de LOTERIA: {self.loteria} CON SORTEO: {self.sorteo} FECHA {self.fecha}')
                return True #! ----ME FALTA enviar NOTIFICACION TELEGRAM -------------------------------------------------------------------------------
            else:
                if(self.intentos<100):
                    print(f'NO SE PUBLICO EN LOTENET.... ESTA LOTERIA: => {self.loteria} CON SORTEO: => {self.sorteo} INTENTANDO DE NUEVO #{self.intentos}')
                    self.intentos = self.intentos+1
                    time.sleep(1)
                    self.buscar()
                else:
                    print(f'NO SE PUBLICO CON TODOS LOS INTENTOS VALIDOS EN LOTENET.... ESTA LOTERIA: => {self.loteria} CON SORTEO: => {self.sorteo} INTENTO #{self.intentos}')
                    return False #! ----ME FALTA enviar NOTIFICACION TELEGRAM -------------------------------------------------------------------------------


        else:
            print(CONSULTA['MESSAGE']+f' => LOTERIA : => {self.loteria} => SORTEO => {self.sorteo} INTENTANDO DE NUEVO #{self.intentos}')
            self.intentos = self.intentos+1
            time.sleep(1)
            self.buscar()
