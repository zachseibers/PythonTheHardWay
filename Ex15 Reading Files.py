#Ex15 Reading Files

from sys import argv

script, filename =  argv

txt = open(filename) #creates a file object from filename...allows the file's contents to be accessed later

print("Here's your file %r:" % filename)
print(txt.read()) #reads the contents of txt, due to above that means we are reading the contents of filename

print("Type the filename again:")
file_again = input(">") 

txt_again = open(file_again) #same as previous, just different names. Note that file name can be stored as variable in python code

print(txt_again.read()) #same as previous use.
