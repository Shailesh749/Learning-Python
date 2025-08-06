#Number
print("Print number data type")

a=5
print(a, type(a)) #int
a=5.5
print(a, type(a)) #float
a=2+5j
print(a, type(a)) #complex


#String
print("Print string data type")
s= "Hello@123"
print(s, type(s)) #str

s='''
    Hello
    Welcome to Shailesh 
'''
print(s, type(s))


s="10"
print(s, type(s)) #str



#List
print("Print List data type")
l= [10, 'sh', 5.5]
l[2]=10
print(l, type(l))



#Tuple
print("Print Tuple data type")
t=(10, 20, 'hello')
# t[1]=30 we can't modify or change tuple value
print(t, type(t))
t=(10)
print(t, type(t))



#Dictionary
# key always uniq
print("Print Dictionary data type")
d= {
   'course_name':'Python',
   'course_duration':'2 Month'
}
print(d, type(d))
print(d['course_name']) #data value get



#Set
# set cannot accept duplicate value he removed duplicate value
print("Print Set data type")
s={10, 20, 30, 10}
print(s, type(s))