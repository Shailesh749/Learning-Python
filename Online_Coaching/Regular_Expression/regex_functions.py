# match()
import re
s1 = "We are learning regex in Python"
pat = r"[A-Z][a-z]"
match_obj = re.match(pat, s1)
print(match_obj)


pat = r"[a-z]{3}"
match_obj = re.match(pat, s1)
print(match_obj)


phones = "Jphn-1234567890, Shailesh-7492966727, Rajesh-8651463694"

pat = r"[0-9]{10}"
match_obj = re.search(pat, phones)
print(match_obj)


# findall()
pat = r"[0-9]{10}"
match_obj = re.findall(pat, phones)
print(match_obj)



phones = "Jphn-1234567890, Shailesh-7492966727, Rajesh-8651463694, Divya-764534878, Python3.13.5"

pat = r"[0-9]{10}"
match_obj = re.findall(pat, phones)
print(match_obj)

pat = r"[0-9]+"
match_obj = re.findall(pat, phones)
print(match_obj)


# fetch all phone numbers. the phone number are exactly 7 digits and should not exceed 15 digit 

pat = r"[0-9]{7,15}"
match_obj = re.findall(pat, phones)
print(match_obj)


# fetch all phone numbers. the phone number are atleast 7 digits 

pat = r"[0-9]{7,}"
match_obj = re.findall(pat, phones)
print(match_obj)



phones = "Jphn-1234567890, Shailesh-7492966727, Rajesh-8651463694, Divya-764534878, dada-87493742294924994324"

pat = r"\b[0-9]{7,15}\b"
match_obj = re.findall(pat, phones)
print(match_obj)



# finditer()

pat = r"\b[0-9]{7,15}\b"
match_obj_iter = re.finditer(pat, phones)
for matches in match_obj_iter:
   print(matches)