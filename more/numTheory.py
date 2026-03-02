import math


def call_lcm(num1, num2):
    n = 2
    lcm = 1
    while (num1 != 1) or (num2 != 1):
        if (num1 % n == 0) or (num2 % n == 0):
            if num1 % n == 0:
                num1 = num1 // n
            if num2 % n == 0:
                num2 = num2 // n
            lcm = lcm * n
        else:
            n = n + 1
    print("The GCD of the two numbers is: ", lcm)


def call_gcd(num1, num2):
    n1 = min(num1, num2)
    n2 = max(num1, num2)
    while n1 != 0:
        n3 = n2 % n1
        n2 = n1
        n1 = n3
    print("The GCD of the two numbers is: ", n2)


def call_facor(num):
    factors = []
    for i in range(1, int(math.sqrt(num)) + 1):
        if num % i == 0:
            factors.append(i)
            factors.append(num // i)
    factors = sorted((set(factors)))
    print("The factors of the number are: ", factors)


def main():
    # num1 = int(input("Enter the first number: "))
    # num2 = int(input("Enter the second number: "))
    # call_lcm(num1, num2)
    # call_gcd(num1, num2)
    # call_facor(10)


if __name__ == "__main__":
    main()
