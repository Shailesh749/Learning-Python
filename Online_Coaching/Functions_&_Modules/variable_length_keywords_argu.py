# **kwargs - variable length keyword arguments

# def func( **kwargs):
#    print(kwargs, type(kwargs))

# func(x= 10, y = 20)   




# def student_details(sid, sname, **marks):
#    if len(marks) == 0:
#       print(f"{sname} did not attend the exam")
#    else:   
#      percent = sum(marks.values()) / len(marks)
#      print(f"{sname} with id {sid}, secured {percent}%")

# student_details(101, "shailesh", sub1=78.5, sub2=89.5, sub3=67.7)     
   





def student_details(sid, sname,*extra, **marks):
   if len(marks) == 0:
      print(f"{sname} did not attend the exam")
   else:   
     percent = sum(marks.values()) / len(marks)
     print(f"{sname} with id {sid}, secured {percent}%")

   print(f"{sname} does {extra}")  

student_details(101, "shailesh", 'cricket', sub1=78.5, sub2=89.5, sub3=67.7)     
student_details(101, "shailesh", 'Cricket','Playing', sub1=78.5, sub2=89.5, sub3=67.7)     