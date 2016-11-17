'''
P34 Digit Factorials
    145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

    Find the sum of all numbers which are equal to the sum of the factorial of 
    their digits.

    Note: as 1! = 1 and 2! = 2 are not sums they are not included.
'''

def answer():
    '''
    Because 1! = 1, 2! = 2, 3! = 6, 4! = 24, 5! = 120, 6! = 720, 7! = 5040, 
    8! = 40320 and 9! = 362880:
    Any number containing '4' must be at least 2 digits and  greater than 24.
    Any number containing '5' must be at least 3 digits and greater than 120.
    Any number containing '6' must be at least 3 digits and greater than 720.
    Any number containing '7' must be at least 4 digits and greater than 5040.
    Any number containing '8' must be at least 5 digits and greater than 40320.
    Any number containing '9' must be at least 6 digits and greater than 362880.
    
    Furthermore, a two digit number, which ranges from 10 to 99, has a minimum
    of digit factorial sums of 1 (when n = 10, x = 1! + 0 ! = 1) and a maximum
    of digit factorial sums of 725760 (when n = 99, x = 9! + 9! = 725760).
    Similarly...
        two digits:   10 <= n <= 99,             1 <= x <= 725760
        three digits: 100 <= n <= 999,           1 <= x <= 1086640
        four digits:  1000 <= n <= 9999,         1 <= x <= 1451520
        five digits:  10000 <= n <= 99999,       1 <= x <= 1814400
        six digits:   100000 <= n <= 999999,     1 <= x <= 2177280
        seven digits: 1000000 <= n <= 9999999,   1 <= x <= 2540160
        eight digits: 10000000 <= n <= 99999999, 1 <= x <= 2903040
    Thus we establish an upper bound at 9! * 7 = 2540160
    
    '''
    sum_ = 0
    factorials = {}
    for n in range(10): # Compute once and store in dict
        factorials[n] = factorial(n)
    num = 3
    while num < 2540160:
        num_str = str(num)
        if (num_str >= 362880 and '9' in num_str) or \
           (num_str >= 40320 and '8' in num_str) or \
           (num_str >= 5040 and '7' in num_str) or \
           (num_str >= 720  and '6' in num_str) or \
           (num_str >= 120 and '5' in num_str) or \
           (num_str >= 24 and '4' in num_str):
            digit_factorials = 0
            for digit in num_str:
                digit_factorials += factorials[int(digit)]
            if digit_factorials == num:
                sum_ += digit_factorials
        num += 1
    return sum_

def factorial(n):
    if n == 1 or n == 0:
        return 1
    return n * factorial(n - 1)
    
def lala(n):
    sum_ = 0
    for digit in str(n):
        sum_ += factorial(int(digit))
    print sum_
    

if __name__ == "__main__":
    print answer() # 40730

    