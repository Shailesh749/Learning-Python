student1 = {"maths": 80.5, "eng":76.0, "phy":89.0}
print(student1)

# fetch the marks for "phy"
print(student1["phy"])

# get()
print(student1.get("phy"))
print(student1.get("chem")) # None
print(student1.get("chem", 40.0)) 


emp1 = {'id': 1001, 'name': 'John', 'salary': 10000}
print(emp1.get('phone', 90000))
print(emp1.get('id', 90000)) # 1001


# memship operator => in

print(1001 in emp1) # False
print('name' in emp1) # True


emp1['phone'] = 7492966727
print(emp1)



sem1_marks = {'maths':78.5, 'eng':71.0, 'phy': 86.5}
sem2_marks = {'chem':81.5, 'bio':90.5}

sem1_marks.update(sem2_marks)
print(sem1_marks)



groceries_1 = {'milk': 60, 'rice': 100, 'biscuits': 20}
groceries_2 = {'rice': 110, 'bread': 30 }

groceries_1.update(groceries_2)
print(groceries_1)


# pop()
groceries_1.pop('milk')
print(groceries_1)


groceries_3 = {'milk': 60, 'rice': 100, 'biscuits': 20, 'milk':65}
print(groceries_3)


# key cannot be duplicated in a dict