"""
Class methods are methods defined inside the class that are bound to the class
To create a class method, we use a decorator -> classmethod
"""

# class Welcome:
#    @classmethod
#    def greet(cls):
#       print(cls)
#       print("Hello")

# w1 = Welcome()   
# w1.greet()   
# print(Welcome)







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
      print(f"The student plays {sports_name} in the college {self.college_name}")


   @classmethod
   def greet(cls):
      print(cls)
      print(f"Welcome to {cls.college_name} the college")

   @classmethod
   def get_departments(cls):
      print(f"Departments in {cls.college_name} are:")  
      for department in cls.departments: 
         print(department)
         

student1 = Student('Shailesh', 1001)  
student1.study(3) 
student1.greet() 
student1.sports("Football") 
student1.get_departments()


