"""
reverse()
sort()
count()
Membership operation
"""

days_of_week = ["Mon", "Tue", "Wed", "Thu", "Fri", "sat", "sun"]
print(days_of_week)
# reverse()
days_of_week.reverse()
print(days_of_week)


nums = [4, 9, 0, 2, 8,1]
print(nums)
# sort()
nums.sort()
print(nums)
nums.sort(reverse=True)
print(nums)


# count()
# numbers = [0, 1, 3, 4, 1, 0, 5,0 , 0, 3, 0]
# print(numbers.count(0))


numbers = [0, 1, 3, 4, 1, 0, 5,0 , 0, 3, 0]

print(f"The list is: {numbers}")
item_to_count = int(input("Enter the number to be counted from above the list: "))
c= numbers.count(item_to_count)
print(f"Occurrance of{item_to_count} is {c}")



language = ["Python", "Java", "C++", "Python"]

print(language.count("Python"))
print("Python" in language)
print("Python" not in language)