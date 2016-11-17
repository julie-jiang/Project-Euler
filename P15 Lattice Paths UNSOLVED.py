# -*- coding: utf-8 -*-
'''
P15 Lattice Paths

    Starting in the top left corner of a 2×2 grid, and only being able to move 
    to the right and down, there are exactly 6 routes to the bottom right corner.
        <image>
    How many such routes are there through a 20×20 grid?
'''
c = 2
def answer():
    '''
    Breadth first search of possible routes
    Because the starting point is the top left corner, and the ending point is 
    the bottom right corner, and the only legal moves are right and down, then
    we can deduct that all possible routes will arrive at the ending location
    at the same time. That means, we can return the answer as soon as we see 
    the ending point appearing once.
    Divide and conquer
    '''
    #return lattice((0, 0))
    return laticeee((0, 0))
def laticeee((x, y)):
    print "start pos: (%d, %d)" % (x, y)
    length = 1
    for (i, j) in [(x + 1, y), (x, y + 1)]:
        if i == c and j == c:
            print "goal reached"
            print "legnth: ", length
            return length
        elif i < c and j < c:
            print "checking pos (%d, %d)" % (i, j)
                
            print "------------------RECURSING-----------------------"
            result = laticeee((i, j))
            length += 2 * result
            print "result from recursing: ", result
            print "---------------------ENDED------------------------"
    print "function complete. returning length: ", 
    print length
    return length
    
    
    
    
    
    '''
    
    
    for x in range( c + 1):
        for y in range(c + 1):
            if (x, y) != startPos:
                print "checking pos (%d, %d)" % (x, y)
                if x < c and y < c:
                    print "------------------RECURSING-----------------------"
                    result = 2 * laticeee((x, y))
                    length += result
                    print "result from recursing: ", length
                    print "---------------------ENDED------------------------"
                
            print length
    return length
    '''
def lattice(startPos):
    length = 1
    currPositions = [startPos]
    while True:
        #print "============"
        nextPositions = []
        replicate_times, replicate_coord = 0, None
        for (x, y) in currPositions:
            #print
            #print "curr pos: 
            numNewPos = 0
            for (i, j) in [(x + 1, y), (x, y + 1)]:
                if i == c and j == c:
                    #print "goal acheived."
                    return length
                elif i <= c and j <= c:
                    #print "next pos: (%d, %d)" % (i, j)
                    
                    if i == j:
                        replicate_coord = (i, j)
                        replicate_times += 1
                    else:
                        numNewPos += 1
                        nextPositions.append((i, j))
            if numNewPos == 2:
                length += 1
            #print "length: ", length
        if replicate_coord != None:
            #print "------------------RECURSING-----------------------"
            result = replicate_times * lattice(replicate_coord)
            #print "result from recursing: ", result
            length += result
            #print "length after recursing: ", length
            #print "---------------------ENDED------------------------"
            
            
        currPositions = nextPositions
            
            #length += lattice(replicate_coord, length)
                    
            
            
                


if __name__ == "__main__":
    print answer() # 
    