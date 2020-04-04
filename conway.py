# Simple implementation of Conway's game of life
import random, time, copy
print('Enter width: ')
WIDTH = int(input())
print('Enter height: ')
HEIGHT = int(input())
print('how many cycles? ')
CYCLES = int(input())

# Creating and populating a 2D list with random zeros and ones
nextCells = []
for j in range(WIDTH):
	column = []
	for i in range(HEIGHT):
		if random.randint(0,1) == 0:	
			column.append('#')
		else:
			column.append(' ')
	nextCells.append(column)

currentCells = copy.deepcopy(nextCells)

# Defining the function that sets the rules of the game
def CalculateNextCell(currentCells):
	
# Creating and populating an empty 2D list with random zeros and ones
	NewCells = []
	for j in range(WIDTH):
		column = []
		for i in range(HEIGHT):
			if random.randint(0,1) == 0:	
				column.append(' ')
			else:
				column.append(' ')
		NewCells.append(column)

	for alpha in range(WIDTH):
		
		for beta in range(HEIGHT):

			leftCoord = (alpha-1) % WIDTH
			rightCoord = (alpha+1) % WIDTH
			aboveCoord = (beta-1) % HEIGHT
			belowCoord = (beta+1) % HEIGHT
			
			numLivingNeighbors = 0
			if currentCells[leftCoord][aboveCoord]=='#':
				numLivingNeighbors += 1
			if currentCells[alpha][aboveCoord]=='#':
				numLivingNeighbors += 1
			if currentCells[rightCoord][aboveCoord]=='#':
				numLivingNeighbors += 1
			if currentCells[leftCoord][beta]=='#':
				numLivingNeighbors += 1
			if currentCells[rightCoord][beta]=='#':
				numLivingNeighbors += 1
			if currentCells[leftCoord][belowCoord] =='#':
				numLivingNeighbors += 1
			if currentCells[alpha][belowCoord] =='#':
				numLivingNeighbors += 1
			if currentCells[rightCoord][belowCoord] =='#':
				numLivingNeighbors += 1
			
# Setting the rules:
			if currentCells[alpha][beta]=='#' and (numLivingNeighbors==2 or numLivingNeighbors==3):
				NewCells[alpha][beta]='#'
			elif currentCells[alpha][beta]==' ' and numLivingNeighbors==3:
				NewCells[alpha][beta]='#'
			else:
				NewCells[alpha][beta]=' '


	
	return NewCells
	


# iterates over cycles, updating currentCells by calling the above defined function
for k in range(CYCLES):
	print('\n')
	print('Cycle: '+str(k))
	# Print current cell on the screen
	for p in range(HEIGHT):
		for q in range(WIDTH):
			print(currentCells[q][p],end='')
		print() #this is a new line at the end of a row

	currentCells=CalculateNextCell(currentCells)
	
