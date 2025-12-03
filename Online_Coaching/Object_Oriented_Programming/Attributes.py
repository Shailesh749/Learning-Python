class Student:
   pass

s1 = Student()
s2 = Student()

s1.name = "Shailesh"
s1.roll = "1001"

print(s1.name)
print(s1.roll)

# print(s2.name)
# print(s2.roll)

# help(Student)

print(s1.__dict__)
print(s2.__dict__)