# Use the os module to check if a file exists in a given directory.
import os
folder_name = input("enter the name of the folder")
os.chdir(os.path.join(os.getcwd(),folder_name))
file_name = input("wnter the file name that you what to delete")
if file_name in os.listdir():
    # os.remove(file_name)
    print("file is present")
else:
    print("the file is not present in the class")