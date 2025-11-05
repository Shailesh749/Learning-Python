# d1 = {[1,3,5]: 9, [1, 2,1]:4}
# print(d1) # error

# keys cannot be lists, set, dict => mutable datatypes
# allowed keys - str, int, float, bool, tuple => immutable datatypes

# keys of a dictionary can only be mutable datatypes!!



d2 = {'Nine': 9, 'Four': 4}
print(d2)

# d3 = {1:True, 0: False}
# d3 = {True: 1, False: 0}
# d3 = {(1,2,3): 6, (1,2): 3}
# d3 = {{1,2,3}: 6, {1,2}: 3}
# d3 = {{'a':1, 'b':2}: 6}
# print(d3)




# Values can be any datatype

# d4 = {'id': 1001, 'name': 'John', 'marks': [89.5, 71.5, 81.0]}
d4 = {'id': 1001, 'name': 'John', 'marks': {'eng':89.5, 'maths':71.5, 'bio':81.0}}
print(d4)
print(d4['marks'])
# print(d4['marks'][1])
print(d4['marks']['maths'])


# fetch the keys?
# keys()
print(d4.keys())
print(d4.keys(), type(d4.keys()))

# values()

print(d4.values())
print(d4.values(), type(d4.values()))


#items()
print(d4.items())
print(d4.items(), type(d4.items()))