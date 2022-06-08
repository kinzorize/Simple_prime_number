def prime_number(number):
    is_prime = True
    for i in range(2, number):
        if number % i == 0:
            is_prime = False
    if is_prime:
        print(f"{number} It's a prime number")
    else:
        print(f"{number} It's a not prime number")


n = int(input("Enter a number: "))

prime_number(number=n)
