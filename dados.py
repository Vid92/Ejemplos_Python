# Juego lanzamiento de dados(Elige entre 1 dado o dos)
# Resultados al azar
# Ejercicio sencillo
#
# Ejemplo de resultados:
#	Un dado:
#		| 3 |
#
#	Dos dados:
#		| 5 | 1 |
#

import random

def dados():
	while True:
		game = input("Elige entre 1 o 2 dados: ")
		if game == '1':
			return "| "+str(random.randrange(1,7))+" | "
		elif game == '2':
			return "| "+str(random.randrange(1,7))+" | "+str(random.randrange(1,7))+" | "

print(dados())
