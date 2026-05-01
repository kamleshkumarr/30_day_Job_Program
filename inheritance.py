"""Inheritance allows a class (child class) to acquire properties and 
 methods of another class (parent class). It supports hierarchical 
 classification and promotes code reuse."""""


# A child get the properties and methods of the parent class.
# The child class can also have its own properties and methods.4

class Parent:
    def show(self):
        print("This is the parent class.")


class Child(Parent):
    def display(self):
        print("This is the child class.")

obj = Child()
obj.show()     # Output: This is the parent class.
obj.display()  # Output: This is the child class.


# 1. Single Inheritance: A child class inherits from a single parent class.

class Animal:
    def eat(self):
        print("Animal eats food.")

class Cow(Animal):
    def sound(self):
        print("cow says moo")

obj1 = Cow()
obj1.eat()   # Output: Animal eats food.
obj1.sound() # Output: cow says moo



# 2. Multiple Inheritance: A child class inherits from multiple parent classes.

class Father:
    def speak(self):
        print("Father speaks.")

class Mother:
    def cook(self):
        print("Mother cooks food.")

class Child(Father, Mother):
    def play(self):
        print("Child play games.")

obj2 = Child()
obj2.speak()  # Output: Father speaks.
obj2.cook()   # Output: Mother cooks food.
obj2.play()   # Output: Child play games.

# 2nd Example of Multiple Inheritance

class Animal:
    def eat(self):
        print("Animal eats food.")

class Lion(Animal):
    def sound(self):
        print("Makes sound")

class Cub(Animal, Lion):
    pass

obj3 = Cub()
obj3.eat()   # Output: Animal eats food.    
obj3.sound() # Output: Makes sound

# 3. Multilevel Inheritance: A child class inherits from a parent class, and then another child class inherits from that child class.

class Grandparent:
    def show(self):
        print("This is the grandparent class.")

class Parent(Grandparent):
    def display(self):
        print("This is the parent class.")

class Child(Parent):
    def play(self):
        print("This is the child class.")


obj4 = Child()
obj4.show()     # Output: This is the grandparent class.
obj4.display()  # Output: This is the parent class.
obj4.play()     # Output: This is the child class.

# 4. Hierarchical Inheritance: Multiple child classes inherit from a single parent class.

class Parent:
    def show(self):
        print("This is the parent class.")
class Child1(Parent):
    def display1(self):
        print("This is child class 1.")

class Child2(Parent):
    def display2(self):
        print("This is child class 2.")

obj5 = Child1()
obj5.show()    # Output: This is the parent class.
obj5.display1() # Output: This is child class 1.

obj6 = Child2()
obj6.show()    # Output: This is the parent class.
obj6.display2() # Output: This is child class 2.