def isPrime(n):
    if n <= 1:
        return False
    for i in range(2, int(n * 0.5)):
        print(i)
        if n % i == 0:
            return False
    return True


print("Is this is prime number:", isPrime(199))



