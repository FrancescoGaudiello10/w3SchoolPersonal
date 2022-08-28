# Object Methods
# Objects can also contain methods.
# Methods in objects are functions that belong to the object.


class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def myfunc(self):
        print("Hello, my name is " + self.name)


p1 = Person("John", 23)
p1.myfunc()


# Note: The self parameter is a reference to the current instance of the class, and is used to access variables that belong to the class.

# The self Parameter
# The self parameter is a reference to the current instance of the class, and is used to access variables that belongs to the class.

# You can modify properties on objects like this:
print(p1)
print(p1.age)
p1.age = 40
print(p1.age)

# Delete Object Properties
del p1.age

# Delete Objects
del p1


# The pass Statement
# class definitions cannot be empty, but if you for some reason have a class definition with no content, put in the
# pass statement to avoid getting an error.
class Robot:
    pass

