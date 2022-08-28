# w3schools.com/python/python_dictionaries.asp

# Dictionaries are used to store data values in key:value pairs.
# A dictionary is a collection which is ordered*, changeable and do not allow duplicates.
# As of Python version 3.7, dictionaries are ordered.
# In Python 3.6 and earlier, dictionaries are unordered.

ex = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1992
}
print(ex)
print("**"*20)

# Dictionary items are ordered, changeable, and does not allow duplicates.
print(ex["model"])
print("**"*20)

# When we say that dictionaries are ordered, it means that the items have a defined order,
# and that order will not change.
# Unordered means that the items does not have a defined order,
# you cannot refer to an item by using an index.
# Duplicates Not Allowed
# Dictionaries are changeable, meaning that we can change,
# add or remove items after the dictionary has been created.

# len
print(len(ex))

# The values in dictionary items can be of any data type:
newdict = {
    "brand": "Ford",
    "electric": False,
    "year": 1993,
    "colors": ["red", "white", "black"]
}

# REMEMBER
# There are four collection data types in the Python programming language:
#
# List is a collection which is ordered and changeable. Allows duplicate members.
# Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
# Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
# Dictionary is a collection which is ordered** and changeable. No duplicate members.
print("**"*20)

# ACCESSING ITEMS
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = thisdict["model"]
print("accessing:", x)

# Another method to return a value
x = thisdict.get("model")
print("accessing:", x)
print("**"*20)

# get keys: return a list of all the keys
x = thisdict.keys()
print("Keys:", x)
print("**"*20)

car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
x = car.keys()
print(x)    # before the change

car["color"] = "white"
print(x)    # after the change
print("**"*20)

# The values() method will return a list of all the values in the dictionary.
x = thisdict.values()
print("Value:", x)
x = car.values()
print(x)
car["year"] = 2020
print(x)
print("**"*20)

# get items:
# The items() method will return each item in a dictionary, as tuples in a list.
print("X", x)
x = thisdict.items()
# Get a list of the key:value pairs
print("X after items:", x)
print("**"*20)

# Check if Key Exists
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
if "model" in thisdict:
    print("Yes, 'model' is one of the keys in the thisdict dictionary")
print("**"*20)


# UPDATE DICTIONARY
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1921
}
thisdict.update({"year": 1992})
print("**"*20)


# ADDING ITEMS
# method 1
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1993
}

thisdict["color"] = "white"
print(thisdict)

# method 2
thisdict.update({"color": "black"})
print(thisdict)
print("**"*20)


# REMOVING ITEMS
# There are several methods to remove items from a dictionary:
# The pop() method removes the item with the specified key name:
print("before dizionario:\n", thisdict)
thisdict.pop("model")
print("after dizionario:\n", thisdict)
print("**"*20)


# The popitem() method removes the last inserted item
# (in versions before 3.7, a random item is removed instead):

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.popitem()
print(thisdict)
print("**"*20)

# The del keyword removes the item with the specified key name:
del thisdict["model"]
print(thisdict)

# del thisdict => delete the dictionary
thisdict.clear()
print(thisdict)