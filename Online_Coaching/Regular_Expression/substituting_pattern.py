import re

# sub()
s1 = "Sunday, Monday, Tuesday, Monday, Sunday"
pat = "Sunday"
replacement = "Friday"

result = re.sub(pat, replacement, s1)
print(result)

result = re.sub(pat, replacement, s1, count=1)
print(result)


s1 = "Sunday, Monday, Tuesday, Monday, Sunday, Saturday"
pat = r"S[a-z]+"
replacement = "Friday"

result = re.sub(pat, replacement, s1)
print(result)


message = """We are learning re. Using RE, we can search for a pattern in a given string. Using the sub(), We can replace the pattern with a given string as well."""

patt = r'\bre\b'
replacement = "Regular Expression"
# result = re.sub(patt, replacement, message)
result = re.sub(patt, replacement, message, flags=re.IGNORECASE)
print(result)



phone_nums = "+91-1234567890, +91-999999999"
pattern = r"[+-]"
replacement = ""
result = re.sub(pattern, replacement, phone_nums)
print(result)