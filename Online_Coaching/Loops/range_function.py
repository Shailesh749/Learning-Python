# range() - built in function used to generate sequence of integers in a given intervel

# range(start, stop, step) stop is not included

# for i in range(1, 11, 1):
#    print(i)


# for i in range(1, 11, 2):
#    print(i)



# generate even numbers between 1 and 10 (10 excluded)

# for i in range(2 , 10, 2):
#    print(i)


# generate even numbers reverse order between 20 and 10 (10 excluded)

# for i in range(20 , 10, -2):
#    print(i)



# Countdown from 10 to 1 (1 included)
# for i in range(10, 0, -1):
#    print(i)
# print("Happy New Year")   




# range(start, stop) => 1 by default

# for i in range(1, 5):
#    print(i)

# range(stop) = > 0 to stop-1 with a step of 1

# for i in range(5):
#    print(i)




# groceries = ['salt', 'milk','sugar']
# for item in groceries:
#    print(item)

# for index in range(len(groceries)):
#    print(index)



profits = [9, 11, 6, 10]

for index in range(len(profits)):
   q = index + 1
   print(f"Profits for quarter {q} is {profits[index]}")