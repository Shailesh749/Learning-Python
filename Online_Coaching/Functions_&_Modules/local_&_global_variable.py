# n = 1 # GLOBAL VARIABLE 

# def fn():
#    n = 5  # Local VARIABLE
#    print('in', n)

# fn()

# print('out', n)





n = 1 # GLOBAL VARIABLE 

def fn():
   global n
   n = 5  
   print('in', n)

fn()

print('out', n)
