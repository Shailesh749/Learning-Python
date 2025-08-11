# learning operators
a=10
b=20

a=10
b=20
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(10%3) # give reminder value 1
print(5**2) # 5*5
print(5**3) # 5*5*5
print(10/3)
print(10//3) # floor division always return integer 3 ans


# Assignment operators in Python

# x++ not work in python
# x-- not work in python


x = 5
print(x)
x= x+5
print(x)
x +=5
print(x)
x-=5
print(x)


# Comparison Operators in Python
print("Comparison Operators")
y=10
z=20
print(y==z)
print(z!=y)
print(y>z)
print(y<z)
print(y>=z) # both false give false atleast one true give true
print(y<=z)



# Logical Operators in Python
print("Logical Operators")

d = 10
e = 20
print(d==10 and d<e and d==e)
print(d==10 or d<e or d==e)
print(d!=10 or d<e or d==e)

print( d!=10)
print(not d!=10)



# Membership Operators in Python
print("Membership Operators")
string1 = "hello"
print('H' in string1) # case sensitive in Python exact match
print('h' in string1)

number = [10, 20, 30, 40]
print(50 in number)
print(50 not in number)



# Identity Operators in Python
print("Identity Operators")
t= 10 
s= 10
print(t is s, x==y ) # both are same x==y and x is y, not different
print(t is not s, x!=y ) # both are same x==y and x is y, not different



# Bitwise Operators in Python
print("Bitwise Operators")

n= 10
m= 8
print(bin(n))
print(bin(m))

# AND Operators
print(bin(n&m))
#0b  1010
#0b  1000
#&0b 1000  8
print(bin(n&m), n&m)


# OR Operators
print(bin(n|m))
#0b  1010
#0b  1000
#|0b 1010  10
print(bin(n|m), n|m)


# XOR Operators
print(bin(n^m))
#0b  1010
#0b  1000
#^0b 0010  2