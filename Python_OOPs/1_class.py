

# Class
# A class is a collection of objects. Classes are blueprints for creating objects. A class defines a set of attributes and methods that the created objects (instances) can have.  

# Classes are created by keyword class.
# Attributes are the variables that belong to a class.
# Attributes are always public and can be accessed using the dot (.) operator. Example: Myclass.Myattribute


# Creating a class
class Myclass:
    x = 5

# Creating an object
p1 = Myclass()  
print(p1.x)  # Output: 5


class Dog:
    species = "Canine"  # Class attribute

    def __init__(self, name, age):
        self.name = name  # Instance attribute
        self.age = age    # Instance attribute

# Creating an object of the Dog class
my_dog = Dog("Buddy", 3)
print(my_dog.name)     # Output: Buddy  
print(my_dog.age)      # Output: 3
print(my_dog.species)  # Output: Canine        