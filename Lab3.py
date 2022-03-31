def display(arr, rows, cols):
	pad_center = 10
	print('|'+('-'*pad_center + "|")*cols)
	for i in range(rows):
		for j in range(cols):
			print("|", end='')
			print(str(round(arr[i][j], 4)).center(pad_center), end="")
		print("|\n|", end='')
		print(('-'*pad_center + "|")*cols)
	print()

def divideByOwn(arr, x, y, cols):
	c = arr[x][y]
	for i in range(rows):
		for j in range(y, cols):
			arr[i][j] = arr[i][j]/c
		
def setColsZero(arr, x, y, rows):
	for i in range(rows):
		if i != x:
			arr[i][y] = 0
		
def squareMethod(arr, i, j, rows, cols):
		for x in range(rows):
			for y in range(cols):
				if x != i and y > j:
					arr[x][y] = arr[i][j] * arr[x][y] - arr[i][y] * arr[x][j]
				
def JordanGaussMethod(arr, rows, cols):
	for c in range(rows):
		squareMethod(arr, c, c, rows, cols)
		divideByOwn(arr, c, c, cols)
		setColsZero(arr, c, c, rows)

if __name__ == "__main__":

	# rows, cols = (int(input('кількість прикладів: ')), int(input('кількість Х:'))+1)
	# arr = [[0 for i in range(cols)] for j in range(rows)]
	
	# for i in range(rows):
	# 	print(str(i+1), ' Приклад ')
	# 	for j in range(cols):
	# 		if j == cols-1:
	# 			arr[i][j] = float(input(' = '))
	# 		else:
	# 			arr[i][j] = float(input(' Cx' + str(j+1) + ': '))
	
	#-------------------------------------------------------

	k = 0.01*2

	arr = [[(1+k), 2, 3, -2, 6],
		   [2, -0.04, -2, -3, 8*(1-k)],
		   [3, 2, -0.1, (2-k), 0.16],
		   [2, -3, 2, 1, -8*(1+3*k)]]

	arrCopy = list(map(list, arr))

	rows = len(arr)
	cols = len(arr[0])

	display(arr, rows, cols)
	JordanGaussMethod(arr, rows, cols)
	print()
	display(arr, rows, cols)

	for i in range(rows):
		print('X('+ str(i+1)+ ') = ' + str(arr[i][cols-1]))
	
	res = 0
	for i in range(rows):
		print('\n',arrCopy[i][cols-1], ' = ', end='')
		for j in range(cols-1):
			res += arrCopy[i][j] * arr[j][cols-1]
		print(res, '\t Δ = ', arrCopy[i][cols-1] - res, '\n')
		res = 0
	