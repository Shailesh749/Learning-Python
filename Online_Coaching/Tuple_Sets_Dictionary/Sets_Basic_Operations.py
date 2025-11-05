# Membership operator - in, not in

nums = {1, 3, 2, 0, -1}
print(0 in nums)
print(10 not in nums)

# we cannot concate sets
nums2 = {6, 5, 4, 8, -2}
# print(nums+nums2)

# we cannot repeating 
# print(nums2 * 2)


weekdays = ("Mon", "Tue", "Wed", "Thu", "Fri")
weekdays = set(weekdays)
print(weekdays)

# sets are not sequationally data and unorder data structure data 


# Sets are mutable

set4 = {2, 0, -1}
# set4[0] = 10  # error give

# add()
set4.add(5)
set4.add(0)
print(set4)
set4.remove(0)
print(set4)

# discard() working like delete
set4.discard(2)
print(set4)