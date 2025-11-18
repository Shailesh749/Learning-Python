"""
Recursion is a process in which a function calls itself till a certain condition is not met

Factorial of n => n * (n-1) * (n-2) * .... 2 *1
n!
4! = 4 * 3 * 2 *1 = 24
"""

# without Recursion
# def fact(num):
#   factorial = 1
#   while num > 1:
#     factorial *= num
#     num -= 1

#   return factorial  
# n = 4
# print(f"Factiorial of {n} is {fact(n)}")



# There are two parts to any recursive function
# 1. Base/terminal condition
# 2. Recursive condition
# n! => n *(n-1) * (n-2) * .... * 2 * 1

# With Recursion

def fact_rec(num):
   if num == 1:
      return 1
   else:
      factorial = num * fact_rec(num-1) # ye function khudko call karega
      return factorial
n = 5   
print(f"Factiorial of {n} is {fact_rec(n)}")  