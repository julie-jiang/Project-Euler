'''
Problem 1: Multiples of 3 and 5
    If we list all the natural numbers below 10 that are multiples of 3 or 5, 
    we get 3, 5, 6 and 9. The sum of these multiples is 23.
    Find the sum of all the multiples of 3 or 5 below 1000.
'''
def answer():
    '''
    Find and return the sum of all the multiples of 3 or 5 less than 1000
    '''
    sum_ = 0
    for n in range(1000):
        if n % 3 == 0 or n % 5 == 0:
            sum_ += n
    return sum_

if __name__ == "__main__":
    print answer() # 233168