from sys import argv 

script, filename = argv

print(f"Were going to erase {filename}.")
print("If you dont want that, hit CRTL-C (^C).")
print("If you do want that hit RETURN.") 

input("?")

print("Opening the file...")
target=open(filename,'w')

print("Truncating the file. Goodbye!") 
target.truncate()

print("Now I'm going to ask you for three lines.") 

line1= input("line1:")
line2= input("line2:")
line3= input("line3:")

print("I'm going to write these to the file.")

target.write("{0}\n{1}\n{2}\n".format(line1, line2, line3))

print("And finally, we close it.")

target.close()
