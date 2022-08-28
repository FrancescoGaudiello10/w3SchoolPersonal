### https://www.w3schools.com/python/python_lists_loop.asp
### PYTHON LIST LOOPS

# Loop Through a List
thislist = ["apple", "banana", "cherry"]
for x in thislist:
    print(x)
print(20*"-")

# Loop Through the Index Numbers
# You can also loop through the list items by referring to their index number.
# Use the range() and len() functions to create a suitable iterable.
thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
    print(thislist[i])
# The iterable created in the example above is [0, 1, 2].
print(20*"-")


# Using a While Loop
# Remember to increase the index by 1 after each iteration.
thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist):
    print(thislist[i])
    i += 1
print(20*"-")


# Looping Using List Comprehension
# List Comprehension offers the shortest syntax for looping through lists:
thislist = ["apple", "banana", "cherry"]
[print(x) for x in thislist]
print(20*"-")


# Python - List Comprehension
# List comprehension offers a shorter syntax when you want to create
# a new list based on the values of an existing list.
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
    if "a" in x:
        newlist.append(x)

print(newlist)

# With list comprehension you can do all that with only one line of code:
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x for x in fruits if "a" in x]

print(newlist)


# The Syntax
""" 
    newlist = [expression for item in iterable if condition == True]

- The return value is a new list, leaving the old list unchanged.
"""
newlist = [x for x in fruits if x != "apple"]
print(newlist)


# The condition is optional and can be omitted:
newlist = [x for x in fruits]
print(newlist)
print(20*"-")

# With no if statement:
newlist = [x for x in fruits]
print(newlist)
print(20*"-")


# The iterable can be any iterable object, like a list, tuple, set etc.
newlist = [x for x in range(10)]
print(newlist)
print(20*"-")

newlist = [x for x in range(10) if x < 5]
print(newlist)
print(20*"-")


# EXPRESSION
# The expression is the current item in the iteration, but it is also the outcome,
# which you can manipulate before it ends up like a list item in the new list:
newlist = [x.upper() for x in fruits]
print(newlist)
print(20*"-")

newlist = ['hello' for x in fruits]
print(newlist)
print(20*"-")

newlist = [x if x != "banana" else "orange" for x in fruits]
print(newlist)
print(20*"-")