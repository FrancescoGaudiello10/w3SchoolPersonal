# https://www.w3schools.com/python/python_operators.asp

# Python Operators

print(10+65)

# * => Multiplication
x = 5
y = 2
print(x * y)

# / => Division
x = 5
y = 2
print(x / y)

# % => modulus
x = 5
y = 2
print(x % y)

# ** => Exponentiation
x = 2
y = 5
print(x ** y)   #same as 2*2*2*2*2

# // => Floor division
x = 5
y = 2
print(x // y)


# PYTHON ASSIGNMENT OPERATORS
x = 6
x += 4
x -= 1
x *= 3
x /= 9
x %= 2
x //= 2
x **= 3


# PYTHON COMPARISON
# != NOT EQUAL

# Python Logical
x = 5
print(not(x > 3 and x < 10))
# returns False because not is used to reverse the result


# PYTHON IDENTITY OPERATORS
x = ["apple", "banana"]
y = ["apple", "banana"]
z = x

print(x is z)
# returns True because z is the same object as x

print(x is y)
# returns False because x is not the same object as y, even if they have the same content

print(x == y)
# to demonstrate the difference betweeen "is" and "==": this comparison returns True because x is equal to y


# python membership operators:
x = ["apple", "banana"]

print("banana" in x)
# returns True because a sequence with the value "banana" is in the list


"""

Operator	Name	Description
& 	AND	Sets each bit to 1 if both bits are 1
|	OR	Sets each bit to 1 if one of two bits is 1
^	XOR	Sets each bit to 1 if only one of two bits is 1
~ 	NOT	Inverts all the bits
<<	Zero fill left shift	Shift left by pushing zeros in from the right and let the leftmost bits fall off
>>	Signed right shift	Shift right by pushing copies of the leftmost bit in from the left, and let the rightmost bits fall off

"""