# Tuple
# (item1, item2, ....)
# sequence of items as a collection

t1 = ("Python", 10, 1.5, True, [1,2,4], (10,20))
print(len(t1))

# Accessing items of a tuple - index
print(t1[0])
print(t1[-1])


# t2 = (10, 20, 30)
t2 = 10, 20, 30
print(t2)
print(type(t2))


l1 = [1, 2, 3]
print(l1, type(l1))
t3 = tuple(l1)
print(t3)
print(t3, type(t3))


fruits = ("mango", "orange", "apple")
print(fruits, type(fruits))
fruits = list(fruits)
print(fruits, type(fruits))