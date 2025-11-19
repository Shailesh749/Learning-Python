# raise

# salary = float(input("Enter Salary: "))

# if salary < 0:
#    raise ValueError("Salary cannot be negative!")
# else:
#    print(f"Your salary is {salary}")





# age = float(input("Enter your age: "))

# if age < 0:
#    raise ValueError("Age cannot be negative!")
# else:
#    if age >= 18:
#       print("You can vote")
#    else:
#       print("You cannot vote")   






age = float(input("Enter your age: "))

if age < 0:
   raise Exception("Age cannot be negative!")
else:
   if age >= 18:
      print("You can vote")
   else:
      print("You cannot vote") 