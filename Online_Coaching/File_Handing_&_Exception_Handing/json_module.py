import json

students = {'student1': {'roll':101, 'name': 'John', 'percent': 95.5, 'sports':False},
            'student2': {'roll':102, 'name': 'Shailesh', 'percent': 92.5, 'sports':False},
            'student3': {'roll':103, 'name': 'Praneeth', 'percent': 81.5, 'sports':True}
            }
print(students)
print(type(students))


# dump()

# with open("student_data.json", "x") as fh:
#    json.dump(students, fh)

# this will create the json file



# with open("student_data.json", "w") as fh:
#    json.dump(students, fh, indent=4)

# this is for write    




# load()

# with open("student_data.json", "r") as fh:
#    data = json.load(fh)

# print(data)
# print(type(data))   




"""
# update()

# read the old data from the json file
with open("student_data.json", "r") as fh:
   data = json.load(fh)
# update operation   
data.update(students)  

# dump - write the updated data in the json file

with open("student_data.json", 'w') as fh:
   json.dump(data, fh, indent=4)

"""  



# update()

# read the old data from the json file
try:
   with open("student_data.json", "r") as fh:
      data = json.load(fh)
except FileNotFoundError: 
   with open("student_data.json", 'w') as fh:
     json.dump(students, fh, indent=4)
else:          
   # update operation   
   data.update(students)  

   # dump - write the updated data in the json file

   with open("student_data.json", 'w') as fh:
      json.dump(data, fh, indent=4)