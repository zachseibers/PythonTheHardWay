#Ex17 More Files

from sys import argv
from os.path import exists

script, from_file, to_file = argv     #stores command line inputs to respective variables according to order

print("Copying from %s to %s" % (from_file, to_file))

#we could do these two on one line, how?
in_file = open(from_file)
indata = in_file.read()

#This is how it would be done
#indata = open(from_file).read() 

print("The input file is %d bytes long" %len(indata))

print("Does the output file exist? %r" % exists(to_file)) #Exists tests to see if the argument file already exists
print("Ready, hit RETURN to continue, CTRL-C to abort.")
input()

out_file = open(to_file,'w')
out_file.write(indata)

print("Alright, all done.")

out_file.close()
in_file.close()
