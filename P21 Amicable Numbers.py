# -*- coding: utf-8 -*-
'''
P21 Amicable Numbers
    Let d(n) be defined as the sum of proper divisors of n (numbers less than n 
    which divide evenly into n).
    If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair 
    and each of a and b are called amicable numbers.
    For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 
    55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 
    71 and 142; so d(284) = 220.
    Evaluate the sum of all the amicable numbers under 10000.
'''
def answer():
    d = {}
    amicable_pairs = []
    # Only numbers equal to or above 4 have dfunc values
    for num in range(4, 10000): 
        value = dfunc(num)
        d[num] = value
        for key in d.keys():
            if key == value and d[key] == num and key != num:
                amicable_pairs.append(key)
                amicable_pairs.append(num)
    return sum(amicable_pairs)
    
def dfunc(num):
    divisors = []
    for n in range(1, int(num ** 0.5)):
        if num % n == 0:
            divisors.append(n)
            divisors.append(num / n)
    divisors.remove(num)
    return sum(divisors)
            
if __name__ == "__main__":
    print answer() # 31626