# Write a program to read and print the contents of a text file.
# • Write a program to append a new line of text to an existing file.
choice = input("enter 1 if you want to read the data or 2 to write the data")
match choice:
    case "1":
        with open("data.txt",'r') as fs:
            for i in sorted(fs.readlines()):
                print(i.rstrip())
    case "2":
        with open('data.txt','a') as fs:
            fs.write(input("enter what you want to write"))