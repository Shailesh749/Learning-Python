# Opening a file in Python
# open(file_name, mode_to_open)
# Modes: r, x, w, a, t, b => 'rt' is the default mode


file_handler = open("practice.txt", 'rt')
print(file_handler)
# Read operation
# read() => reads the contents of the file as str

# content = file_handler.read()
#content = file_handler.read(10) 
# this reads first 10 characters of the file

# readline()
'''
line1 = file_handler.readline()
line2 = file_handler.readline()
line3 = file_handler.readline()
line4 = file_handler.readline()
# Empty string => the file has reached End of File (EOF)
'''


# readlines()
lines = file_handler.readlines()

# Closing a  file => close()

file_handler.close()

# print(content)
# print(type(content))

"""
print(f"Line 1: {line1}")
print(f"Line 2: {line2}")
print(f"Line 3: {line3}")
print(f"Line 4: {line4}")
"""


print(f"Lines: {lines}")
print(type(lines))

for line in lines:
   print(line.rstrip('\n'))