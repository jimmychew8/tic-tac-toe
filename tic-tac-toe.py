
# A basic tictac toe game against the computer 
# July 2015 
#-------------------------------------------------------------------------------

#to generate computer move 
from random import randint 
#to end game 
import sys

#global matrix value that will serve as tic-tac-toe grid 
matrix = [[" "," "," "],[" "," "," "],[" "," "," "]]

#returns user input for row position
def PlacementX():
    while True: 
    	# asks the user to pick a ROW to move in, and checks to see if user has specified a row, 
    	# asks the user until he/she types a form of top, middle, or bottom. 

    	row = raw_input("Please enter row: 'top', 'middle', 'bottom':") 

    	#gets rid of spaces and uppercase letters 
    	r = row.strip().lower() 

    	# checks to see if user has specified a row 
    	if r in ['top', 'middle', 'bottom'] :  
    		break
    	else:
    		print "Please type: top, middle, or bottom."

    # returns coordinate values based on the user input for row position 
    if r in ["bottom"]: 
    	x = 2
    	return x
    elif r in ["middle"]:
    	x = 1
    	return x
    elif r in ["top"]:
    	x = 0
    	return x

#returns user input for column position
def PlacementY(): 
	# asks the user to pick a COLUMN to move in, and checks to see if user has specified a column, 
    # asks until the user inputs some form of left, middle, or right. 

	while True: 
		column = raw_input("Please enter column 'left, middle, right':")
		c = column.strip().lower()
		if c in ['left', 'middle', 'right']:
			break
		else:
			print "Please type: top, middle, or bottom."

	#returns the user input 
	if c in ["left"]:
	    y = 0
	    return y
	elif c in ["middle"]:
	    y = 1
	    return y
	elif c in ["right"]:
		y = 2
		return y


#handles a one complete turn (users move, then computer's move), and checks for a win 
def move(x):
	turn = x
	while True: 
		#gets the position of the user and stores the row as x, and the column as y 
		x,y = PlacementX(), PlacementY() 

		#checks to see if the user's move is not already taken, if not moves the user 
		#to that position 

		if matrix[x][y] == " ": 
			matrix[x][y] = "X"
			break
		else: 
			print "Spot taken"

	# handles the move for the computer 
	if turn < 4: 
		while True:
			#generates random coordinates for the computer 
			#only adds a move if the spot is not taken 
			a,b = randint(0,2), randint(0,2)

			if matrix[a][b] == " ":
				matrix[a][b] = "O"
				break
	else: #evaluates the case of a draw if the board is full 
		if check() == 1:
			print "Draw"

	#otherwise, checks for a win 
	check()

	#prints board 
	for row in matrix:
		print row


#defining conditions for a win
def check():
	if matrix[0][0] == matrix[0][1] == matrix[0][2] != " " or \
	matrix[1][0] == matrix[1][1] == matrix[1][2] != " " or \
	matrix[2][0] == matrix[2][1] == matrix[2][2] != " " or \
	matrix[0][0] == matrix[1][0] == matrix[2][0] != " " or \
	matrix[0][1] == matrix[1][1] == matrix[1][2] != " " or \
	matrix[0][2] == matrix[1][2] == matrix[2][2] != " " or \
	matrix[0][0] == matrix[1][1] == matrix[2][2] != " " or \
	matrix[0][2] == matrix[1][1] == matrix[2][0] != " ": 
		print "Game Over!"
		sys.exit(0)
	else: 
		return 1


#runs game 
def main():
	for x in range(0,5):
		move(x)

if __name__ == '__main__': 
	main()
