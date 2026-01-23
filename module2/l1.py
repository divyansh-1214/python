# Write a function to calculate the area of a rectangle (length × width).
def area(l, b):
    return l * b


def main():
    length = float(input("Enter the length of the rectangle: "))
    width = float(input("Enter the width of the rectangle: "))
    print("The area of the rectangle is:", area(length, width))


if __name__ == "__main__":
    main()
