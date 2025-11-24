import re
message = "The current Python version is 3.85. Other previous version are 3.13, 3.12, 3.11, 3.10."

match_object = re.search("[0-9][0-9]", message)
print(match_object)

match_object = re.search("[0-9][0-9]", "House number: 251/A")
print(match_object)

match_object = re.search("[0-9][0-9][0-9]", "House number: 251/A")
print(match_object)

match_object = re.search("[0-9].[0-9]", "House number: 251/A")
print(match_object)



# dot . matches any character except new line character (\n)



message_1 = "The year is 2011"
match_object = re.search("[0-9].[0-9][0-9]", message_1)
print(match_object)

match_object = re.search("[0-9][.][0-9][0-9]", message_1)
print(match_object)


match_object = re.search("[0-9][.][0-9][0-9]", message)
print(match_object)