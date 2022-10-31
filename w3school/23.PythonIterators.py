# https://www.w3schools.com/python/python_iterators.asp

"""
-   An iterator is an object that contains a countable number of values.
-   An iterator is an object that can be iterated upon, meaning that you can traverse through all the values.
-   Technically, in Python, an iterator is an object which implements the iterator protocol,
    which consist of the methods __iter__() and __next__().

Iterator vs Iterable:
-   Lists, tuples, dictionaries, and sets are all iterable objects.
    They are iterable containers which you can get an iterator from.
-   All these objects have a iter() method which is used to get an iterator:

"""

mytuple = ("apple", "banana", "cherry")
myit = iter(mytuple)

# single element
print(next(myit))
print(next(myit))
print(next(myit))
print("**"*8)


# Even strings are iterable objects, and can return an iterator:
mytuple = "banana"
myit = iter(mytuple)

print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print("**"*8)


# Looping Through an Iterator
mytuple = ("apple", "banana", "cherry")

for x in mytuple:
    print(x)
print("**"*8)


# Iterate the characters of a string:
mystr = "banana"
for x in mystr:
    print(x)
print("**"*8)
# The for loop actually creates an iterator object and executes the next() method for each loop.


"""
    CREATE AN ITERATOR
    - To create an object/class as an iterator you have to implement the methods __iter__() and __next__() to your object.
    - all classes have a function called __init__(), which allows you to do some initializing when the object is being created.
    - The __iter__() method acts similar, you can do operations (initializing etc.), but must always return the iterator object itself.
    - The __next__() method also allows you to do operations, and must return the next item in the sequence.
    
"""


class MyNumbers:

    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        x = self.a
        self.a += 1
        return x

myClass = MyNumbers()
myIter = iter(myClass)

print(next(myIter))
print(next(myIter))
print(next(myIter))
print(next(myIter))
print(next(myIter))
print(next(myIter))
print(next(myIter))
print("**"*8)


"""
    StopIteration
    - To prevent the iteration to go on forever, we can use the StopIteration statement.
    - n the __next__() method, we can add a terminating condition to raise an error if the iteration is done a specified number of times:
    
"""


# stop after 20 iterations
class MyNumbers2:

    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        if self.a <= 20:
            x = self.a
            self.a += 1
            return x
        else:
            raise StopIteration

myClass2 = MyNumbers2()
myIter2 = iter(myClass2)

for x in myIter2:
    print(x)
print("**"*8)
