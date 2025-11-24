import re

with open("student_details.txt", "rt") as fh:
   data = fh.read()
# pattern = r"[a-zA-Z]+[a-zA-Z0-9_.-]+[@][a-z]+[.][a-z]+"
# pattern = r"\b[a-zA-Z]+[\w.-]+[@][a-z]+[.][a-z]+\b"
pattern = r"\b[a-zA-Z]+[\w.-]+[@][a-z]+[.][a-z]{2,}\b"
match_obj = re.finditer(pattern, data)

for matches in match_obj:
   print(matches)