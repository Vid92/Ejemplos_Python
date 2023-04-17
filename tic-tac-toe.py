# Juego gato, version sencilla
# Jugador 1 = X 
# Jugador 2 = O
# Tabla: Cada jugador escoge el número donde se colocara su ficha
#
#		| 1 | 2 | 3 |
#		| 4 | 5 | 6 |
#		| 7 | 8 | 9 |
#

class tictactoe:
	def __init__(self):
		self.flag = True
		self.prev_flag = True
		self.flag_repite = False
		self.board_tic_tac_toe = [1,2,3,4,5,6,7,8,9]
		self.count = 0
		self.process()

	def board(self,pos,sim):
		pos = int(pos)
		simbol = sim
		self.flag_repite = False
		if pos in self.board_tic_tac_toe:
			self.board_tic_tac_toe[pos-1] = simbol
		else:
			self.flag_repite = True

		result = "| "+str(self.board_tic_tac_toe[0])+" | "+str(self.board_tic_tac_toe[1])+" | "+str(self.board_tic_tac_toe[2])+" |\n"\
		+"| "+str(self.board_tic_tac_toe[3])+" | "+str(self.board_tic_tac_toe[4])+" | "+str(self.board_tic_tac_toe[5])+" |\n"\
		+"| "+str(self.board_tic_tac_toe[6])+" | "+str(self.board_tic_tac_toe[7])+" | "+str(self.board_tic_tac_toe[8])+" |\n"
		return result

	def process(self):
		while self.count<9:
			self.count +=1
			if self.prev_flag:
				jugador = "Jugador 1"
				simbol = 'X'
				flag = False
			else:
				jugador = "Jugador 2"
				simbol = 'O'
				flag = True
			try:
				player = input("Ingrese posicion para "+jugador+" :")
				print(self.board(player,simbol))
			except:
				self.flag_repite = True
				while self.flag_repite:
					try:
						player = input("Ingrese otra posicion o valor aceptable para "+jugador+" :")
						print(self.board(player,simbol))
					except:
						print("Otro valor")

			self.prev_flag = flag

			if (self.board_tic_tac_toe[0] == "X" and self.board_tic_tac_toe[1] == "X" and self.board_tic_tac_toe[2] == "X")or\
				(self.board_tic_tac_toe[3] == "X" and self.board_tic_tac_toe[4] == "X" and self.board_tic_tac_toe[5] == "X")or\
				(self.board_tic_tac_toe[6] == "X" and self.board_tic_tac_toe[7] == "X" and self.board_tic_tac_toe[8] == "X")or\
				(self.board_tic_tac_toe[0] == "X" and self.board_tic_tac_toe[3] == "X" and self.board_tic_tac_toe[6] == "X")or\
				(self.board_tic_tac_toe[1] == "X" and self.board_tic_tac_toe[4] == "X" and self.board_tic_tac_toe[7] == "X")or\
				(self.board_tic_tac_toe[2] == "X" and self.board_tic_tac_toe[5] == "X" and self.board_tic_tac_toe[8] == "X")or\
				(self.board_tic_tac_toe[0] == "X" and self.board_tic_tac_toe[4] == "X" and self.board_tic_tac_toe[8] == "X")or\
				(self.board_tic_tac_toe[2] == "X" and self.board_tic_tac_toe[4] == "X" and self.board_tic_tac_toe[6] == "X"):
				print("Gana Jugador 1")
				return "Gana Jugador 1"
				#break
			elif (self.board_tic_tac_toe[0] == "O" and self.board_tic_tac_toe[1] == "O" and self.board_tic_tac_toe[2] == "O")or\
				(self.board_tic_tac_toe[3] == "O" and self.board_tic_tac_toe[4] == "O" and self.board_tic_tac_toe[5] == "O")or\
				(self.board_tic_tac_toe[6] == "O" and self.board_tic_tac_toe[7] == "O" and self.board_tic_tac_toe[8] == "O")or\
				(self.board_tic_tac_toe[0] == "O" and self.board_tic_tac_toe[3] == "O" and self.board_tic_tac_toe[6] == "O")or\
				(self.board_tic_tac_toe[1] == "O" and self.board_tic_tac_toe[4] == "O" and self.board_tic_tac_toe[7] == "O")or\
				(self.board_tic_tac_toe[2] == "O" and self.board_tic_tac_toe[5] == "O" and self.board_tic_tac_toe[8] == "O")or\
				(self.board_tic_tac_toe[0] == "O" and self.board_tic_tac_toe[4] == "O" and self.board_tic_tac_toe[8] == "O")or\
				(self.board_tic_tac_toe[2] == "O" and self.board_tic_tac_toe[4] == "O" and self.board_tic_tac_toe[6] == "O"):
				print("Gana Jugador 2")
				return "Gana Jugador 2"
				#break

		if self.count == 9:
			print("Juego empatado")
			return "Juego Empatado"

if __name__ == "__main__":
	print("main")
	tictactoe()
