from sys import exit 

def finish_line(): 
	print("Holy shit it worked. The Fascists are obliterated.") 
	print("You won!") 
	
finish_line() 

def gate_start():
	print("""You are at the top of your favorite ski run, you look left and see the Jesus themself strapping into their skis. \n 
	You look right and see Stalin taking one last drag one off his cigar. \n 
	In front of you is your middle school math teacher holding a large flask of liquid LSD. \n
	'To the victor goes the spoils!' The teacher yells into the crisp morning air.""") 
	
	print("""You know Stalin to be an incredible skiier, and Jesus is sure to cheat. \n 
	you think to yourself 'I have to start strong.' \n 
	There is a large rock in front of you. \n Do you veer left and cut off the son of god, try to launch over the rock (type launch) or right into the hulking mass of Stalin?""") 
	choice = input(">") 
	
	if choice == "left": 
		print(" You duck under Jesus' gaudy out-dated robe and launch into first place.") 
	elif choice == "right":
		print("Stalin punches you square in the face and you fall into a pillow of powder snow. Do you get back up? Y or N?") 
		get_up = input(">")
		if get_up == "Y":
			pass 
		else: 
			print("You don't deserve the spoils anyway, brush yourself off, you're in last place.") 		
	else: 
		print("You eat shit over the rock and are relegated to last place. But the race is has just started, carry on!") 

gate_start()

def bear_encounter():
	print("You are in the midst of wondering how the heck you got into this situation when a bear steps into the ski run.") 
	print("You are faced with some options here. \n You need the bear to move. \n Do you head butt (head) or use a ski pole as a joust (joust)?") 
	head_joust = input(">") 
	
	if head_joust == "head": 
		print("""That was a really dumb idea. Do I even need to explain why? \n 
		No, but I will. The bear rips your helmet off, allong with your headphones. \n 
		No more beats for you on this epic ride.""") 
	elif head_joust == "joust": 
		print("Hell yea! Skewered bear balls for dinner tonight! Provided you beat those two fascists in this race and don't die.") 
	else: 
		print("Looks like you F'd that up, heres another bear, try again.") 
		bear_encounter()
			
bear_encounter() 

def silos():
	print("""You're either in first or last at this point (I'm not sure, as I'm just a computer), but you think to yourself: \n 
	'Gee, sure would be nice to ensure my victory in this race and snag that big 'ol vial of Electric Kool-Aid. \n 
	So you're on the lookout for options.""") 
	print("And just as luck would have it, you see a shiny metal dome in the trees. So you veer towards it.") 
	print("Oh boy, its a Soviet missile silo! Did I forget to mention your favorite ski run is in Siberia now?")
	print("This is your opportunity, you ponder launching these missiles at your opponents. But you need a code.") 
	print("Do you search the trees for a carving of the four digit code you need (trees), do you check you body for new tatoos (tats) or make something up (make)?") 
	
	
	
	
	silos = input(">")
	if silos == "trees": 
		print("You find a carving: 'Putin has a small Дик', fall into a tree well and die.")
	elif silos == "tats": 
		print("Dude, you need to lay off the ketamine, how'd that new tat get there? You enter the code and launch the missiles right into Stalin and Jesus.") 
	elif silos == "make": 
		print("Think of something quick, that countdown timer just started out of nowhere. Guess your 4 numbers.") 
		make = input()
		number_correct = False 
		while True: 
			if "1" in make or "7" in make and not number_correct: 
				finish_line()
		else: 
			print("That's not a number.") 
	else: 
		silos() 
				
silos() 





					
			
				
	