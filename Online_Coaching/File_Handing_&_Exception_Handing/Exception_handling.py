# try:
#    with open("my_file.txt", 'rt') as fh:
#       data = fh.read()

#    print(data) 
# except FileNotFoundError as file_err:
#    print("File that you are trying to open does not exist!") 
#    print(file_err)    






# try:
#    with open("file1.txt", 'rt') as fh:
#       data = fh.read()
# except FileNotFoundError as file_err:
#    print("File that you are trying to open does not exist!") 
#    print(file_err)    
# else: 
#    print(data)




import io

try:
   fh = open("file10.txt", 'wt')
   data = fh.read()
   fh.close()
except FileNotFoundError as file_err:
   print("File that you are trying to open does not exist!") 
   print(file_err)  
except io.UnsupportedOperation as io_err:
   print(io_err)
else: 
   print("else block")
   print(data)
finally:
   print("Finally block")    
