# __init__() method
# is an instance method
# is used to create and initialize the attributes during the object creation


class Student:
   """
   This is a class Student to manage student info and activities
   """
   
   # study is method when we create function inside class these are called method

   def __init__(self, name, roll, dept):
      print(f"Calling the initializer for {self}")
      self.name = name
      self.roll = roll
      self.department = dept

   def study(self, n_hours):
      print(f"self is: {self}")
      print(f"The student studies for {n_hours} hours a day!")
   
   def sports(self, sports_name):
      print(f"The student plays {sports_name}")


student1 = Student("Shailesh", 1001, "Science")   
#object_name.attribute_name = value
student2 = Student("Praneeth", 1002, "Maths")

print(student1.name, student1.roll, student1.department)
print(student2.name, student2.roll, student2.department)

print(student1.__dict__)
print(student2.__dict__)



"""
Instance variables/attributes are different for different objects
"""


student1.grade = "B"

print(student1.__dict__)
print(student2.__dict__)

student3 = Student("Raju", 1003, "Arts")
print(student3.__dict__)