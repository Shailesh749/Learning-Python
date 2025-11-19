"""
Compile time error => Syntax error $ Indentation error

2. Exceptions => error during execution
"""

# How to handle exceptions? => try-except block



try:
   num1 = int(input("Enter a number: "))
   num2 = int(input("Enter another number: "))
   result = num1 / num2
   print(result)
except ZeroDivisionError:
      print("The denominator cannot be 0")
except ValueError:
     print("Input should only be digits")      