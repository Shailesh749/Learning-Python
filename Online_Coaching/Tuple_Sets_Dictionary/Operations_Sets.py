student1 = {"English", "maths", "Cs", "Chemistry", "Physics"}
student2 = {"English", "Biology",  "Chemistry", "Physics"}
student3 = {"Sanskrit", "Maths", "CS"}

# common subjects of student1 and student2 - intersection

# common_subjects = student1.intersection(student2)
# common_subjects = student1 & student2
# print(common_subjects)
common_subjects = student1.intersection( student2, student3)
print(common_subjects)


# all subjects of student1 AND student1 - union

# all_subjects = student1.union(student2, student3)
all_subjects = student1 | student2 | student3
print(all_subjects)


days = {"Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"}
weekends = {"Sat", "Sun"}

# difference of sets

# weekdays = days - weekends 
weekdays = days.difference(weekends) 
# elements of days which are Not in weekends

print(weekdays)