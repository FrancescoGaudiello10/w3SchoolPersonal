### https://www.w3schools.com/python/python_lists_sort.asp

### PYTHON LIST SORT
# List objects have a sort() method that will sort the list alphanumerically, ascending, by default:

thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)

thislist = [100, 50, 65, 82, 23]
thislist.sort()
print(thislist)
print(20*"-")

# To sort descending, use the keyword argument reverse = True:
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort(reverse=True)
print(thislist)

thislist = [100, 50, 65, 82, 23]
thislist.sort(reverse=True)
print(thislist)
print(20*"-")


### Customize Sort Function
# You can also customize your own function by using the keyword argument key = function.
# Sort the list based on how close the number is to 50:
def myfunc(n):
    return abs(n-50)

thislist = [100, 50, 40, 30, 210, 12]
thislist.sort(key=myfunc)
print(thislist)
print(20*"-")


# Case Insensitive Sort
# By default the sort() method is case sensitive,
# resulting in all capital letters being sorted before lower case letters:

thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(key=str.lower)
print(thislist)
print(20*"-")


# Reverse Order
# What if you want to reverse the order of a list, regardless of the alphabet?
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.reverse()
print(thislist)
print(20*"-")


### COPY LISTS PYTHON
# You cannot copy a list simply by typing list2 = list1, because:
# list2 will only be a reference to list1,
# and changes made in list1 will automatically also be made in list2.
thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)

# *** Another way to make a copy is to use the built-in method list(). ***
thislist = ["apple", "banana", "cherry"]
mylist = list(thislist)
print(mylist)
print(20*"-")


### PYTHON - JOIN LISTS
# There are several ways to join, or concatenate, two or more lists in Python.
# One of the easiest ways are by using the + operator.
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3)


# Another way to join two lists is by appending all the items from list2 into list1, one by one:
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]
for x in list2:
    list1.append(x)

print(list1)


### Or you can use the extend() method, which purpose is to add elements from one list to another list:
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list1.extend(list2)
print(list1)


### PYTHON - LIST METHODS
"""

Method	Description:

append()	    Adds an element at the end of the list
clear()	        Removes all the elements from the list
copy()	        Returns a copy of the list
count()	        Returns the number of elements with the specified value
extend()	    Add the elements of a list (or any iterable), to the end of the current list
index()	        Returns the index of the first element with the specified value
insert()	    Adds an element at the specified position
pop()	        Removes the element at the specified position
remove()	    Removes the item with the specified value
reverse()	    Reverses the order of the list
sort()	        Sorts the list

"""