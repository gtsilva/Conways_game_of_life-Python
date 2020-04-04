# Simple implementation of Conway's game of life
# Implementation using binary integers

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
			column.append(0)
		else:
			column.append(1)
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
				column.append(0)
			else:
				column.append(0)
		NewCells.append(column)

	for alpha in range(WIDTH):
		
		for beta in range(HEIGHT):

			leftCoord = (alpha-1) % WIDTH
			rightCoord = (alpha+1) % WIDTH
			aboveCoord = (beta-1) % HEIGHT
			belowCoord = (beta+1) % HEIGHT
			
			numLivingNeighbors = 0
			if currentCells[leftCoord][aboveCoord]==1:
				numLivingNeighbors += 1
			if currentCells[alpha][aboveCoord]==1:
				numLivingNeighbors += 1
			if currentCells[rightCoord][aboveCoord]==1:
				numLivingNeighbors += 1
			if currentCells[leftCoord][beta]==1:
				numLivingNeighbors += 1
			if currentCells[rightCoord][beta]==1:
				numLivingNeighbors += 1
			if currentCells[leftCoord][belowCoord] ==1:
				numLivingNeighbors += 1
			if currentCells[alpha][belowCoord] ==1:
				numLivingNeighbors += 1
			if currentCells[rightCoord][belowCoord] ==1:
				numLivingNeighbors += 1
			
# Setting the rules:
			if currentCells[alpha][beta]==1 and (numLivingNeighbors==2 or numLivingNeighbors==3):
				NewCells[alpha][beta]=1
			elif currentCells[alpha][beta]==0 and numLivingNeighbors==3:
				NewCells[alpha][beta]=1
			else:
				NewCells[alpha][beta]=0


	
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
	time.sleep(0.1) #for visualization purposes
	
