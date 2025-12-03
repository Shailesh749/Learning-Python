class A:
   def add(self, num1, num2):
      return num1 + num2
   

   def add(self, num1, num2, num3):
      return num1 + num2 + num3
   

obj = A()
# print(obj.add(10, 20))
print(obj.add(10, 20, 30))

# method overloading is not work in python