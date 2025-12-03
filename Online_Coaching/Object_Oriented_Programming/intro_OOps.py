"""
object => a container
   => data -> attributes
   => functionality -> methods/behaviour
"""

fruits = ["mango", "apple", "orange"]
print(type(fruits))

# fruits is an object of a class
fruits.append("grapes")
print(fruits)


"""
car1
    => brand = "BMW", model ="XYZ340", year = 2020
    => accelerate, break

dot notation (.)  

car1.brand => "BMW"
car1.accelerate(10)
"""

# Creating objects => we need classes

# classes => templates/blueprints/design used for creating objects
# Also called as type

# Objects are creating using the class
# Instances of a class


# Creating a class

class MyClass:
   pass


# Creating an object
obj1 = MyClass()
obj2 = MyClass()

# obj1 and obj2 are objects of class MyClass

l1 = [10, 20, 30]
print(type(l1))

print(type(obj1))
print(type(obj2))


# Calling methods using objects?
# obj1.method(arg1, arg2,....)




class Student:
   """
   This is a class Student to manage student information and activities
   """
   pass

s1 = Student()
s2 = Student()

# Doc strings => __doc__
print(Student.__doc__)

print(help(Student))