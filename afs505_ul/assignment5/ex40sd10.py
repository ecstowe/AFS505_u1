class Cars(object): 

	def __init__(self, color, type): 
		self.color = color 
		self.type = type 
		
	def what_kinda_car(self): 
		print("This car is" + self.color, "and" + self.type)
		
coup = Cars("Red", "Fuckin Fast") 
turd = Cars("Blue", "Not Fast") 


coup.what_kinda_car() 