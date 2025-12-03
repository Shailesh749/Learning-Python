"""
Static method - method defined inside a class which is neither bound to the object nor to the class
To create a static method, we use staticmethod decorator
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
      print(f"The {self.name} studies for {n_hours} hours a day!")
   
   def sports(self, sports_name):
      print(f"The student plays {sports_name} in the college {self.college_name}")


   @staticmethod
   def greet():
      print(f"Welcome to  the college")

   @classmethod
   def get_departments(cls):
      print(f"Departments in {cls.college_name} are:")  
      for department in cls.departments: 
         print(department)
         


# help(Student)

student1 = Student('Shailesh', 1001)
student1.study(3)
student1.get_departments()
student1.greet()


student2 = Student('Praneeth', 1002)
student2.study(3)
student2.get_departments()
student2.greet()
