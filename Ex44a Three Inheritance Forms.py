#Ex44 with combined forms of inheritance functions

class Parent(object):

    def override(self):
        print("PARENT override()")

    def implicit(self): 
        # implicit function that will be available to sub classes, such as Child
        print("PARENT implicit()")

    def altered(self):
        print("PARENT altered")

class Child(Parent):

    def override(self):
        print("CHILD override()")

    def altered(self):
        print("CHILD, BEFORE PARENT altered()")
        super(Child, self).altered()
        #super calls the super class of Child and runs the function .altered() that it contains.
        print("CHILD, AFTER PARENT altered()")

dad = Parent()
son = Child()

dad.implicit()
son.implicit() #This is contained in Parent class

dad.override()
son.override() #Since function is contained in Child subclass, it overrides the parent class function

dad.altered() 
son.altered()  
#runs altered() from Parent class, then son, as per normal. 
# The super function in the altered function of the Child class (ln 22) calls the parent function
