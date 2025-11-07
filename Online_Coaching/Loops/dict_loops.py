"""
We have the following dictionary containly details:

user = {
   "user_name": "my_user",
   "password": "test@123",
   "email": "my_user@example.com",
   "address": "ABC road, 111111",
   "country": "Australia"

}

Delete the sensitive information from the dictionary present in list

sensitive_info = ["password", "address"]
"""


# user = {
#    "user_name": "my_user",
#    "password": "test@123",
#    "email": "my_user@example.com",
#    "address": "ABC road, 111111",
#    "country": "Australia"

# }
# sensitive_info = ["password", "address"]

# for i in sensitive_info:
#    print(f"key: {i}, Value: {user[i]}")
#    user.pop(i)

# print(user)   







user = {
   "user_name": "my_user",
   "password": "test@123",
   "email": "my_user@example.com",
   "address": "ABC road, 111111",
   "country": "Australia"

}
sensitive_info = ["password", "address", "phone"]

for i in sensitive_info:
    if i in user:
      print(f"Deleted => key: {i}, Value: {user[i]}")
      user.pop(i)
    else:
       print(f"{i} is not present, cannot delete")   

print(user)   
