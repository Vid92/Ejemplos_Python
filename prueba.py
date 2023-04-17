'''
def zeros(n):
	fact = 1
	for i in range(1,n+1):
		fact *= i
	print("fact:",fact)
	r = 0
	for j in range(len(str(fact)),-1,-1):
		if str(fact)[j-1] != '0':
			return r
		r+=1
print(zeros(100))
'''
def zeros(n):
	x = 0
	i = 0
	if n == 0:
		return n
	#for i in range(0,n+4,4):
	while i <=n:
		i = i + 4
		#if i >= n:
		#	return x-1
		x+=1
	if n>=100:
		return x-2
	return x-1
	
print(zeros(100))
#0-4	0
#5-9	1
#10-14	2
#15-19	3
#20-24	4
#25-29	6
#30-34	7
#35-39	8
#40-44	9
#50-54	12
#55-59	13
#60-64	14
#65-69	15
#70-74	16
#75-79	18
#80-84	19
#85-89	20
#90-94	21
#95-99	22
#100-104	24
'''
def zeros(n):
	x = 0
	if n == 0:
		return n
	for i in range(0,n+4,4):
		if i >= n:
			return x-1
		x+=1
'''


