# help(int)

# a = 10
# b = 20
# print(a + b) # a.__add__(b) => int.__add__(a,b)

# class A:
#    def f1(self, val):
#       pass

# obj = A()

# obj.f1(20) # A.f1(obj, 20)




class Rectangle:
   def __init__(self, length, breadth):
      self.length = length
      self.breadth = breadth


   def area(self):
      return self.length * self.breadth  

   def __add__(self, other):
      return self.length + other.length 
   
r1 = Rectangle(5, 3)
r2 = Rectangle(8, 6)
print(r1.area())
print(r2.area())

print(r1 + r2)
      