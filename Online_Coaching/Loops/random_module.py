import random

# random() - returns random float between 0.0 and 1.0 (excluded)

# print(random.random())
# print(random.random())



# randint(a, b) => returns random int between a and b (both included)

# print(random.randint(10, 15))




# choice(sequence) => returns a random item from the sequence 
# nums = [10, 4, 1, 8, 4, 3]
# nums = ['apple', 'orange', 'banana', 'guava', 'mango']

# print(random.choice(nums))





# shuffle(sequence) => returns the elements shuffled in random order

nums = ['apple', 'orange', 'banana', 'guava', 'mango']

random.shuffle(nums)
print(nums)