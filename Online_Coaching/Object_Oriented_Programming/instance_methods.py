# Instance method
# defined inside a class which is bound to/ associated with the instance/object

# help(list)


# class Student:
#    """
#    This is a class Student to manage student info and activities
#    """
   
#    # study is method when we create function inside class these are called method
#    def study():
#       print("The student studies for 3 hours a day!")
   
# s1 = Student()   
# print(s1)

# s1.study()





class Student:
   """
   This is a class Student to manage student info and activities
   """
   
   # study is method when we create function inside class these are called method
   def study(self):
      print(f"self is: {self}")
      print("The student studies for 3 hours a day!")
   
s1 = Student()   
print(f"The object: {s1}")

s1.study()

"""
When we call an instance method using the object/instance of the class, Python passes the object itself as the first argument to that method and That first argument is by standard is self
"""