'''
Problem 5: Smallest multiple
    2520 is the smallest number that can be divided by each of the numbers from 
    1 to 10 without any remainder.
    What is the smallest positive number that is evenly divisible by all of the 
    numbers from 1 to 20?
'''
def answer():
    num = 21
    cont = True
    '''
    If the number must be divisible by al the numbers from 1 to 20, 
    then arithmetically speaking, we only need to check if the number is 
    divisble by the numbers from 11 to 20. 
    '''
    divisors = range(11, 21)
    while cont:
        cont = False
        for d in divisors:
            if num % d != 0:
                    num += 1
                    cont = True
                    break
    return num

if __name__ == '__main__':
    print answer() # 232792560