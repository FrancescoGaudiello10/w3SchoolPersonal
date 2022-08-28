# Link: https://www.w3schools.com/python/python_variables.asp

x = 5
y = "John"
print(x)
print(y)
print(type(x))
print(type(y))

# Casting
x = str(3)
y = int(3)
z = float(3)


# Techniques name variable

# CamelCase
myVariableName = "Hon"

# PascalCase
MyVariableName = "John"

# SnakeCase
my_variable_name = "john"


# Many Values to Multple variables:
x, y, z = "Orange", "Banana", "Cherry"
print(x)

# One value to multiple variables
a = b = c = "Orange"
print(a)

# Unpack a collection (ATTENZIONE)
fruits = ["apple", "banana", "cherry"]
p, w, k = fruits
print(p)

# Output Variables
x = "awesome"
print("Python is " + x)


# Global variables
# Variables that are created outside of a function are known as GLOBAL VARIABLES.
y = "ESKERE"
def myfunc_1():
    print("Python is " + y)
myfunc_1()


# if create a varibale with the same name inside a function, this variable will be local
# and can only used inside the function.
# Create a variable inside a function, with the same name as the global variable
x = "Perfect"

def myfunc_2():
  x = "fantastic"
  print("Python is " + x)

myfunc_2()

print("Python is " + x)

print(40*"-")

# The GLOBAL Keyword
# Per creare una variabile globale dentro una funzione, si utilizza "global"
def myfunc_gl():
  global x
  x = "fantastic"

myfunc_gl()

print("Python is " + x)


# Viene usato "global" se si vuole cambiare la variabile dentro la funzione
x = "awesome"

def myfunc():
  global x
  x = "fantastic"

myfunc()
print("Python is " + x)
