# https://www.w3schools.com/python/python_datetime.asp

# A date in Python is not a data type of its own, but we can import a module named datetime to work with dates as date objects.

# Import the datetime module and display the current date:
import datetime

x = datetime.datetime.now()
print(x)
print("**"*5)

"""
-   The date contains year, month, day, hour, minute, second, and microsecond.
-   The datetime module has many methods to return information about the date object.
-   Here are a few examples, you will learn more about them later in this chapter:

"""

x = datetime.datetime.now()
print(x.year)
print(x.strftime("%A"))     # actual day
print("**"*5)


# Creating Date Objects
# To create a date, we can use the datetime() class (constructor) of the datetime module.
# The datetime() class requires three parameters to create a date: year, month, day.

import datetime

x = datetime.datetime(2020, 5, 18)
print(x)
print("**"*5)

# The datetime() class also takes parameters for time and timezone (hour, minute, second, microsecond, tzone),
# but they are optional, and has a default value of 0, (None for timezone).


"""
    The strftime() Method.
    - The datetime object has a method for formatting date objects into readable strings.
    - The method is called strftime(), and takes one parameter, format, to specify the format of the returned string:

"""

x = datetime.datetime(2021, 4, 20)
print(x.strftime("%A"))
print(x.strftime("%a"))
print(x.strftime("%B"))
print(x.strftime("%b"))
print(x.strftime("%c"))
print(x.strftime("%D"))
print(x.strftime("%Y"))
print(x.strftime("%y"))
print("**"*5)


# NOTE: more codify in: https://www.w3schools.com/python/python_datetime.asp
