# https://www.w3schools.com/python/python_modules.asp

# Consider a module to be the same as a code library.
# A file containing a set of functions you want to include in your application.

# Create a Module
# To create a module just save the code you want in a file with the file extension .py

import mymodule

mymodule.greeting("Jonathan")
print("**"*5)

"""
- Note: When using a function from a module, use the syntax: module_name.function_name.
"""

# Variables in Module
# The module can contain functions, as already described, but also variables of all types (arrays, dictionaries, objects etc)

a = mymodule.person1["age"]
print(a)
print("**"*5)


# Re-naming a Module
# You can create an alias when you import a module, by using the as keyword:
import mymodule as mx
a = mx.person1["age"]
print(a)
print("**"*5)


# Built-in Modules
# There are several built-in modules in Python, which you can import whenever you like.
import platform

x = platform.system()
print(x)
print("**"*5)


# There is a built-in function to list all the function names (or variable names) in a module. The dir() function:
import platform

x = dir(platform)
print(x)
print("**"*5)

# Note: The dir() function can be used on all modules, also the ones you create yourself.

# Import From Module
# You can choose to import only parts from a module, by using the from keyword.
from mymodule import person1

print(person1["country"])
print("**"*5)

"""
- Note: When importing using the from keyword, do not use the module name when referring to elements in the module.
"""


