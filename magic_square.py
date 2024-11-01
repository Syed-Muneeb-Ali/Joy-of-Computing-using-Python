# Python program to generate odd sized magic squares

def generateSquare(n):

	# 2-D array with all
	# slots set to 0
	magicSquare = [ [0 for x in range(n)] for y in range(n)]

	# initialize position of 1
	i = n // 2
	j = n - 1

	# Fill the magic square
	# by placing values
	num = 1
	while num <= (n * n):
		if i == -1 and j == n: # 3rd condition
			i = 0
			j = n - 2
		else:

			# next number goes out of
			# right side of square
			if j == n:
				j = 0

			# next number goes
			# out of upper side
			if i < 0:
				i = n - 1

		if magicSquare[int(i)][int(j)] != 0: # 2nd condition
			i = i + 1
			j = j - 2
			continue
		else:
			magicSquare[int(i)][int(j)] = num
			num = num + 1

		j = j + 1
		i = i - 1 # 1st condition

	# Printing magic square
	print("Magic Square for n =", n)
	print("Sum of each row or column", n*(n*n+1)//2, "\n")

	for i in range(0, n):
		for j in range(0, n):
			print('%2d ' % (magicSquare[i][j]), end='')

			# To display output
			# in matrix form
		print()

# Driver Code


# Works only when n is odd
while(True):
    n = int(input("Enter an odd number (-1 if quit) : "))
    if n == -1: break
    else: generateSquare(n)

# 1) The position of next number is calculated by decrementing row number of the previous number by 1,
# 		and incrementing the column number of the previous number by 1. At any time, if the calculated 
# 		row position becomes -1, it will wrap around to n-1. Similarly, if the calculated column position
# 		becomes n, it will wrap around to 0.

# 2) If the magic square already contains a number at the calculated position, calculated column position 
# 	will be decremented by 2, and calculated row position will be incremented by 1.

# 3) If the calculated row position is -1 & calculated column position is n, the new position would be: (0, n-2). 