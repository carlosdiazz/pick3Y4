from Funciones_Especiales import fecha, CONSULTAR_NUMEROS_API, saber_sorteo

from Datos_Loterias.DATOS_PLATAFORMA import PLATAFORMA_MEGA, user_desarrollo
from PUBLICAR_ORKAPI import PUBLICAR_EN_LOTENET_PICK

class PREMIAR_PICKS():
    
    def __init__(self, obj):
        self.loteria = obj['LOTERIA']
        self.sorteo = obj['SORTEO']

    def buscar(self):
        #? Con esta funcion buscare los numeros ganadores
        #! ? VALIDAR DATOS DESDE AQUI LA FECHA VALIDAR PREMIAR PICK #3Y PICK $4
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

            publicar_P3 = PUBLICAR_EN_LOTENET_PICK(user_desarrollo, PLATAFORMA_MEGA ).publicar(arrp3)
            publicar_P4 = PUBLICAR_EN_LOTENET_PICK(user_desarrollo, PLATAFORMA_MEGA ).publicar(arrp4)
            if(publicar_P3 and publicar_P4):
                print(f"SE PREMIO CORRECTAMENTE LA LOTERIA: {self.loteria }CON EL SORTEO: {self.sorteo}")
            else:
                print(f"NOOOOOOOO SE PREMIO LA LOTERIA: {self.loteria }CON EL SORTEO: {self.sorteo}")

        else:
            print(f"NO SE PREMIO ESTA LOTERIA: {self.loteria} COn este sorteo {self.sorteo}")