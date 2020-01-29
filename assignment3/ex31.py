print("""You enter a dark rooom with two doors. Do you go through door #1 or door #2?""")


door = input(">")

if door == "1": 
	print("There's a giant bear in here eating all of your cheese cake!") 
	print("What do you do?")
	print("1. Take the cake.")
	print("2. Throw your shoe at the bear.")
	 
	bear = input(">")
	 
	if bear == "1":
		print("The bear eats your entire friggin' face. Nice.") 
	elif bear == "2":
		print(" The bear eats your legs. Nice.") 
	else: 
		print(f"Well, doing {bear} is probably better anyway.") 
		print("The big fat bear runs away.")
		
elif door == "2":
		print("You stare into the endless abyss of Cthulhu's retina.")
		print("1.Bloobs")
		print("2.Tiny metal martians.")
		print("3.Zoidberg's balls.")
		
		insanity = input(">")
		
		if insanity == "1" or insanity == "2":
			print("You are now an amorphous ball of jello.")
			print("Dude, sweet.")
		else:
			print("You ride a carosell for eternity.")
			
			
else:
				print("You get stuck in an escelator and die.")
				
	
		