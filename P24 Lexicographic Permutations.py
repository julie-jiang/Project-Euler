'''
P24 Lexicographic Permuations
    A permutation is an ordered arrangement of objects. For example, 3124 is one 
    possible permutation of the digits 1, 2, 3 and 4. If all of the permutations 
    are listed numerically or alphabetically, we call it lexicographic order. 
    The lexicographic permutations of 0, 1 and 2 are:

        012   021   102   120   201   210
    
    What is the millionth lexicographic permutation of the digits 
    0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?
'''
import itertools
def answer():
    '''
    I admit, I'm cheating a little bit using itertools
    '''
    digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    #digits =[0, 1, 2]
    perm = itertools.permutations(digits)
    for i in range(999999):
        next(perm)
        
    result = '' 
    for digit in next(perm):# Convert a list of int to a string
        result += str(digit)
    return result
    

if __name__ == "__main__":
    print answer() # 2783915460