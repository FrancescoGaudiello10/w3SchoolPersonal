# https://www.w3schools.com/python/python_math.asp

# The min() and max() functions can be used to find the lowest or highest value in an iterable:
x = min(5, 40, 20)
y = max(10, 29, 49, 32)
print("min:", x, "\nmax:", y)

# The abs() function returns the absolute (positive) value of the specified number:
a = abs(-10.5)
print("abs:", a)

# The pow(x, y) function returns the value of x to the power of y (xy).
p = pow(3, 2)
print("pow of 3^2:", p)
print("**"*10)

### The Math Module
# Python has also a built-in module called math, which extends the list of mathematical functions.
import math

# The math.sqrt() method for example, returns the square root of a number:
sq = math.sqrt(16)
print("square of 16:", sq)

# The math.ceil() method rounds a number upwards to its nearest integer,
# and the math.floor() method rounds a number downwards to its nearest integer, and returns the result:
ce = math.ceil(2.7)
fl = math.floor(2.7)
print("ceil:", ce, "\nfloor:", fl)
print("**"*10)


# The math.pi constant, returns the value of PI (3.14...):
pi = math.pi
print("pi greco:", pi)
