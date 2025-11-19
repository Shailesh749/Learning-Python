# students = {'student1': {'roll':101, 'name': 'John', 'percent': 95.5, 'sports':False},
#             'student2': {'roll':102, 'name': 'Shailesh', 'percent': 92.5, 'sports':False},
#             'student3': {'roll':103, 'name': 'Praneeth', 'percent': 81.5, 'sports':True}
#             }

# print(students)
# print(type(students))


"""
with open("students_info.txt", "xt") as fh:
   fh.write(str(students))
"""

# with open("students_info.txt", "rt") as fh:
#    for student in fh:
#       print(student)




# with open("students_info.txt", "rt") as fh:
#    content = fh.read()

# print(type(content))   





import pickle
students = {'student1': {'roll':101, 'name': 'John', 'percent': 95.5, 'sports':False},
            'student2': {'roll':102, 'name': 'Shailesh', 'percent': 92.5, 'sports':False},
            'student3': {'roll':103, 'name': 'Praneeth', 'percent': 81.5, 'sports':True}
            }

print(students)
print(type(students))


# Serialization 
with open("students.bin", "bw") as fh:
   for student in students:
      pickle.dump(students[student], fh)


# Deserialization
with open("students.bin", "rb") as fh:
   # print(pickle.load(fh))      
   # print(pickle.load(fh))      
   # print(pickle.load(fh))   

   data1 = pickle.load(fh)
   print(data1, type(data1))   
   data2 = pickle.load(fh)
   print(data2, type(data2))   
   data3 = pickle.load(fh)
   print(data3, type(data3))   