# -*- coding: utf-8 -*-
'''
P27 Quadratic Primes
    Euler discovered the remarkable quadratic formula:
        n^2 + n + 41
    It turns out that the formula will produce 40 primes for the consecutive 
    integer values 0 <= n <= 39. However, when n = 40,
    40^2 + 40 + 41 = 40(40+1)+41 is divisible by 41, and certainly when n = 41,
    41^2 + 41 + 41 is clearly divisible by 41.

    The incredible formula n^2 − 79n + 1601 was discovered, which produces 80 
    primes for the consecutive values 0 <= n <= 79. 
    The product of the coefficients, −79 and 1601, is −126479.

    Considering quadratics of the form:
        n^2 + an + b, where |a| < 1000 and |b| <= 1000
        where |n|is the modulus/absolute value of n
            e.g. |11| = 11 and |−4| = 4
    Find the product of the coefficients, a and b, for the quadratic expression 
    that produces the maximum number of primes for consecutive values of n, 
    starting with n = 0.
'''
def answer():
    most_consec, max_a, max_b = 0, None, None
    for a in range(-999, 1000):
        for b in range(-1000, 1001):
            num_consecs = quadratic(a, b)
            if num_consecs > most_consec:
                most_consec, max_a, max_b = num_consecs, a, b
    return max_a * max_b

def quadratic(a, b):
    n = 0
    num_consecs = 0
    while True:
        x = n ** 2 + a * n + b
        #print "checking x: ", x
        #break
        if not is_prime(x):
            #print "not prime."
            return num_consecs
        else:
            num_consecs += 1
            n += 1

def is_prime(x):
    if x < 2:
        return False
    for d in range(2, int(x ** 0.5) + 1):
        if x % d == 0:
            return False
    return True
        
if __name__ == "__main__":
    print answer() # -59231