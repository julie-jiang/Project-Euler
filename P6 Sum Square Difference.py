'''
P6: Sum square difference
    The sum of the squares of the first ten natural number is,
        1^2 + 2^2 + ... + 10^2 = 385
    The square of the sum of the first ten natural number is.
        (1 + 2 + ... + 10)^2 = 55^2 = 3025
    Hence the difference between the sum of the squares of the first ten natural
    number and the square of the sum is 3025 - 385 = 2640.
    Find the difference between the sum of the squares of the first one hundred 
    natulra numbers and the square of the sum
'''
def answer():
    sum_squares = 0
    for n in range(101):
        sum_squares += n ** 2
    square_sum = sum(range(101)) ** 2
    return abs(sum_squares - square_sum)

if __name__ == "__main__":
    print answer() # 25164150