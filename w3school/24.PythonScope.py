# https://www.w3schools.com/python/python_scope.asp

# A variable is only available from inside the region it is created. This is called scope.

# Local Scope
# A variable created inside a function belongs to the local scope of that function, and can only be used inside that function.
def myfunc():
    x = 300
    print(x)

myfunc()
print("**"*5)


# Function Inside Function
# the variable x is not available outside the function, but it is available for any function inside the function:
def myfunc2():
    x = 250

    def myinnerfunc():
        print(x)
    myinnerfunc()

myfunc2()
print("**"*5)


# Global Scope
# A variable created in the main body of the Python code is a global variable and belongs to the global scope.
x = 900


def myfunc3():
    print(x)

myfunc3()
print(x)
print("**"*5)


# Global Keyword
# If you need to create a global variable, but are stuck in the local scope, you can use the global keyword.
# The global keyword makes the variable global.
y = 555
print(y)


def myfunc4():
    global y
    y = 300

myfunc4()
print(y)
print("**"*5)
