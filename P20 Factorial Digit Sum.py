# -*- coding: utf-8 -*-
'''
P20 Factorial Digit Sum
    n! means n × (n − 1) × ... × 3 × 2 × 1
    For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800, and the sum of the 
    digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.
    Find the sum of the digits in the number 100!
'''
def answer():
    factorial_100 = factorial(100)
    factorial_100 = str(factorial_100)
    sum_ = 0
    for digit in factorial_100:
        sum_ += int(digit)
    return sum_

def factorial(number):
    if number == 1:
        return number
    return number * factorial(number - 1)

if __name__ == "__main__":
    print answer() # 648