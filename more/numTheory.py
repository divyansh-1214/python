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


def call_prime(num):
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True


def call_prime_factors(num):
    prime_factors = []
    n = 2
    while num != 1:
        if num % n == 0:
            num = num // n
            if call_prime(n):
                prime_factors.append(n)
        else:
            n = n + 1
    print(prime_factors)


def call_prime_range(num):
    numbers = list(range(2, num))
    for i in range(2, int(math.sqrt(num)) + 1):
        for j in range(2, (num // 2)):
            if (i * j) in numbers:
                numbers.remove(i * j)
    return numbers


def main():
    # num1 = int(input("Enter the first number: "))
    # num2 = int(input("Enter the second number: "))
    # call_lcm(num1, num2)
    # call_gcd(num1, num2)
    # call_facor(10)
    # call_prime_factors(30)
    # print(call_prime(10))
    # 2, 3, 5, 7, 11, 13, 17, 19
    print(call_prime_range(100))


if __name__ == "__main__":
    main()
