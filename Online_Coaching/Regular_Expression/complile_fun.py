import re

phones = "Alice-1234567890, Mark-7492966727, Praneeth-9349373354"

pattern = r"\d{10}"
pattern_compiled = re.compile(pattern)
print(pattern_compiled)
print(type(pattern_compiled))
# math_obj = re.findall(pattern, phones)
math_obj = re.findall(pattern_compiled, phones)
print(math_obj)



with open("student_details.txt", "rt") as fh:
   data = fh.read()
print(data) 
print(type(data))  

phone_matches = re.finditer(pattern_compiled, data)
print(phone_matches)

for matches in phone_matches:
   print(matches)