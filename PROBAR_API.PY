from API_USA import API
from Datos_Loterias.FLORIDA_AM import FLORIDA_LOTTERY_USA_AM
from Datos_Loterias.NY_AM import NEW_YORK_TARDE_LOTTERYUSA
from Datos_Loterias.FLORIDA_PM_ import FLORIDA_LOTTERY_USA_PM


FL_AM=(API().devolver_numeros(FLORIDA_LOTTERY_USA_AM))
FL_PM=(API().devolver_numeros(FLORIDA_LOTTERY_USA_PM))
NY_AM=(API().devolver_numeros(NEW_YORK_TARDE_LOTTERYUSA))


print("-----------")

print(FL_AM)
print(FL_PM)
print(NY_AM)