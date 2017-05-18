#Ex16 Reading and Writing Files

from sys import argv

script, filename = argv

print("We're going to erase %r." % filename)
print("If you don't want that, hit CTRL-C (^C).")
print("If you do want that, hit RETURN.")

input("?")

print("Opening the file...")
target = open(filename, 'w') #opens the target file so that the program can use it, notice it is stored as a variable
# In the above line, w means open the file in write mode
print("Truncating the file. Goodbye!")
target.truncate() #Empties the contents of the file, not to be used carelessly

print("Now I'm going to ask you for three lines.")

line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")

print("I'm going to write these to the new file.")

target.write(line1) #Writes variable or string to file, note that in this case target is the variable of the open file
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print("And finally, we close it")
target.close()  #Closes the file, similar to close & save in a text editor