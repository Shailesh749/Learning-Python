# Mutability & Immutability
# Lists are mutable
# Tuples and Strings are immutable

s1 = "Python is fun"
s2 = s1.replace("Python", "Java")
print(s1)
print(s2)

# s1[0] = 'p' # it will give error 


l1 = ['mango', 'orange', 'aple']
print(id(l1))
l1.append("Banana")
print(l1)
print(id(l1))

l1[-1] = "Apple"

print(l1)
print(id(l1))