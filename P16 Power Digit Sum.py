'''
P16: Power Digit Sum
    2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
    What is the sum of the digits of the number 2^1000?
'''
def answer():
    number = 2 ** 1000
    number = str(number)
    sum_ = 0
    for digit in number:
        sum_ += int(digit)
    return sum_

if __name__ == "__main__":
    print answer() # 1366
