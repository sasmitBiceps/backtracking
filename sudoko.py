grid = 	[[3, 0, 6, 5, 0, 8, 4, 0, 0], 
         [5, 2, 0, 0, 0, 0, 0, 0, 0], 
         [0, 8, 7, 0, 0, 0, 0, 3, 1], 
         [0, 0, 3, 0, 1, 0, 0, 8, 0], 
         [9, 0, 0, 8, 6, 3, 0, 0, 5], 
         [0, 5, 0, 0, 9, 0, 6, 0, 0], 
         [1, 3, 0, 0, 0, 0, 2, 5, 0], 
         [0, 0, 0, 0, 0, 0, 0, 7, 4], 
         [0, 0, 5, 2, 0, 6, 3, 1, 0] ]

def print_grid(grid):
	for i in range(len(grid)):

		if i!= 0 and i%3==0:
			print("-"*(len(grid[0])*2+3))
		for j in range(len(grid[0])):

			print(grid[i][j], end=" ")
			if j!=len(grid[0])-1 and j%3==2:
				print("|", end=" ")
			
		print()

def num_valid(grid, num, position): #board, number, position: tuple
	x_posi, y_posi = position
	for i in range(len(grid[0])):
		if grid[x_posi][i] == num and i != y_posi:
			return False

	for j in range(len(grid)):
		if grid[j][y_posi] == num and j != x_posi:
			return False

	box_x, box_y = x_posi//3, y_posi//3

	for i in range(box_x*3, box_x*3+3):
		for j in range(box_y*3, box_y*3+3):
			if grid[i][j] == num and (i,j) != position:
				return False

	return True


def returnZero(grid):
	for i in range(len(grid)):
		for j in range(len(grid[0])):
			if grid[i][j] == 0:
				return i,j

	return None

def solve(grid):

	zero_posi = returnZero(grid)

	if zero_posi is None:
		return True

	else:
		for i in range(1, 10):
			if(num_valid(grid, i, zero_posi)):
				grid[zero_posi[0]][zero_posi[1]] = i
				if solve(grid):
					return True
				grid[zero_posi[0]][zero_posi[1]] = 0
			
				
	return False

solve(grid)
print_grid(grid)