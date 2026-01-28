print("hey my name is Divaynsh Sivastava")
# with open("data.txt", "r") as f:
#     print(f.read())
# import os
# print(os.getcwd())
# os.chdir("D:/")     # change to D drive
# print(os.getcwd())

with open("data.txt",'a') as f:
    f.write(f"{input("Enter the name = ")}\n")