# https://www.w3schools.com/python/python_classes.asp

# Python is an object oriented programming language. (OOP)
# Almost everything in Python is an object, with its properties and methods.
# A Class is like an object constructor, or a "blueprint" for creating objects.

# To create a class, use the keyword class:
class MyClass:
    x = 5


# Create an object named p1, and print the value of x:
p1 = MyClass()
print(p1.x)
print("**"*10)

# To understand the meaning of classes we have to understand the built-in __init__() function.
# All classes have a function called __init__(), which is always executed when the class is being initiated.
# Use the __init__() function to assign values to object properties, or other operations that are necessary to do when
# the object is being created:


# Create a class named Person, use the __init__() function to assign values for name and age:
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p1 = Person("John", 39)
print(p1.name)
print(p1.age)


# Note: The __init__() function is called automatically every time the class is being used to create a new object.

