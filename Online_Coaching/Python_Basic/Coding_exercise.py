# calculat the area of triangle

# a = float(input("Enter first side: "))
# b = float(input("Enter second side: "))
# c = float(input("Enter third side: "))

# s= (a + b + c) /2
# area = (s * (s-a)* (s-b) * (s-c)) **0.5
# # print("Area of triangle with given side is", area)
# print("Area of triangle with given side is", round(area, 2))





# Calculate Simple interest

# principal = float(input("Enter principal amout: "))
# rate = float(input("Enter interest rate: "))
# time = float(input("Enter time : "))

# si = (principal * rate * time) / 100
# print("Simple interest is", si)





# Calculate Compound Interest

principal = float(input("Enter principal amout: "))
rate = float(input("Enter interest rate: "))
time = float(input("Enter time : "))

amount1 = principal * (1 + rate/100) ** time
amount2 = principal * pow((1 + rate/100) ,time)

print(amount1, amount2)
print(round(amount2, 2))

ci = amount2 - principal
print("Compound interest", round(ci))


# (b*h)*(1/2)