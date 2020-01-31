print("How much would you like to increment by?")

user_select = input(">")
def loopy():
	i = 0 
	numbers = []
	snickers = 18
	while i < snickers:
		print(f"At the top i is {i}")
		numbers.append(i)
	
		i = i + int(user_select)
		print("Numbers now:", numbers)
		print(f"At the bottom i is {i}")
		
		
	print("The numbers:")

	for num in numbers:
		print(num)

loopy() 
