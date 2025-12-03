class Student:
   """
   This is a class Student to manage student info and activities
   """
   
   # study is method when we create function inside class these are called method
   def study(self, n_hours):
      print(f"self is: {self}")
      print(f"The student studies for {n_hours} hours a day!")
   
   def sports(self, sports_name):
      print(f"The student plays {sports_name}")

s1 = Student()   
print(f"The object: {s1}")
s1.study(3)
s1.sports("Football")

print("-------------------------")

s2 = Student()   
# print(f"The object: {s2}")
s2.study(5)
s2.sports("Cricket")

"""
When we call an instance method using the object/instance of the class, Python passes the object itself as the first argument to that method and That first argument is by standard is self
"""