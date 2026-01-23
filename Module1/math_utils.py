def get_factorial(n):
    p = 1
    while n > 1:
        p *= n
        n -= 1
    return p


def main():
    n = int(input("Enter a number to compute its factorial: "))
    print(get_factorial(n))  # Output: 120


# this part was add to run the main function when this file is executed directly
if __name__ == "__main__":
    main()
