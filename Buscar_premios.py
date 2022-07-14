from Funciones_Especiales import devolver_arreglo, fecha
from API_USA import API


class Buscar_Premio():

    def __init__(self, Datos):
        self.loteria = Datos['LOTERIA']
        self.sorteo = Datos['SORTEO']
        self.intentos=0

    def Buscar_numeros_ganadores(self):

        #!Crear funcion que valide que no existen en la base de datos
        if(True):
            arreglo_loteria = devolver_arreglo(self.loteria,self.sorteo)
            numeros_ganadores = API().devolver_numeros(arreglo_loteria)
            if(numeros_ganadores):
                self.intentos=0
                return {
                    'LOTERIA'       : self.loteria,
                    'SORTEO'        : self.sorteo,
                    'NUMEROS'       : numeros_ganadores,
                    'FECHA'         : fecha('%d-%m-%Y'),
                    "AGREGADO_POR"  : "BOT"
                }
            else:
                self.intentos=self.intentos+1
                if(self.intentos<150):
                    print(f"No se encontro esta loteria:{self.loteria} con este sorteo: {self.sorteo} intento #:{self.intentos}")
                    self.Buscar_numeros_ganadores()
                else:
                    print("No se encontro esta loteria")
                    return False
                    print("No se encontro esta loteria")
        else:
            print("Ya la loteria existe")
            return False

FLORIDA_AM = {
    'LOTERIA': 'FLORIDA',
    "SORTEO" : 'MIDDAY'
}

FLORIDA_PM = {
    'LOTERIA': 'FLORIDA',
    "SORTEO" : 'EVENING'
}

NY_AM = {
    'LOTERIA': 'NEW YORK',
    "SORTEO" : 'MIDDAY'
}

NY_PM = {
    'LOTERIA': 'NEW YORK',
    "SORTEO" : 'EVENING'
}

fl=(Buscar_Premio(FLORIDA_AM).Buscar_numeros_ganadores())
fl2=(Buscar_Premio(FLORIDA_PM).Buscar_numeros_ganadores())
ny=(Buscar_Premio(NY_AM).Buscar_numeros_ganadores())
ny2=(Buscar_Premio(NY_PM).Buscar_numeros_ganadores())

print('----------------------')
print(fl)
print(fl2)
print(ny)
print(ny2)