class Contact:
   phone_directory = []

   def __init__(self, name, phone_number):
      self.name = name
      self.phone = phone_number
      Contact.phone_directory.append(self)
      

   def show_contact(self):
      return f"Name: {self.name}, Contact number: {self.phone}"
   
   @classmethod
   def show_all_contact(cls):
      if len(cls.phone_directory) == 0:
         print("No contacts found in the directory!")
      else:
         print("All contacts from the directory!!")
         for contact in cls.phone_directory:
             print(contact.show_contact())


   @classmethod
   def search_contact(cls, search_name):
      for contact in cls.phone_directory:
         if contact.name.lower() == search_name.lower():
            return contact.phone

      return f"No contact found for {search_name}"  


   @staticmethod
   def validate_phone_number(number):
      if len(number) >= 8 and number.isdigit():
         return True
      else:
         return False

n_contacts = int(input("How many contacts do you want to add?: "))

for i in range(n_contacts):
   name = input("Enter the name of the contact: ")
   phone_number = input("Enter the phone number: ") 
   if Contact.validate_phone_number(phone_number):
         Contact(name, phone_number)
   else:
      print(f"Invalid phone number for {name}, phone number should be atleast 8 digits and should only contain number {phone_number}")      


# c1 = Contact('Shailesh', 7492966727)
# c2 = Contact('Praneeth', 8581867756)
# c3 = Contact('Rajveer', 8434943149)
# print(Contact.phone_directory)

# print(c1.show_contact())
# print(c2.show_contact())

# c1.show_all_contact()

Contact.show_all_contact()

# print(Contact.search_contact('Raju'))
# print(Contact.search_contact('Shailesh'))