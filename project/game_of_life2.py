""" A python script that immitates Conway's Game of Life. Run on your terminal, prints to STDOUT.
.. module:: AFS505_u1 Project 
	:Platform: Unix, Windows
	:synopsis This script recieves a command line argument of life cycle generations and
	grid positions in the format row:column as such:python game_of_life.py 50 14:40 15:42 16:39 16:40 16:43 16:44 16:45
	
..moduleauthor:: EVAN STOWE evan.stowe@wsu.edu
..modulereviewer:: None, no reply from Amin.
"""
from sys import argv
script,ticks,coordinates = argv
def create_grid(seeds): 
	""" 
	Innitializes a dictionary called grid of 30 rows and 80 columns. 
	
	Parameters: 
	seeds (tuple): Coordinate pairs in the grid representing user defined ON 
	or 'seeded' cells. 
	
	Returns: 
	grid (dict): dictionary grid populated with '-' representing OFF cells
	and 'X' representing ON cells 
	""" 
	#create an empty dictionary called grid
	#populate the grid with '-' for ever position r and c in both specified ranges
	#for speficied tuples r,c in seeds, populate that position in the grid with 'X' 
	grid = {}
	for r in range(1, 31):
		for c in range(1, 81): 
			grid[r,c] = '-'		
	for r,c in seeds: 
		grid[r,c] = 'X'
		
	return grid

	
def display_grid(grid): 
	""" 
	Show grid (dict) to user via STDOUT.
	
	Parameters: 
	grid (dict): Dictionary polulated with seeded ON and OFF cells. 
	
	Returns: 
	grid_row (str): Prints the string of ON and OFF cells to the STDOUT. 
	"""
	#for all row elements in specified range assign an empty string
	#for all column elements within row elements assign them an empty string and print the entire picture to STDOUT
	for r in range(1, 31): 
		grid_row = ''
		for c in range(1,81):
			grid_row = grid_row + grid[r,c]
		print(grid_row)

def get_neighbors(r,c): 
	""" 
	Determines the neighbors for each cell in grid (dict). 
	
	Parameters: 
	r,c (tuple): Tuple of coordinates in grid (dict). 

	Returns: 
	List of tuples of all neighboring (adjacent) cells. 
	""" 
	#defines the neighbors of any interior r,c coordinate pair in terms of r,c
	return [(r-1,c-1),(r-1, c), (r-1, c+1), (r, c-1), (r, c+1), (r+1,c-1), (r+1,c), (r+1, c+1)]
	

def count_live_neighbors(r, c, grid): 
	""" 
	Determines the number of ON neighbors for each cell.
	
	Parameters: 
	r (int): Integer representing cell row position. 
	c (int): Integer representing cell column position. 
	grid (dict): Dictionary containing all possible coordinate pairs. 
	
	Returns: 
	n_live_neighbors (int): Representing all ON neighboring (adjacent) cells.
	""" 
	#sets the variable neighbors as the output of the function get_neighbors for coordinate r,c
	#sets innitial value n_live_neighbors to 0 
	#evaluates every neighbor element in list of neighbors for 'X' denoting a live neighbor, upon finding 'X' updates n_live_neighbors by +=1
	
	neighbors = get_neighbors(r, c)
	n_live_neighbors = 0 
	for neighbor in neighbors: 
		if grid[neighbor] == 'X':
			n_live_neighbors += 1
			
	return n_live_neighbors
	
		
def determine_cell_state(r, c, grid):	
	""" Determines the state of each cell in grid based on the number of ON neighbors. Essentially the 'rules' of the game.
	
	Parameters: 
	r (int): Integer representing cell row position. 
	c (int): Integer representing cell column position. 
	grid (dict): Dictionary containing all possible coordinate pairs. 
	
	Returns:
	cell_state (str): Updated cell state. 
	""" 
	#sets each initial cell state to '-' or OFF 
	#evaluates cell state defined by parameters r,c with series of if statements which define rules of 'cellular life' 
	cell_state = '-' 
	n = count_live_neighbors(r, c, grid) 
	if grid[r,c] == '-' and n == 3: 
		cell_state = 'X' 
	elif grid[r,c] == 'X' and (n == 2 or n == 3): 
		cell_state = 'X' 
	elif grid[r,c] == 'X' and (n < 2):
		cell_state = '-' 
	elif grid[r,c] == 'X' and (n > 3):
		cell_state = '-' 
	return cell_state
	
		 
def update_grid(grid): 
	""" 
	Updates grid (dict) based on the cell state determined in function determine_cell_state.
		
	Parameters: 
	grid (dict): Dictionary containing all possible coordinate pairs.  
	
	Returns: 
	updated_grid (dict): Updated dictionary (based on the determined cell state function) containing all possible coordinate pairs.  
	""" 
	#copy the dictionary grid 
	#for all interior cells defined range r and c, update the dictionary grid with the output of the function determined_cell_state
	updated_grid = grid.copy()
	for r in range(2, 30): 
		for c in range(2,80):
			updated_grid[r,c] = determine_cell_state(r, c, grid) 
			 
	return updated_grid 

def parse_input(input_string): 
	""" 
	Parses and alters the user input of ticks (generations) and seed cell coordinates for use in function 'main'. 
	
	Parameters: 
	input_string (str): String of user defined ticks (generations) and cell coordinates. 
	
	Returns: 
	tickies (int): Integer representing user defined number of ticks (generations) for the game to run. 
	coordinate_list (list): List of coordinates representing user defined seed cells. 
	"""
	#take the string of inputs recieved in function main(), split it at every space and assign it to the variable user_inputs
	#parse ticks from the string user_inputs convert it from a string variable to integer and assign it to the variable tickies
	#parse the rest of the string user_inputs that represent the coordinates defined by user and update the variable user_inputs
	#create an empty list called coordinate_list
	# for every element in user_inputs, split it by ':' 
	#and assign the first half of the element as r_string and the second as c_string while converting them from string variabels to integers
	#append the new r,c tuples to the newly created list coordinate_list 
	#user_inputs = input_string.split() 
	tickies = int(ticks)
	user_inputs = coordinates
	coordinate_list = []
	for user_input in user_inputs: 
		r_string, c_string = user_input.split(':') 
		coordinate_list.append((int(r_string), int(c_string))) 
	return (tickies, coordinate_list) 
	
	
def main():
	"""
	Prompts user for ticks (generations) and seed cells. Uses update_grid function and display_grid function in a while loop until 
	user defined number of ticks is achieved. Prints number of generations left to STDOUT.
	
	Parameters: 
	None 
	
	Returns: 
	G (str): Displays a string of '-' representing ON cells and 'X' representing OFF cells 
	30 rows by 80 columns to STDOUT. 
	"""
	#assign the variable tickies_and_coordinates to the user input 
	#assign the variables ticks, coordinates to the output of the function parse_input that takes the argument tickies_and_coordinates
	#assign the variable G to the output of the function create_grid that takes argument coordinates 
	#display the grid 
	#while ticks is less than 0, with every generation, count down the number of ticks by 1 every generation and 
	#prompt the user for an input before displaying an the output of updated_grid that takes the argument G 
	#print the number of generations left and display the grid again. 
	print("Please provide the number of ticks (generations) to cycle through followed by one space \n and then cells to seed as ON in the format row:column. \n Hit return to advance generations.")
	tickies_and_coordinates = input('>') 
	ticks, coordinates = parse_input(tickies_and_coordinates)
	G = create_grid(coordinates)
	display_grid(G)
	while ticks > 0:
		ticks -= 1 
		input('>')
		G = update_grid(G)	
		print(f"Generations left:", ticks)
		display_grid(G)

main()
	