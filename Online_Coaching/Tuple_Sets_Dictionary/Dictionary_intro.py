# comma separated Key-Value pairs enclosed within {}

# {key1:value1, key2:value2, ....}

groceries = {'milk': 60,'biscuite':20, 'rice':90, 'bread': 30}

print(groceries)
print(type(groceries))
print(len(groceries))
# print(groceries[0])
# it doesn't have indexes

print(groceries['milk'])

# dictionary are mutable
groceries['milk'] = 65
print(groceries)


# print(groceries['eggs'])
# error give

groceries['eggs'] = 10
# adds new key-value pair to the dictionary
groceries['bread'] = 35
# update the values of the key
print(groceries)

