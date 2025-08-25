print('''
+ ADD
-SUBSTRACT
* MULTIPLY
/ DIVIDE                 
''')
# #  #using if elif else
# num1=int(input("Enter the Value num1:-"))
# num2=int(input("Enter the Value num2:-"))
# opr=input("Enter The Operator:-")
# if opr=="+":
#    print(num1+num2)
# elif opr=="-":
#      print(num1-num2)   
# elif opr=="*":
#      print(num1*num2)  
# elif opr=="/":
#      print(num1/num2) 
# else:
#      print("invalid Opr...") 




# #using if  else is  working in all condition that's we can't use else
# num1=int(input("Enter the Value num1"))
# num2=int(input("Enter the Value num2"))
# opr=input("Enter The Oprator:-")
# if opr=="+":
#    print(num1+num2)
# if opr=="-":
#      print(num1-num2)   
# if opr=="*":
#      print(num1*num2)  
# elif opr=="/":
#      print(num1/num2) 
# else:
#      print("invalid Opr...")   
   




#using if  elif is  working in all condition that's we  use elif

num1=int(input("Enter the Value num1:-"))
num2=int(input("Enter the Value num2:-"))
opr=input("Enter the Operator:-")
if opr=="+":
   print(num1+num1)
if opr=="-":
   print(num1-num2)
if opr=="*":
   print(num1*num2)
elif opr=="/":
   print(num1/num2)
if opr!="+" and opr!="-" and opr!="*" and opr!="/":
   print("invalid Oparator...")            