# https://www.w3schools.com/python/python_functions.asp

# A function is a block of code which only runs when it's called.
# Can pass data (parameters) into a function.
# A function can return data as a result


def my_function():
    print("Hello from a function.")


my_function()
print(20 * "-")


# Information can be passed into functions as arguments.
def my_function_2(fname):
    print(fname + " Refsnes")


my_function_2("Emil")
my_function_2("Tobias")
my_function_2("Linus")
print(20 * "-")


# Arguments are often shortened to args in Python documentations.
# Function with 2 argument

def my_function_2arg(fname, lname):
    print(fname + " " + lname)


my_function_2arg("Emil", "Refsnes")
print(20 * "-")


# Arbitrary Arguments, *args
# Arbitrary Arguments are often shortened to *args in Python documentations.
def my_function(*kids):
    print("The youngest child is " + kids[2])


my_function("Emil", "Tobias", "Linus")
print(20 * "-")


# Keyword Arguments
# You can also send arguments with the key = value syntax.
# This way the order of the arguments does not matter.
def my_function(child3, child2, child1):
    print("The youngest child is " + child3)

my_function(child1="Emil", child2="Tobias", child3="Linus")
# The phrase Keyword Arguments are often shortened to kwargs in Python documentations.
print(20 * "-")


# Arbitrary Keyword Arguments, **kwargs
# If you do not know how many keyword arguments that will be passed into your function,
# add two asterisk: ** before the parameter name in the function definition.
def my_function(**kid):
    print("His last name is " + kid["lname"])
    print("His first name is " + kid["fname"])


my_function(fname="Tobias", lname="Refsnes")
print(20 * "-")


# Arbitrary Kword Arguments are often shortened to **kwargs in Python documentations.


# Default Paramter value
# If we call the function without argument, it uses the default value:
# if no argument, insert "Norway"
def my_function(country="Norway"):
    print("I am from " + country)


my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil")
print(20 * "-")


# Passing a List as an Argument
# You can send any data types of argument to a function
# (string, number, list, dictionary etc.),
# and it will be treated as the same data type inside the function.
#
# E.g. if you send a List as an argument,
# it will still be a List when it reaches the function:
def my_function(food):
    for x in food:
        print(x)


fruits = ["apple", "banana", "cherry"]
my_function(fruits)
print(20 * "-")


# return values
# use the "return" statement
def my_function_return(x):
    return 5*x

print(my_function_return(50))
print(my_function_return(3))

print(20 * "-")


# The pass Statement
# function definitions cannot be empty, but if you for some reason have a function definition with no content,
# put in the pass statement to avoid getting an error.
def pass_my_function():
    pass


# **** RECURSION ****
# Python also accepts function recursion, which means a defined function can call itself
def tri_recursion(k):
    if k > 0:
        result = k+tri_recursion(k-1)
        print(result)
    else:
        result = 0
    return result

print("\n\nRecursion Example Results")
tri_recursion(6)
