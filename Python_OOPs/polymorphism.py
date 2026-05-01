

"""Polymorphism means "same operation, different behavior." 
It allows functions or methods with the same name to work 
differently depending on the type of object they are acting upon.
The flowchart below represents the different types of polymorphism, 
showing how a single interface can exhibit multiple behaviors at compile-time and run-time."""


# 🔥 1. Method Overriding (Runtime Polymorphism)

# Child class changes parent method behavior.

class Animal:
    def speak(self):
        print("Animal speaks")

class Dog(Animal):
    def speak(self):
        print("Dog barks")

class Cat(Animal):
    def speak(self):
        print("Cat meows")


animals = [Dog(), Cat()]
for animal in animals:
    animal.speak()  # Output: Dog barks, Cat meows



# 🔥 2. Duck Typing (Very Important in Python)
# Python doesn’t care about class type, only behavior.

class Bird:
    def fly(self):
        print("Bird flies")

class Airplane:
    def fly(self):
        print("Airplane flies")

def make_it_fly(thing):
    thing.fly()

make_it_fly(Bird())      # Output: Bird flies
make_it_fly(Airplane())  # Output: Airplane flies


# 🔥 3. Operator Overloading
# Same operator behaves differently.

print(1 + 2)          # Output: 3 (integer addition)
print("Hello, " + "World!")  # Output: Hello, World! (string concatenation)


# 🔥 4. Function Polymorphism
# Same function works with different data types

def add(a, b):
    return a + b

print(add(1, 2))          # Output: 3 (integer addition)
print(add("Hello, ", "World!"))  # Output: Hello, World! 


# 🧠 Why Polymorphism Matters
# Flexible code
# Reusable functions
# Cleaner design
# Used heavily in:
# Django
# APIs
# Large-scale systems

# Real-world example of polymorphism in a user management system:

class Payment:
    def pay(self):
        pass

class UPI(Payment):
    def pay(self):
        print("Pay via UPI")

class Card(Payment):
    def pay(self):
        print("Pay via Card")

def process(payment):
    payment.pay()

process(UPI())
process(Card())