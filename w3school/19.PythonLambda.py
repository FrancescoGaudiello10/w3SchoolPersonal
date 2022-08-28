# https://www.w3schools.com/python/python_lambda.asp

x = lambda a: a + 10
print(x(5))

x = lambda a, b: a * b
print(x(5, 6))

x = lambda a, b, c: a+b+c
print(x(5, 6, 10))


# Why Use Lambda Functions?
# The power of lambda is better shown when you use them as an anonymous
# function inside another function.
def myfunc(n):
    return lambda a: a*n


mydoubler = myfunc(2)
print(mydoubler(11))


def myfunc(n):
    return lambda a: a*n


mytripleer = myfunc(3)
print(mytripleer(11))
