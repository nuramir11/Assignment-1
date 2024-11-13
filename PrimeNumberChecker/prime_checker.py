import math

def isPrime(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def generatePrimes(limit):
    primes = []
    for num in range(2, limit + 1):
        if isPrime(num):
            primes.append(num)
    return primes

def main():
    limit = int(input("Enter the limit for generating a list of prime numbers: "))
    primes = generatePrimes(limit)
    print("Prime numbers up to", limit, ":", primes)

if __name__ == "__main__":
    main()
