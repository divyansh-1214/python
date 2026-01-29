print("Divyansh")
# try:
#     x = int(input("Enter number: "))
#     y = 10 / x
# except ZeroDivisionError:
#     print("Division by zero not allowed")
# except ValueError:
#     print("Invalid input")
# else:
#     print("Result:", y)
# finally:
#     print("Program Ended")

# try:
#     age = int(input("enter the age"))
#     if age < 18:
#         raise ValueError
#     else:
#         print(f" age is {age}")
# except ValueError:
#     print("age must be grater that 18")

# try:
#     number = int(input("enter the age"))
# except ValueError:
#     print("enter the valid number")

# try:
#     a = int(input("enter the value of a"))
#     b = int(input("enter the value of b"))
# except ValueError:
#     print("enter the valid value")
# else:
#     try:
#         print(a/b)
#     except ZeroDivisionError:
#         print("you have enter wrong value")

# try:
#     a = int(input("enter the value of a"))
#     b = int(input("enter the value of b"))
#     print(a/b)
# except ValueError:
#     print("enter the valid value")
# except ZeroDivisionError:
#     print("you have enter wrong value")
    
try:
    marks = int(input("Enter marks: "))
    if marks < 0 or marks > 100:
        raise ValueError("Marks must be between 0 and 100")
    print("Marks accepted")
except ValueError as e:
    print("Error:", e)
