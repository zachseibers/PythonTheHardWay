#Ex14 Prompting and Passing

from sys import argv

script, user_name = argv
prompt = '>' #This is the string that appears before the space inwhich the user would respond


print("Hi %s, I'm the %s script." %(user_name, script))  #%s is the variable placeholder for cript inputs
print("I'd like to ask you a few questions.")
print("Do you like me %s?" % user_name)
likes = input(prompt)

print("Where do you live %s?" % user_name)
lives = input(prompt)

print("What kind of computer do you have?")
computer = input(prompt)

print("""
Alright, so you said %r about liking me. 
You live in %r. Not sure where that is. 
And you have a %r computer. Nice. 
""" %(likes, lives, computer))  # %r is the variable placeholder for an output.
