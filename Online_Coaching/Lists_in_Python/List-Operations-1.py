# Slicing of lists

l1 = [3, 8, 1, 0, 4,9,7,3,6]
print(l1[1:6:1])
print(l1[2:6:2])


# concatenation of lists
l1 = [1,7,2]
l2 = [0,5]
print(l1+l2)
print(l2+l1)

#Repeatation of lists

# *
print(l2 *3)

# append()
#adds an item to the end of the list

fruits = ["mango", "apple", "orange"]
print(fruits)
# Syntax : list.append(item) 
fruits.append("banana")
print(fruits)


# insert 
# adds an element before the specified index
# Syntax : list.insert(inde, item)

fruits.insert(2, "guava")
print(fruits)