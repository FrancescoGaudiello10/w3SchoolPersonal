# https://www.w3schools.com/python/python_dictionaries_loop.asp

# You can loop through a dictionary by using a for loop.
thisdict = {
    "nome": "Francesco",
    "anno": 1995,
    "mese": "Agosto",
    "lavoro": "ingegnere informatico"
}

for x in thisdict:
    print(x)
print("**"*20)

for x in thisdict:
    print(thisdict[x])
print("**"*20)

# another method
for x in thisdict.values():
    print(x)
print("**"*20)

for x in thisdict.keys():
    print(x)
print("**"*20)

# return a couple of tuple (key, value)
for x, y in thisdict.items():
    print(x, y)
print("**"*20)


# Python - Copy Dictionaries
# You cannot copy a dictionary simply by typing dict2 = dict1
# dict2 will only be a reference to dict1,
# and changes made in dict1 will automatically also be made in dict2.
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = thisdict.copy()
print(mydict)

# Another way to make a copy is to use the built-in function dict().
mydict2 = dict(thisdict)
print(mydict2)
print("**"*20)


# Nested Dictionaries
myfamily = {
    "child1": {
        "name": "Emily",
        "year": 2003
    },
    "child2": {
        "name": "Maria",
        "year": 2007
    },
    "child3": {
        "name": "Fulvio",
        "year": 1994
    }
}

# METHODS: https://www.w3schools.com/python/python_dictionaries_methods.asp

