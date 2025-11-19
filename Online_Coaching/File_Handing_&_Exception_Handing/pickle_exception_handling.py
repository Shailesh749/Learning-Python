import pickle

students = {'student1': {'roll':101, 'name': 'John', 'percent': 95.5, 'sports':False},
            'student2': {'roll':102, 'name': 'Shailesh', 'percent': 92.5, 'sports':False},
            'student3': {'roll':103, 'name': 'Praneeth', 'percent': 81.5, 'sports':True}
            }

print(students)
print(type(students))


# Serialization
with open("students.bin", 'bw') as fh:
   for student in students:
      # pickle.dump(student, fh)
      pickle.dump(students[student], fh)


# Deserialization
"""
with open("students.bin", "rb") as fh:
   data1 =  pickle.load(fh)
   print(data1, type(data1))
   data2 =  pickle.load(fh)
   print(data2, type(data2))
   data3 =  pickle.load(fh)
   print(data3, type(data3))
"""




"""
with open("students.bin", "rb") as fh:
   while True:
      try:
         data = pickle.load(fh)
         print(data, type(data))
      except EOFError:
         print("Done!")
         break   
         
"""



# Print the names of the students as a list who secured 90 or more percent

students_list_90 = []
with open("students.bin", "rb") as fh:
   while True:
      try:
         data = pickle.load(fh)
         if data['percent'] >= 90:
            # print(data['name'])
            students_list_90.append(data['name'])
      except EOFError:
         print("Done!")
         break 

print(f"List of students_list_90 is {students_list_90}")      