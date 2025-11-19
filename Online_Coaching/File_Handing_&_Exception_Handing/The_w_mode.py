# w mode - open the file for writing. Overwrites the file

# create a new file if file does not exist

fh = open("file1.txt", 'wt')
fh.write("This file is overwritten using 'w' mode in Python.\n")
fh.write("Have a nice day!")
fh.close()