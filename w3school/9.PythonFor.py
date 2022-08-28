# https://www.w3schools.com/python/python_for_loops.asp

# loop for => iterating element in a list
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)

# The for loop does not require an indexing variable to set beforehand.
print(20*"-")

# looping through a string
for x in "banana":
    print(x)

print(20*"-")

print("first case: ")
# With BREAK statement, we can stop the loop before the end
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)
    if x == "banana":
        break

print("\nsecond case: ")

# second case, with after print
for x in fruits:
    if x == "banana":
        break
    print(x)

print(20*"-")
print("CONTINUE CASE: ")
# The CONTINUE statement = we cna stop the current iteration of the loop and continue
# continue = passa immediatamente all'istruzione successiva del FOR!!!
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    if x == "banana":
        continue
    print(x)

print(20*"-")


# The range() function
# The range() function returns a sequence of numbers, starting from 0 by default,
# and increments by 1 (by default), and ends at a specified number.

for x in range(6):
    print(x, end=" ")

# Note that range(6) is not the values of 0 to 6, but the values 0 to 5.
print("\n"+20*"-")

for x in range(2, 6):
    print(x, end=" ")
# Take the value of 2, 3, 4, 5.

print("\n" + 20*"-")


# The range() function defaults to increment the sequence by 1,
# however it is possible to specify the increment value by
# adding a third parameter: range(2, 30, 3):
for x in range(2, 30, 3):
    print(x, end=" ")

print("\n" + 20*"-")


# else in for loop = when loop is finished
for x in range(6):
    print(x)
else:
    print("Finally finished.")

print(20*"-")

# the else block won't be executed if the loop is stopped by a break statement.
# in this case, not print ( finally finished! )
for x in range(6):
    if x == 3:
        break
    print(x)
else:
    print("Finally finished!")

print(20*"-")


# NESTED LOOPS = loop inside a loop
# Print each adjective for every fruit:
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
    for y in fruits:
        print(x, y)


# The PASS statement
# for loops cannot be empty, but if you for some reason
# have a for loop with no content,
# put in the pass statement to avoid getting an error.

for x in [0, 1, 2]:
    pass

print(20*"-")

