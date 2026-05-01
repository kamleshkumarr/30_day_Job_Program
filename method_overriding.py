# When a child class provides a new version of a method already defined in the parent class.

"""❗ Reality first:

Python does NOT support true method overloading like Java or C++.
In Python, if you define multiple methods with the same name,
 the last one defined will overwrite the previous ones. However, 
 you can achieve similar functionality using default arguments or variable-length arguments."""

class Parent:
    def show(self):
        print("This is Parent class")


class Child(Parent):
    def show(self):   # overriding
        print("This is Child class")


obj = Child()
obj.show()


# Access Parent Method using super()

class Parent:
    def show(self):
        print("This is Parent class")


class Child(Parent):
    def show(self):   # overriding
        super().show()  # Calls the parent's show method
        print("This is Child class")


obj = Child()
obj.show()