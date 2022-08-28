# https://www.w3schools.com/python/python_sets.asp

# Set is a collection which is unordered, unchangeable and not indexed

thisSet = {"apple", "banana", "cherry"}
print(thisSet)
print("**"*20)

# Set items are unordered, unchangeable, and do not allow duplicate values.
# duplicate not allowed
thisset = {"apple", "banana", "cherry", "apple"}
print(thisset)
print("**"*20)

thisset = {"apple", "banana", "cherry"}
print(len(thisset))
print("**"*20)

# DataType
set1 = {"apple", "banana", "cherry"}
set2 = {1, 5, 7, 9, 3}
set3 = {True, False, False}
print(type(set1))
print(type(set2))
print(type(set3))
print("**"*20)

# but is possible:
set1 = {"abc", 34, True, 40, "male"}
print(type(set1))
print("**"*20)

# cannot access items in a set by referring to an index or a key.
thisset = {"apple", "banana", "cherry"}
for x in thisset:
    print(x)
print("**"*20)

# check if presente an element
print("banana" in thisset)
print("**"*20)

# Once a set is created, you cannot change its items, but you can add new items.
# add items
thisset = {"apple", "banana", "cherry"}
thisset.add("orange")
print(thisset)
print("**"*20)

# to add items from antoher set into the current set, use the "update()".
thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}
thisset.update(tropical)
print(thisset)
print("**"*20)

# The object in the update() method does not have to be a set, it can be any iterable object
# (tuples, lists, dictionaries etc.).

# to remove an item in a set, use remove() or discard()
thisset = {"apple", "banana", "cherry"}
thisset.remove("banana")
print(thisset)
print("**"*20)
# Note: If the item to remove does not exist, remove() will raise an error.

thisset = {"apple", "banana", "cherry"}
thisset.discard("apple")
print(thisset)
print("**"*20)
# Note: If the item to remove does not exist, discard() will NOT raise an error.

# clear empties the set
thisset.clear()
print(thisset)
print("**"*20)

# del will delete the set completely
thisset = {"apple", "banana", "cherry"}
del thisset
# print(thisset)
