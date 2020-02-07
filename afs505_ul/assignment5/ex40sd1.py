class Song(object): 
	def __init__(self, lyrics): 
		self.lyrics = lyrics 
		
	def sing_me_a_song(self): 
		for line in self.lyrics:
			print(line) 

pickles_taste_good = Song(["These pickles are just so tasty, I just can't live without them."]) 
	
pickles_taste_good.sing_me_a_song()
