# -*- coding: utf-8 -*-
'''
P15 Lattice Paths

    Starting in the top left corner of a 2×2 grid, and only being able to move 
    to the right and down, there are exactly 6 routes to the bottom right corner.
        <image>
    How many such routes are there through a 20×20 grid?
'''
import time
c = 20
def answer():
    start = time.time()
    r =  lattice((0, 0))
    print (time.time() - start)
    return r
def lattice((x, y)):
    result1, result2 = 0, 0
    if x == c and y == c:
        return 1
    elif x == y:
        result1 += 2 * lattice((x + 1, y))
    else:
        if x < c:
            result1 += lattice((x + 1, y))
        if y < c:
            result2 += lattice((x, y + 1))
    
    return result1 + result2 
    
    
if __name__ == "__main__":
    print answer() # 
