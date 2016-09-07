# -*- coding: utf-8 -*-
'''
P14 Longest Collatz Sequence
    The following iterative sequence is defined for the set of positive 
    integers:
        n → n/2 (n is even)
        n → 3n + 1 (n is odd)
    Using the rule above and starting with 13, we generate the following 
    sequence:
        13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
    It can be seen that this sequence (starting at 13 and finishing at 1) 
    contains 10 terms. Although it has not been proved yet (Collatz Problem), 
    it is thought that all starting numbers finish at 1.
    Which starting number, under one million, produces the longest chain?
    NOTE: Once the chain starts the terms are allowed to go above one million.
'''

def answer():
    '''
    Assuming a collatz sequence always terminates at 1, then working backwards, 
    it is easy to see that the last few numbers will always be:
        ... 16 -> 8 -> 4 -> 2 -> 1
    Hence the starting number that yields the longest collatz sequence must be 
    greater than 16.
    
    BUG IN THE QUESTION: The questions states that:
        "Once the chain starts the terms are allowed to go above one million."
    But the right answer, 837799, yields a number of values that shoot above 
    a million.
    '''
    max_len, max_num = 0, None
    starting_number = 17
    while starting_number < 1000000:
        collatz_length = collatz(starting_number, 1)
        if collatz_length > max_len:
            max_len, max_num = collatz_length, starting_number
        starting_number += 1
    return max_num
    
def collatz(number, length):
    ''' 
    Computes the length of a collatz sequence recursively, then returns the 
    length of that colltaz sequence
    '''
    if number == 16:
        return length + 4
    elif number % 2 == 0:
        return collatz(number / 2, length + 1)
    else:
        return collatz(number * 3 + 1, length + 1)



if __name__ == "__main__":
    print answer() # 837799