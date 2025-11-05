import copy

l1 = [1,2.5, [10, 20, 30], 'Python']

# shallow copy
# l2 = copy.copy(l1)
# print(l2)
# print(id(l1))
# print(id(l2))

# l1[0] = 100
# l1[2][0] = 50
# print(f"l1 -> {l1}", id(l1))
# print(f"l2 -> {l2}", id(l2))




# deep copy
l2 = copy.deepcopy(l1)
print(l2)
print(id(l1))
print(id(l2))

l1[0] = 100
l1[2][0] = 50
print(f"l1 -> {l1}", id(l1))
print(f"l2 -> {l2}", id(l2))



d1 = {'id': 1111, 'name':'John', 'marks': {'eng':71.5, 'phy': 68.5, 'maths':80}}
d2 = copy.deepcopy(d1)
d1['name'] = "Dan"
d1['marks']['maths'] = 90.4
print(f"d1 -> {d1}", id(d1))
print(f"d2 -> {d2}", id(d2))