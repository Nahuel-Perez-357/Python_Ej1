from random import choice, randrange
from datetime import datetime

# Operadores posibles
operators = ["+", "-","*","/"] #MOD
# Cantidad de cuentas a resolver
times = 5
# Contador inicial de tiempo.
# Esto toma la fecha y hora actual.
init_time = datetime.now()
cant_Correct = 0
cant_Incorrect = 0
print(f"¡Veremos cuanto tardas en responder estas {times} operaciones!")
for i in range(0, times):
	# Se eligen números y operador al azar
	number_1 = randrange(10)
	number_2 = randrange(10)
	operator = choice(operators)
	# Se imprime la cuenta
	if operator == "/":
		while number_2 == 0:
			number_2 = randrange(10)
	print(f"{i+1}- ¿Cuánto es {number_1} {operator} {number_2}?")
	if operator == "+": #MOD
		print("dentro del operador +")
		Res = (number_1) + (number_2)
	elif operator == "-":
		print("dentro del operador -")
		Res = (number_1) - (number_2)
	elif operator == "*":
		print("dentro del operador *")
		Res = (number_1) * (number_2)
	else: 
		print("dentro del operador /")
		Res = int ((number_1) / (number_2))
	# Le pedimos al usuario el resultado
	result = int(input("resultado: "))#MOD
	if result == Res:#MOD
		print("CORRECTO")
		cant_Correct = cant_Correct + 1
	else:
		print("INCORRECTO")
		cant_Incorrect = cant_Incorrect + 1
# Al terminar toda la cantidad de cuentas por resolver.
# Se vuelve a tomar la fecha y la hora.
end_time = datetime.now()
# Restando las fechas obtenemos el tiempo transcurrido.
total_time = end_time - init_time
# Mostramos ese tiempo en segundos.
print(f"\n Tardaste {total_time.seconds} segundos.")
print(f"\ Correctos {cant_Correct} Incorrectos {cant_Incorrect}") #MOD
