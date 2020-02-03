ten_things = "Apples Oranges Crows Telephone Light Sugar"

print("Wait there are not 10 things in that list. Let's fix that.") 

#separate the string list ten_things by the separator defined beteween the '' marks in .split() 
# in this case, we separate with a space 
stuff= ten_things.split(' ')
#define a new list of strings, name it more_stuff 
more_stuff = ["Day", "Night", "Song", "Frisbee", "Corn", "Banana", "Girl", "Boy"] 

#create a while loop; while the length of the split list ten_things, now called 'stuff' is not ten words long, 
# add next_one on to the end of my_stuff (via the .append function) 
while len(stuff) != 10: 
#define variable next_one as an element removed from more_stuff 
	next_one = more_stuff.pop()
#add the element popped from the list more_stuff to the end of the list stuff (print the progress along the way) 
	print("Adding:", next_one) 
	stuff.append(next_one) 
	print(f"There are {len(stuff)} items now.") 
	
print("There we go:", stuff)


print(stuff[1]) #print the second element in the list 
print(stuff[-1]) #print the last item in the list 
print(stuff.pop()) #print the last item the last called element from the list
print(''.join(stuff)) #Join list 'stuf' without the separator defined within the quotation marks '' 
print('#'.join(stuff[3:5])) #print the sublist of elements in position 3 nd 5 with the separator '#' 
