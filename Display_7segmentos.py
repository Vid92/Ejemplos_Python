seven_seg = [['111','101','101','101','111'],['001','001','001','001','001'],['111','001','111','100','111'],['111','001','111','001','111'],['101','101','111','001','001'],['111','100','111','001','111'],['111','100','111','101','111'],['111','001','001','001','001'],['111','101','111','101','111'],['111','101','111','001','111']]

try:
	dato = input("Ingrese un numero entero no negativo: ")

	rep = 0
	while rep < 5:
		for n in dato:
			#print("rep:",rep)
			x = seven_seg[int(n)][rep]
			n = 0
			for i in x:
				if int(i) == 1: 
					print(' # ',end='')
				else:
					print("   ",end='')
				n+=1
				if n == 3:
					#print("\n")
					print("   ",end='')
					n = 0

		rep+=1
		print("\n")
except ValueError:
	print("Numero negativo")