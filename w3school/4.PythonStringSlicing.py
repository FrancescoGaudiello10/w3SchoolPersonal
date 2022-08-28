# https://www.w3schools.com/python/python_strings_slicing.asp

# Slicing
b = "Hello, World!"
print(b[2:5])

# Slicing from the start
b = "Hello, World!"
print(b[:5])

# Slice to the end
b = "Hello, World!"
print(b[3:])
print(20*"-")

# Negative index
b = "Hello, World!"
print(b[-5:-2])
print(20*"-")


# MODIFY STRING

# UpperCase
# The upper() method returns the string in upper case:
a = "Hello World!"
print(a.upper())

# Lower Case
# The lower() method returns the string in lower case:
a = "Hello, World!"
print(a.lower())


# Remove WhiteSpace at the start or end! (a.strip())
a = " Hello, World! "
print(a.strip())    # returns "Hello, World!"

# Replace String
# The replace() method replaces a string with another string:
a = "Hello world!"
print(a.replace("H", "J"))
print(20*"-")

# Split string
# The split() method returns a list where the text between the
# specified separator becomes the list items.
a = "Hello, World!"
print(a.split(","))     # returns ['Hello', ' World!']
print(20*"-")


# Python - String concatenation
# To concatenate, or combine, two strings you can use the + operator.
a = "Hello"
b = "World"
c = a + b
print(c)

a = "Hello"
b = "World"
c = a + " " + b
print(c)
print(20*"-")


# Format String
# But we can combine strings and numbers by using the format() method!
# The format() method takes the passed arguments, formats them, and places them in the string
# where the placeholders {} are:
# Use the format() method to insert numbers into strings:
age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))

# The format() method takes unlimited number of arguments, and are placed into the respective placeholders:
quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price))


# You can use index numbers {0} to be sure the arguments are
# placed in the correct placeholders:
quantity = 3
itemno = 567
price = 49.95
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity, itemno, price))
print(20*"-")


# Python - Escape Characters
# To insert char illegal in a string, use an escape char.
txt = "We are the so-called \"Vikings\" from the north."
print(txt)

txt = "This will insert one \\ (backslash)."
print(txt)

txt = "Hello\nWorld!"
print(txt)

txt = "Hello\rWorld!"
print(txt)

txt = "Hello\tWorld!"
print(txt)

#A backslash followed by three integers will result in a octal value:
txt = "\110\145\154\154\157"
print(txt)

##########################################
##########################################
# String Methods
# Note: All string methods returns new values.
# They do not change the original string.

# capitalize(): Upper case the first letter.
txt = "hello, and welcome to my world."
x = txt.capitalize()
print(x)

# casefold(): Make the string lower case
txt = "Hello, And Welcome To My World!"
x = txt.casefold()
print(x)


# Center: Print the word "banana",
# taking up the space of 20 characters, with "banana" in the middle:
txt = "banana"
x = txt.center(20)
print(x)

# string.center(length, character)
txt = "banana"
x = txt.center(20, "O")
print(x)

# count: Returns the number of times a specified value occurs in a string
txt = "I love apples, apple are my favorite fruit"
x = txt.count("apple")
print(x)

# Search from position 10 to 24:
txt = "I love apples, apple are my favorite fruit"
x = txt.count("apple", 10, 24)
print(x)
print(20*"-")


# Encode() The encode() method encodes the string, using the specified encoding.
# If no encoding is specified, UTF-8 will be used.
# string.encode(encoding=encoding, errors=errors)
txt = "My name is Ståle"
x = txt.encode()
print(x)
txt = "My name is Ståle"

print(txt.encode(encoding="ascii",errors="backslashreplace"))
print(txt.encode(encoding="ascii",errors="ignore"))
print(txt.encode(encoding="ascii",errors="namereplace"))
print(txt.encode(encoding="ascii",errors="replace"))
print(txt.encode(encoding="ascii",errors="xmlcharrefreplace"))


# Find()
txt = "Hello, welcome to my world."
x = txt.find("welcome")
print(x)

# First occurrence
txt = "Hello, welcome to my world."
x = txt.find("e")
print(x)

# Where in the text is the first occurrence of the letter "e"
# when you only search between position 5 and 10?:
txt = "Hello, welcome to my world."
x = txt.find("e", 5, 10)
print(x)

# If the value is not found, the find() method returns -1,
# but the index() method will raise an exception:
txt = "Hello, welcome to my world."
print(txt.find("q"))
#print(txt.index("q"))
print(20*"-")

# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# Other: https://www.w3schools.com/python/python_strings_methods.asp
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

# The index() method finds the first occurrence of the specified value.
# The index() method raises an exception if the value is not found.
# The index() method is almost the same as the find() method,
# the only difference is that the find() method returns -1 if
# the value is not found.
# string.index(value, start, end)
# Index:
txt = "Hello, welcome to my world."
x = txt.index("welcome")
print(x)

txt = "Hello, welcome to my world."
x = txt.index("e")
print(x)

txt = "Hello, welcome to my world."
x = txt.index("e", 5, 10)
print(x)