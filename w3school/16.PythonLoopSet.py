# https://www.w3schools.com/python/python_sets_loop.asp

# using a for to iterate
thisset = {"apple", "moon", "banana", "strawberry", "luke"}
for x in thisset:
    print(x)
print("**"*20)


# join two sets
# The union() method returns a new set with all items from both sets:
set1 = {"a", "b", "c", "d"}
set2 = {1, 2, 3, 4, 5}
set3 = set1.union(set2)
print("SET3:", set3)
print("**"*20)

# the update() inserts the items in set2 into set1
set1.update(set2)
print("SET1:", set1)
print("**"*20)
# Note: Both union() and update() will exclude any duplicate items.

# the "intersection_update()" method will keep only the items that are present
# in both sets
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.intersection_update(y)
print(x)
print("**"*20)

# The intersection() method will return a new set, that only contains the items that are present in both sets.
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.intersection(y)
print(z)
print("**"*20)

# Keep All, But NOT the Duplicates
# the symmetric_difference_update()
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.symmetric_difference_update(y)
print(x)
print("**"*20)

# The symmetric_difference() method will return a new set,
# that contains only the elements that are NOT present in both sets.
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.symmetric_difference(y)
print(z)
print("**"*20)

# info methods: https://www.w3schools.com/python/python_sets_methods.asp
