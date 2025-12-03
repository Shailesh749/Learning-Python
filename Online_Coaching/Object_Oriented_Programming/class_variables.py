"""
Class variables are defined at the class level.
Same copy of the class variables are shared among the objects
"""

class Student:
   """
   This is a class Student to manage student info and activities
   """
   college_name = "ABC college"
   departments = ['Arts', "Commerce", "Science"]
   
   # study is method when we create function inside class these are called method

   def __init__(self, name, roll):
      print(f"Calling the initializer for {self}")
      self.name = name
      self.roll = roll
      

   def study(self, n_hours):
      print(f"self is: {self}")
      print(f"The student studies for {n_hours} hours a day!")
   
   def sports(self, sports_name):
      print(f"The student plays {sports_name}")


student1 = Student("Shailesh", 1001)

help(Student)
print(student1.__dict__)

print(student1.departments)
print(student1.college_name)
print(Student.departments)
print(Student.college_name)


student2 = Student("Praneeth", 1002)
print(student2.departments)
print(student2.college_name)