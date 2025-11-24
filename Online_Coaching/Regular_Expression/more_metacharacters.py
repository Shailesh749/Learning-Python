# ^ - Caret it checks only starting point
import re
s1 = "Python is a programming languege"

pat = r"[a-z]{8}"
match_obj = re.search(pat, s1)
print(match_obj)


pat = r"^[a-z]{8}"
match_obj = re.search(pat, s1)
print(match_obj)


# $ - doller - end of the string
pat = r"[a-z]{8}$"
match_obj = re.search(pat, s1)
print(match_obj)



# group -() + | (or)

emails = "abc_123@example.com random words and characters. x1y2z3.abc.edu"
pat = r"(com|edu)"
match_obj = re.search(pat, emails)
print(match_obj)


pat = r"(com)"
match_obj = re.search(pat, emails)
print(match_obj)