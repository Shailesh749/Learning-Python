import re
s1 = "Python is a programming language. python3.13 is the current version"

# [A-Z], [a-z]

# pat = "old\n"
# pat = r"old\n"
# print(pat)


# pat = r"[a-z][a-z]"
# match_object = re.search(pat, s1)
# print(match_object)

# pat = r"[A-Z][a-z][a-z]"
# match_object = re.search(pat, s1)
# print(match_object)



# \d and \D
# \d matches 1 digit character. It is similar to [0-9]

pat = r"[a-z][a-z][a-z]\d"
match_object = re.search(pat, s1)
print(match_object)



# \D matches 1 non-digit character. It is similar to [0-9]
pat = r"[a-z][a-z][a-z]\D"
match_object = re.search(pat, s1)
print(match_object)



# \s, \S
# \s  matches aby whitespace character , tab and new line
pat = r"[a-z][a-z][a-z]\s"
match_object = re.search(pat, s1)
print(match_object)



s2 = """Hi there
We are learning Python
"""
pat = r"[a-z][a-z][a-z]\s"
match_object = re.search(pat, s2)
print(match_object)



# \S => opposite of \s. It matches any character except, space, \n and \t
pat = r"[a-z][a-z][a-z]\S"
match_object = re.search(pat, s2)
print(match_object)




# \w - matches [a-z], [A-Z], [0-9], _

pat = r"[a-z][a-z][a-z]\w"
match_object = re.search(pat, s2)
print(match_object)



# \W -opposite of \w - matches a character except  [a-z], [A-Z], [0-9], _

pat = r"[a-z][a-z][a-z]\W"
match_object = re.search(pat, s2)
print(match_object)