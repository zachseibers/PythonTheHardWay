# Ex42 Is-A, Has-A, Objects, and Classes

## Animal is-a object (yes, sort of confusing) look at the extra credit
class Animal(object):
    pass

## Animal has-a class dog
class Dog(Animal):

    def __init__(self, name):
        ## name is an object in claa Dog
        self.name = name

## Animal has a class cat
class Cat(Animal):

    def __init__(self, name):
        ## self.name is-a object in the cat class
        self.name = name

## Person is a class
class Person(object):

    def __init__(self, name):
        ## ??
        self.name = name

        ## Person has-a pet of some kind
        self.pet = None

## Fish is-a object
class Fish(object):
    pass

## Salmon is-a object
class Salmon(Fish):
    pass

## Halibut is-a-object
class Halibut(Fish):
    pass

## rover is-a Dog
rover = Dog("Rover")

## satan is a Cat
satan = Cat("Satan")

## Mary is a person
mary = Person("Mary")

## satan is-a instance of mary's pet
mary.pet = satan

## Frank is a object within the Employees class
frank = Employees("Frank", 120000)

## Rover is a instance of Frank's pet
frank.pet = rover

## flipper is an instance of fish object
flipper = Fish()

## flipper is an instance of Salmon object
crouse = Salmon()

## flipper is an instance of Halibut object
harry = Halibut()
