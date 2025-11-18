# .py file is a module
# Built-in modules
# math, random, datetime, ...


# how to import a module in python

# Syntax: import module_name
# Syntax for importing only few functions/variables: from module_name import f1, f2, f3


import math
# Calculate square root of a number
num = 100
output = math.sqrt(num)
# module.function_name(agru1, agru2, ...)
print(f"Square root of {output}")



# Calculate the area of a circle
radius = 5
area_of_circle = math.pi * (radius ** 2)
print(f"Area of circle with radius {radius} is {area_of_circle}")
print(math.pi)




# directly import module
# throw a die 
from random import randint
value = randint(1, 6)
print(value)




# Syntax to create an alias for the module that is imported: import module_name as alias_name

import datetime as dt

t = dt.time(8, 43, 51)
print(t)
