# def even_odd(number):
#    if number % 2 == 0:
#       print(f"The Number is {number} Even")
#    else:
#       print(f"The number is {number} Odd")  

# result = even_odd(10)  
# print(result)  # none





# def even_odd(number):
#    if number % 2 == 0:
#       return "Even"
#    else:
#       return "Odd" 

# result = even_odd(10)  
# print(result) 
      



# def add(num1, num2):
#    result = num1 + num2
#    return result

# val_1 = int(input("Enter the num1: "))
# val_2 = int(input("Enter the num2: "))

# val = add(val_1, val_2)
# print(f"Addition of {val_1} and {val_2} is {val}")




# Multiple value return 
def arithmetic(num1, num2):
   add = num1 + num2
   sub = num1 - num2
   mul = num1 * num2
   div = num1 / num2
   return add, sub, mul, div

val_1 = int(input("Enter the num1: "))
val_2 = int(input("Enter the num2: "))

res1, res2, res3, res4 = arithmetic(val_1, val_2)
print(f"Addition of {val_1} and {val_2} is {res1}")
print(f"Substraction of {val_1} and {val_2} is {res2}")
print(f"Multiplication of {val_1} and {val_2} is {res3}")
print(f"Divide of {val_1} and {val_2} is {res4}")