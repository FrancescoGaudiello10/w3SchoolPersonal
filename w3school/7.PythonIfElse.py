# https://www.w3schools.com/python/python_conditions.asp

# Example
a = 33
b = 222
if b > a:
    print("B is greater than A")


a = 33
b = 33
if b > a:
    print("B is greater than A")
elif a == b:
    print("A and B are equal.")
else:
    print("A is greater than B")


a = 200
b = 33
if b > a:
    print("b is greater than a")
else:
    print("b is not greater than a")

print(20*"-")

### SHORT HAND IF
# if u have only one statement to execute, can put in same line.
if a > b: print("A is greater than B")

### SHORT HAND IF ... ELSE
a = 2
b = 300
print("A") if a > b else print("B")

# This technique is known as Ternary Operators, or Conditional Expressions.

# MULTIPLE IF-ELSE same line.
a = 330
b = 3300
print("A") if a > b else print("=") if a == b else print("B")
print(20*"-")


# AND: logical operator
a = 200
b = 33
c = 420
if a > b and c > a:
    print("Both conditions are True")


# OR
a = 200
b = 33
c = 500
if a > b or a > c:
    print("At least one of the conditions is True")


# nested if = if statement inside if statements, this is called nested if.
x = 41
if x > 10:
    print("Above ten, ")
    if x > 20:
        print("and also above 20!")
    else:
        print("but not above 20.")

print(20*"-")


# The PASS statement
# if statements cannot be empty, but if u for some reasone have an if with no content
# put in the pass statemetn to avoid getting an error.
a = 30
b = 100
if b > a:
    pass


