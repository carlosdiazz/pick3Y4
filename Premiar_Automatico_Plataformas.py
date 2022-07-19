import schedule
import VARIABLES
from PUBLICAR_NUMEROS import Publicar_En_Plataformas
from Funciones_Especiales import fecha, run
import time

from Datos_Loterias.DATOS_PLATAFORMA import PLATAFORMA_TODO

user = {
    'USER':'bot@pick',
    'PASS':'951951'
}

loteria_prueba = {
    'loteria'           : 'FLORIDA',
    'sorteo'            : "Hola",
    'numeros_ganadores' :'numeros_ganadores'
}


prueba = Publicar_En_Plataformas(user, PLATAFORMA_TODO,loteria_prueba).publicar()


#prueba = ''
#
#
##!AGREGAR ALGO PARA BORRAR PANTALLA O LIMPIAR CACHE AL INIICO DE CADA DIA
#
#hora_prueba =  '23:12:00'
#
###! HORARIO DE BUSCAR NUMEROS
#schedule.every().day.at(hora_prueba).do(run, prueba)
#
#while True:
#    fecha_actual = fecha('%d-%m-%Y || %H:%M:%S')
#    print(f"|----------> {fecha_actual} <----------|")
#    saber = schedule.run_pending()
#    if(saber == None):
#        pass
#    else:
#        print(schedule.run_pending())
#    time.sleep(1)