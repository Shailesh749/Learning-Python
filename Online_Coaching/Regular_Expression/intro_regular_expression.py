# Regular Expression (RegEx) - re module

import re
message = "The current Python version is 3.85. Other previous version are 3.13, 3.12, 3.11, 3.10."

"""
# if Python is present in message
print("Python" in message)
print("85" in message)

print(message.find('3.85'))
print(message.find('Python'))
"""


"""
re.search(regex_pattern, string) => returns a match object when there is a match found, else returns None
"""

match_obj = re.search('13', message)
print(match_obj)

if re.search('13', message):
   print("Found!")
else:
   print("Not found!")  

print(message[32:34])    