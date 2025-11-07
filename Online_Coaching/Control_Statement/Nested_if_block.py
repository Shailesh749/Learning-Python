marks = float(input("Enter Your marks: "))

if marks >= 60:
   print("Congrats, you has passed the exam")
   if marks >= 90:
      print("Grade is A")
   elif marks >= 80 and marks < 90:
      print("Grade B")
   elif marks >= 70 and marks < 80:
      print("Grade c")
   elif marks >= 60 and marks < 70:
      print("Grade d")
   else:
      print("Your grade is C")
else:
   print("You have failed, study hard next time")   