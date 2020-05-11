from math import sqrt

num = int(input("Please enter a number (greater than 2): "))
def isprime(num):
    for a in range(2, num):
        if num % a == 0:
            return False
            
    return True

primes = []

if num < 2:
    print('error, input mustt be greater than 2')

else:
    factor = 2
    while factor <= num:
        if isprime and num % factor == 0:
            primes.append (factor)
            num = num // factor
        
        else:
            factor += 1

for n in primes:
    print (n)