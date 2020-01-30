def main(): 
	from sys import argv
	scipt, filename = argv
	filehand = open(filename) 
	count = 0 
	line = filehand.readline()
	while line: 
		count += 1
		filehand.readline()
	print(count)
main()

#count lines, words and characters(including white spaces) should be 6, 69, 446) 