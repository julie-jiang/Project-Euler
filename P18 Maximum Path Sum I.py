'''
P18 Maximum Path Sum I
    By starting at the top of the triangle below and moving to adjacent numbers 
    on the row below, the maximum total from top to bottom is 23.
           3
          7 4
         2 4 6
        8 5 9 3
    That is, 3 + 7 + 4 + 9 = 23.
    Find the maximum total from top to bottom of the triangle below:
        
                         75
                        95 64
                      17 47 82
                     18 35 87 10
                    20 04 82 47 65
                   19 01 23 75 03 34
                  88 02 77 73 07 63 67
                 99 65 04 28 06 16 70 92
                41 41 26 56 83 40 80 70 33
               41 48 72 33 47 32 37 16 94 29
              53 71 44 65 25 43 91 52 97 51 14
             70 11 33 28 77 73 17 78 39 68 17 57
           91 71 52 38 17 14 91 43 58 50 27 29 48
          63 66 04 68 89 53 67 30 73 16 69 87 40 31
        04 62 98 27 23 09 70 98 73 93 38 53 60 04 23

    NOTE: As there are only 16384 routes, it is possible to solve this problem 
    by trying every route. However, Problem 67, is the same challenge with a 
    triangle containing one-hundred rows; it cannot be solved by brute force, 
    and requires a clever method! ;o)
'''
def answer():
    '''
    For every node in a lower level of the pyramid, there are one or two nodes 
    in the level above that is capable of reaching that node. In the case that 
    there are two possibilities, i.e. two parent nodes that reaches a node, we
    compare the sum of between the two and only keep track of the greater one.
     
    Note: this function is identitical to the one I wrote for P67 Maximum Path
    Sum II
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
    
    pyramid = str("""75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23""").split("\n")

    pyramid_grid = []
    i = 0
    for level in pyramid:
        level = level.split()
        pyramid_grid.append([])
        for number in level:
            pyramid_grid[i].append(int(number))
        i += 1 
    return pyramid_grid
    
if __name__ == "__main__":
    print answer() # 1074

