'''
P7: 10001st Prime
    By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see 
    that the 6th prime is 13.
    what is the 10001st prime number?
'''
def answer():
    n = 0
    prime = 2
    while n < 10000:
        prime = next(generate_prime(prime))
        n += 1
    return prime

def generate_prime(curr_prime):
    '''
    A prime number, by definition, is a number that is only divisble by 1 and
    itself
    '''
    number = curr_prime + 1
    while True:
        if find_factors(number) == []:
            yield number
        number += 1
def find_factors(x):
    '''
    Find factors that are NOT 1 and NOT the number itself
    
    Only check values up to sqrt(x) because any factor greater than sqrt(x) 
    has a matching factor that is smaller than sqrt(x)
    '''
    factors = []
    for i in range(2, int(x ** 0.5) +1):
        if x % i == 0:
            factors.append(i)
            factors.append(x / i)
    return factors

if __name__ == "__main__":
    print answer() # 104743
    