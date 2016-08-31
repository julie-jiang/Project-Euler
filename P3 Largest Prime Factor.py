'''
Problem 3: Largest prime factor
    The prime factors of 13195 are 5, 7, 13 and 29.
    What is the largest prime factor of the number 600851475143 ?
'''
number = 600851475143

def answer():
    '''
    Find and return the largest prime factor of the given number.
    '''
    # Use find_factors() to find the next largest factor of the given number.
    for f in find_factors(number):
        # Use the definition of prime numbers to determine if f is a prime.
        # A number is a prime number if it is a positive integer greater than 
        # 1 and only divisible by itself and zero.
        if list(find_factors(f)) == [f, 1]:
            return f
def find_factors(x):
    '''
    Yield the factors of the given number x from largest to smallest.
    
    Set the upper limit of the numbers to check to sqrt(number). This is because
    sqrt(number) * sqrt(number) = number, so any factor greater than sqrt(number)
    has a matching factor that is smaller than sqrt(number).
    
    '''
    if x == 1: # Special case
        yield x
        return
    divisors = []
    for n in range(1, int(x ** 0.5) + 1):
        if x % n == 0:
            # Yield the factors greater than sqrt(number)
            yield x / n
            divisors.append(n)
    divisors.reverse()
    for d in divisors:
        # Yield the factors smaller than sqrt(number)
        yield d 



if __name__ == "__main__":
    print answer() # 6857