'''
P18 Maximum Path Sum II
    By starting at the top of the triangle below and moving to adjacent numbers 
    on the row below, the maximum total from top to bottom is 23.
           3
          7 4
         2 4 6
        8 5 9 3
    That is, 3 + 7 + 4 + 9 = 23.
    Find the maximum total from top to bottom in triangle.txt 
    (right click and 'Save Link/Target As...'), a 15K text file containing a 
    triangle with one-hundred rows.
    NOTE: This is a much more difficult version of Problem 18. It is not 
    possible to try every route to solve this problem, as there are 2^99 
    altogether! If you could check one trillion (10^12) routes every second it 
    would take over twenty billion years to check them all. There is an 
    efficient algorithm to solve it. ;o)
'''
def answer():
    '''
    For every node in a lower level of the pyramid, there are one or two nodes 
    in the level above that is capable of reaching that node. In the case that 
    there are two possibilities, i.e. two parent nodes that reaches a node, we
    compare the sum of between the two and only keep track of the greater one. 
    
    Note: this function is identitical to the one I wrote for P18 Maximum Path
    Sum I
    '''
    pyramid = read_pyramid()
    totalLevel = len(pyramid) - 1
    # Key: end node coordinate of a path. Value: the maximum possible sum
    paths = {(0, 0): pyramid[0][0]}
    level, nextLevel = 0, 1
    while True: 
        for _, index in paths.keys():
            for nextIndex in [index, index + 1]:
                nextNode = pyramid[nextLevel][nextIndex]
                if not paths.has_key((nextLevel, nextIndex)) or nextNode + \
                   paths[(level, index)] > paths[(nextLevel, nextIndex)]:
                    # Update paths with new or better sum
                    paths[(nextLevel, nextIndex)] = nextNode + \
                                                    paths[(level, index)]
            # Dispose parent node
            del paths[(level, index)]
        if nextLevel == totalLevel: # Bottom of pyramid reached
            return max(paths.values())
        level += 1
        nextLevel += 1     
        
        
def read_pyramid():
    # Open triangle.txt (I renamed it)
    pyramid = \
    open("/Users/Jiang/Desktop/Project Euler/Supporting Files/P67 Triangle.txt")
    pyramid = pyramid.read()
    pyramid = str(pyramid).split("\n")
    pyramid_grid = []
    i = 0
    for level in pyramid:
        level = level.split()
        pyramid_grid.append([])
        for number in level:
            pyramid_grid[i].append(int(number))
        i += 1 
    pyramid_grid.pop() # I noticed there's an extra empty line
    return pyramid_grid
    
if __name__ == "__main__":
    print answer() # 7273

