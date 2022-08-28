# https://www.w3schools.com/python/python_while_loops.asp

# While

i = 1
while i < 5:
    print(i)
    i += 1

print(20*"-")

# Rememeber to increment i or loop forever
# with the "break" statement, we can stop the loop
i = 1
while i < 8:
    print(i)
    if i == 3:
        break       # Termina il ciclo while
    i += 1

print(20*"-")


# The "continue" statement
# we can stop the current iteration and continue with the next
i = 0
while i < 5:
    i += 1
    if i == 3:
        continue        # Continua il ciclo while
    print(i)

print(20*"-")


# The else statement:
# with the else statement we can run a block of code once when the condition
# no longer is true

i = 1
while i < 6:
    print(i)
    i += 1
else:
    print("i is no longer than 6.")

print(20*"-")

