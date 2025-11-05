"""
extend()
remove()
pop()
"""


# extend
fruits = ["apple", 'Mango', "orange", "Mango"]
fruits.append(["Banana" , "Grapes"])
fruits.extend(["Banana" , "Grapes"])
print(len(fruits))
print(fruits)

fruits.remove("Mango")
print(fruits)

fruits.pop(3)
fruits.pop(-1)
fruits.pop()
print(fruits)