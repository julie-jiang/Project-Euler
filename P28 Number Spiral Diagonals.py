'''
P28 Number Spiral Diagonals

    Starting with the number 1 and moving to the right in a clockwise direction 
    a 5 by 5 spiral is formed as follows:
        21 22 23 24 25
        20  7  8  9 10
        19  6  1  2 11
        18  5  4  3 12
        17 16 15 14 13
    It can be verified that the sum of the numbers on the diagonals is 101.
    What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral 
    formed in the same way?


1
3 5 7 9 increment = 2
13 17 21 25 increment = 4
31 37 43 49 increment = 6

     43 44 45 46 47 48 49
     42 21 22 23 24 25 26
     41 20  7  8  9 10 27
     40 19  6  1  2 11 28
     39 18  5  4  3 12 29
     38 17 16 15 14 13 30
     37 36 35 34 33 32 31
5 -- 2
7 -- 3
9 -- 4

'''
def answer():
    sum_diagonals = 1
    increment = 0
    curr_num = 1
    layer = 0
    while layer < 1001 / 2: 
        increment += 2
        for i in range(4):
            curr_num += increment
            sum_diagonals += curr_num
            
        layer += 1
    return sum_diagonals

if __name__ == "__main__":
    print answer() # 669171001