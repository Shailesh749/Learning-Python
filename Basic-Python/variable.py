a = 10 # always give value address in python not give variable address
# b = 10
b=12
print(a+b)

print(id(a), id(b))


# variable name write
# -a=20  we cannot write like this
_a = 20 # we can write like this
print(_a)

# 1a = 20 we cannot write like this
a_b = 35 #we can write like this
print(a_b) 

# @a = 20 we cannot write like this


#Casting
#If you want to specify the data type of a variable, this can be done with casting.


x = str(3)
y = int(3)
z = float(3)

print(x)
print(y)
print(z)


#Many Values to Multiple Variables
#Python allows you to assign values to multiple variables in one line:

x, y, z = "Orange", "Banana", "Cherry"

print(x)
print(y)
print(z)


#One Value to Multiple Variables

#And you can assign the same value to multiple variables in one line:

x = y = z = "Orange"
print(x)
print(y)
print(z)


#Unpack a Collection
#If you have a collection of values in a list, tuple etc. Python allows you to extract the values into variables. This is called unpacking.

fruits = ["apple", "banana", "cherry"]
x, y, z = fruits

print(x)
print(y)
print(z)


#Global Variables
#Variables that are created outside of a function (as in all of the examples in the previous pages) are known as global variables.

#Global variables can be used by everyone, both inside of functions and outside.

x = "awesome"

def myfunc():
  print("Python is " + x)

myfunc()



#If you create a variable with the same name inside a function, this variable will be local, and can only be used inside the function. The global variable with the same name will remain as it was, global and with the original value.

#Create a variable inside a function, with the same name as the global variable

x = "awesome"

def myfunc():
  x = "fantastic"
  print("Python is " + x)

myfunc()

print("Python is " + x)



#The global Keyword
#Normally, when you create a variable inside a function, that variable is local, and can only be used inside that function.

#To create a global variable inside a function, you can use the global keyword.

#If you use the global keyword, the variable belongs to the global scope:

def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)




#Also, use the global keyword if you want to change a global variable inside a function.

#To change the value of a global variable inside a function, refer to the variable by using the global keyword:

x = "awesome"

def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)