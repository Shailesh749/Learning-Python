"""
concatenation , repeatation, membership, count, index, min , max, sum
"""

# student_detail1 = (1001, "John")
# student_detail2 = (78.5, 91.0, 83.5, 79.5)
 
# # +
# student_details = student_detail1 + student_detail2
# print(student_details)

# # *
# t1 = ("Class 5", 5000)
# print(t1 * 3)




student_detail1 = (1001, "John")
student_detail2 = (78.5, 91.0, 83.5, 79.5)
 
# in, not in
print(91.0 in student_detail2) 
print(99.0 not  in student_detail2) 



# count
t1 = (10, 4, 1, 9 , 0, 3, 1)
# tuple.count(element)
print(t1.count(1))


# index
t2 = (10, 4, 1, 9 , 0, 3, 1)
# tuple.index(element)
print(t2.index(1))

print(max(t2))
print(min(t2))
print(sum(t2))