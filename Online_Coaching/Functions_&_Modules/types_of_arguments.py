# def add(a, b):
#    return a + b

# Positional arguments - Passing the arguments in order of their position

# result = add(10, 40)




# Default arguments

# def add(a, b=10):
#     print(f"a: {a}, b: {b}")
#     return a + b

# result = add(10)
# result = add(10, 5)
# print(result)




# def add(a, b=10, c):
#    print(f"a: {a}, b:{b}, c: {c}")
#    return a + b + c
# result = add(10, 20,30)
# print(result)

# It will give error
# The non-default arguments should NOT follow the default arguments




# def add(a, c, b=10, ):
#    print(f"a: {a}, b:{b}, c: {c}")
#    return a + b + c
# result = add(10, 20,30)
# print(result)

# it will run




# def add(a,  b=10, c=20):
#    print(f"a: {a}, b:{b}, c: {c}")
#    return a + b + c
# result = add(10)
# print(result)



def add(a,  b=10, c=20):
   print(f"a: {a}, b:{b}, c: {c}")
   return a + b + c

# Keyword agruments
result = add(10, c=50, b=20)
print(result)