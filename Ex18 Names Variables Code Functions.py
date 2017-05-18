#Ex18 Names, Variables, Code, Functions

#This one is like the scripts with argv

def print_two(*args):
    arg1, arg2 = args     #Similar to argv, but not sure why the * is needed in the argument of the function
    print("arg1: %r, arg2: %r" %(arg1, arg2))

#ok, that *args function is actually pointless, we can just do this
def print_two_again(arg1,arg2):
    print("arg1:%r, arg2:%r" %(arg1, arg2)) #eliminates the extra line (line 6) by stating the inputs in parenthese next to the function

#this just takes one argument   
def print_one(arg1):
    print("arg1: %r" %arg1)

#this takes no arguments
def print_none():
    print("I got nothin'.")

print_two("Zed","Shaw")     #to call a function, the function is simply typed along with parenthesese containing the necessary arguments
print_two_again("Zed","Shaw")
print_one("First!")
print_none()
