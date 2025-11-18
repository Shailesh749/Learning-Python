# *args - variable length positional arguments (0 to n)

# def add(*args):
#    print(args, type(args))

#    return sum(args)

# result = add(10, 20, 6) 
# print(result)  




# def add(*nums):
#    print(nums, type(nums))

#    return sum(nums)

# result = add(10, 20, 6) 
# print(result)  





def student_details(sid, sname , *marks):
   if len(marks) == 0:
      print(f"{sname} with is {sid} was absent!")
   else:   
      percent = sum(marks) / len(marks)
      print(f"{sname} with id {sid} secured {percent}%")

student_details(101, "Shailesh", 89, 69, 78, 90, 89)   
student_details(102, "Praneeth", 89, 69, 88, 90, 89)   
student_details(103, "Rahul", 89, 69, 89, 90, 89)   
student_details(104, "raju")   