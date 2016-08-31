'''
P10: Summation of Primes
    The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
    Find the sum of all the primes below two million
'''
def answer():
    sum_ = 0
    prime_numbers = generate_prime()
    for number in prime_numbers:
        if number >= 2000000:
            return sum_
        sum_ += number 

def generate_prime():
    '''
    A prime number, by definition, is a number that is only divisble by 1 and
    itself
    '''
    number = 2
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
    print answer() # 142913828922
    