from math import sqrt

def isprime(num):
    for a in range(2, num):
        if num % a == 0:
            return False
        
    return True

if __name__ == "__main__":
    num = (int(input("Please input a number (greater than 2): ")))
    print(isprime(num))