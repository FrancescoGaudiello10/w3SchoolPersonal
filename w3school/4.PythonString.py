# https://www.w3schools.com/python/python_strings.asp

# single or double quotation marks
print("Hello")
print('Hello')
print(20*"-")

# Assign
a = "Hello"
print(a)
print(20*"-")

# Multiline Strings by 3 quotes
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)
print(20*"-")


# Strings are arrays
a = "Hello, World!"
print(a[1])
print(20*"-")

# Looping through a string
for x in "banana":
    print(x)
print(20*"-")

# String lenght using "len()"
a = "Hello, World!"
print(len(a))
print(20*"-")

# Check String
# we can use keyword "in"
txt = "The best things in life are free!"
print("free" in txt)
print("Original" in txt)
print(20*"-")

# and using "if"
txt = "The best things in life are free!"
if "free" in txt:
  print("Yes, 'free' is present.")
print(20*"-")

# check using "IF NOT"
txt = "The best things in life are free!"
print("expensive" not in txt)
print(20*"-")

# IF with not in
txt = "The best things in life are free!"
if "expensive" not in txt:
  print("No, 'expensive' is NOT present.")
print(20 * "-")

