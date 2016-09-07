'''
P30 Digit fifth powers
    Surprisingly there are only three numbers that can be written as the sum of 
    fourth powers of their digits:
        1634 = 1^4 + 6^4 + 3^4 + 4^4
        8208 = 8^4 + 2^4 + 0^4 + 8^4
        9474 = 9^4 + 4^4 + 7^4 + 4^4
    As 1 = 1^4 is not a sum it is not included.
    The sum of these numbers is 1634 + 8208 + 9474 = 19316.
    Find the sum of all the numbers that can be written as the sum of fifth 
    powers of their digits.
    

'''
def answer():
    '''
    For digit fourth powers, we observe that
    two digits:   10 <= n <= 99,         1 <= x <= 13122
    three digits: 100 <= n <= 999,       1 <= x <= 19683
    four digits:  1000 <= n <= 9999,     1 <= x <= 26244
    five digits:  10000 <= n <= 99999,   1 <= x <= 32805
    six digits:   100000 <= n <= 999999, 1 <= x <= 39366
    
    A two digit number n, which ranges from 10 to 99, has a sum of its digits
    raised to the fifth power a minimum of 1 (when n = 10, x = 1^5 + 0^5 = 1) 
    and a maximum of 118098 (when n = 99, x = 9^5 + 9^5 = 118098). 
    Similarily, 
        two digits:   10 <= n <= 99,           1 <= x <= 118098
        three digits: 100 <= n <= 999,         1 <= x <= 177147
        four digits:  1000 <= n <= 9999,       1 <= x <= 236196
        five digits:  10000 <= n <= 99999,     1 <= x <= 295245
        six digits:   100000 <= n <= 999999,   1 <= x <= 354294
        seven digits: 1000000 <= n <= 9999999, 1 <= x <= 413343
    We can observe that once the number reaches seven digits, the maximum value
    of the sum of its digits raised to the fifth power, 413343, is well below
    the maximum value of the number, 9999999. So n = 1000000, the first seven
    digit number, must be an upper limit to our question.
    '''
    sum_ = 0
    num = 10
    while num < 1000000:
        num_str = str(num)
        digit_fifth_power_sums = 0
        for digit in num_str:
            digit_fifth_power_sums += int(digit) ** 5
        if digit_fifth_power_sums == num:
            sum_ += num
        num += 1
    return sum_

if __name__ == "__main__":
    print answer() # 443839