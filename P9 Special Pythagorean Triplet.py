'''
P9: Special Pythagorean Triplet
    A Pythagorean triplet is a set of three natural numbers, a < b < c, for 
    which,
        a^2 + b^2 = c^2
    For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2
    
    There exists exactly one Pythagorean triplet for which a + b + c = 1000
    Find the product abc
'''

def answer():
    '''
    Since 3 + 4 + 5 = 12, we know that a, b, c must be equal to or greater than
    3, 4, 5, respectively. Hence we will start checking from c = 5 + 1 = 6
    '''
    c = 6
    while True:
        #  Use the fact that a < b < c to limit the range
        for b in range(4, c):
            for a in range(3, b):
                if c ** 2 == a ** 2 + b ** 2:
                    if a + b + c == 1000:
                        return a * b * c
        c += 1

if __name__ == "__main__":
    print answer() # 31875000
    