# https://www.w3schools.com/python/python_booleans.asp

# Booleans represent one of two values: True or False

print(10 > 9)
print(10 == 9)
print(10 < 9)


a = 200
b = 33
if b > a:
    print("b is greater than a")
else:
    print("b is not greater than a")

x = "Hello"
y = 15
print(bool(x))
print(bool(y))
print(20*"-")

# Any string is TRUE, except empty strings
# Any numbers is TRUE, except 0.
# Any list, tuple, set, and dictionare are TRUE, except empty ones.
print(bool("abc"))
print(bool(123))
print(bool(["apple", "cherry", "banana"]))

print(bool(False))
print(bool(None))
print(bool(0))
print(bool(""))
print(bool(()))
print(bool([]))
print(bool({}))


# Functions can return a Boolean
def myFunction():
    return True

print(myFunction())
print(20*"-")


def myFunction_2() :
  return True

if myFunction_2():
    print("YES!")
else:
    print("NO!")


# isinstance(): determine if an object is of a certain data type
x = 200
print(isinstance(x, int))
print(isinstance(x, float))