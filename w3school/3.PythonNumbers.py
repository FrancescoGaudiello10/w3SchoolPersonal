# https://www.w3schools.com/python/python_numbers.asp

# There are three numeric types in Python
# int
# float
# complex

x = 1
y = 2.8
z = 2j

print(type(x))
print(type(y))
print(type(z))
print(20*"-")

# Int (integer) is a whole number, positive or negative,
# without decimal.
x = 1
y = 35656222554887711
z = -3255522

print(type(x))
print(type(y))
print(type(z))
print(20*"-")

# float (floating point number) is a number positive or negative, containing one
# or more decimals
x = 1.10
y = 1.0
z = -35.59

print(type(x))
print(type(y))
print(type(z))
print(20*"-")

# float can also be scientific numbers with "e"
x = 35e3
y = 12E4
z = -87.7e100

print(type(x))
print(type(y))
print(type(z))
print(20*"-")


# complex numbers are written with "j" as the imaginary part
x = 3+5j
y = 5j
z = -5j

print(type(x))
print(type(y))
print(type(z))
print(20*"-")


# Type conversion: is possible convert from one type to another type.
x = 1    # int
y = 2.8  # float
z = 1j   # complex

#convert from int to float:
a = float(x)

#convert from float to int: (not round)
b = int(y)

#convert from int to complex:
c = complex(x)

print(a)
print(b)
print(c)

print(type(a))
print(type(b))
print(type(c))
print(20*"-")

# Note: You cannot convert complex numbers into another number type.


# Random Number
# Python does not have a random() function to make a random number,
# but Python has a built-in module called random that can be used to
# make random numbers.
import random
print(random.randrange(1,10))
print(20*"-")
