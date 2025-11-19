# os.path.exists()

# import os
# file_name = "practice.txt"

# if os.path.exists(file_name):
#    print("File exists.")
# else:
#    print("File does not exist")   



# import os
# file_name = "C:/Users/shail/GITDEMO/practice.txt"

# if os.path.exists(file_name):
#    print("File exists.")
# else:
#    print("File does not exist")   





# pathlib.path.exists()

from pathlib import Path
file_name = Path("C:/Users/shail/GITDEMO/practice.txt")

if file_name.exists():
   print("File exists. Cannot create!")
else:
   print("File does not exist")
   fh = open(file_name, 'xt')
   fh.write("Some content")
   fh.close()   
