'''
P35: Circular primes
    The number, 197, is called a circular prime because all rotations of the 
    digits: 197, 971, and 719, are themselves prime.
    There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 
    71, 73, 79, and 97.
    How many circular primes are there below one million?
'''
def answer():
    count = 0
    for i in range(2, 1000000):
        if circular_prime(i): # If i is a circular prime, add to count
            count += 1
    return count
    
'''
Returns True if number is a circular prime. False otherwise.
'''
def circular_prime(num):
    for n in rotations(num):
        if not prime(n):
            return False
    return True
    
'''
Returns True if number is prime. False otherwise
'''
def prime(num):
    for n in range(2, int(num ** 0.5) + 1):
        if num % n == 0:
            return False
    return True
    
'''
Generator that yields circular rotations of a number
'''
def rotations(num):
    num_str = str(num)
    for combo in range(len(num_str)):
        num_str += num_str[0]
        num_str = num_str[1:]
        yield int(num_str)

if __name__ == "__main__":
    print answer() #55