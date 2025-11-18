balance = 0.0
kyc_documents = {}
def check_balance():
   print(f"Your current balance is {balance}")
   print("======================")


def deposite(amout):
   global balance
   if amout > 0:
      balance += amout
   else: 
      print("Cannot deposite a negative amount or Zero amount")  
      print("======================") 

def withdraw(amount):
   global balance
   if amount <= 0:
      print("Cannot withdraw a negative amount or Zero amount") 
      print("======================") 
   elif amount > balance: 
      print("Cannot withdraw. Insuffient balance.")  
      print("======================")
   else:   
      balance -= amount



def Update_Kyc(docs):
   global kyc_documents
   kyc_documents.update(docs)



def check_kyc():
   if len(kyc_documents) == 0:
      print("KYC not done")
      print("======================")
   else:
      for doc in kyc_documents:
         print(f"{doc}: {kyc_documents[doc]}")  
      print("======================") 



if __name__ == "__main__":
   print("======================")
   print("Welcome to ABC bank!!!")
   print("======================")
   print()
   while True:
      print("1. Check your balance")
      print("2. Deposite an amount")
      print("3. Withdraw an amount")
      print("4. Check KYC")
      print("5. Update KYC")
      print("6. Quit")
      # print("Enter your choice (1-4): ")

      choice = (input("Enter your choice (1-6): "))
      print("======================")

      if choice == '1':
         check_balance()
      elif choice == '2':
         amt = float(input("Enter the amount to deposite: "))
         deposite(amt)
         print(f"Amount {amt} deposited sucessfully")
      elif choice == '3':
         amt = float(input("Enter the amount to withdraw: "))
         withdraw(amt) 
         print(f"Amount {amt} withdraw sucessfully")
         print("======================")
      elif choice == '4':
         check_kyc()
      elif choice == '5':
         kyc_docs = {}
         n_documents = int(input("Enter the number of documents you want to add: "))
         for i in range(n_documents):
            key = input("Enter the document type: ")
            value = input("Enter the document number: ")
            kyc_docs[key] = value
         Update_Kyc(kyc_docs)
         print("KYC Update!")
         print("======================")
      elif choice == '6':
         print("Quiting, have a nice day.")
         break
      else:
         print("Invalid choice!!! Re-try.")
         print("======================")
   print()
   print("Thank you for banking with us!")              