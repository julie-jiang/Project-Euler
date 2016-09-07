'''
P17 Number Letter Counts
    If the numbers 1 to 5 are written out in words: one, two, three, four, five, 
    then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.
    If all the numbers from 1 to 1000 (one thousand) inclusive were written out 
    in words, how many letters would be used?
    NOTE: Do not count spaces or hyphens. For example, 342 
    (three hundred and forty-two) contains 23 letters and 115 
    (one hundred and fifteen) contains 20 letters. The use of "and" when writing
    out numbers is in compliance with British usage.
'''
one_digit_nums = {}
two_digit_10_to_19 = {}
two_digit_tens = {}
    

def answer():
    num_to_letters()
    sum_ = 0
    for n in range(1, 1001):
        sum_ += number_letter(n)
    return sum_
    
def num_to_letters():
    global one_digit_nums
    global two_digit_10_to_19
    global two_digit_tens 
    
    one_digit_let = {1: "one", 2: "two", 3: "three", 4: "four", 5: "five", \
                      6: "six", 7: "seven", 8: "eight", 9: "nine"}
    two_digit_10_to_19_let = {10: "ten", 11: "eleven", 12: "twelve" , \
                              13: "thirteen", 14: "fourteen", 15: "fifteen", \
                              16: "sixteen", 17: "seventeen", 18: "eighteen", \
                              19: "nineteen"}
    two_digit_tens_let = {2: "twenty", 3: "thirty", 4: "forty", 5: "fifty", \
                      6: "sixty", 7: "seventy", 8: "eighty", 9: "ninety"}
    one_digit_nums, two_digit_10_to_19, two_digit_tens = {}, {}, {}
    for key, value in one_digit_let.items():
        one_digit_nums[key] = len(value)
    one_digit_nums[0] = 0
    for key, value in two_digit_10_to_19_let.items():
        two_digit_10_to_19[key] = len(value)
    for key, value in two_digit_tens_let.items():
        two_digit_tens[key] = len(value)

    
def number_letter(number):
    if number == 1000:
        return 11 # "one thousand"
    elif number > 99:
        return three_digit_number_letters(number)
    elif number > 9:
        return two_digit_number_letters(number)
    else:
        return one_digit_number_letters(number)
        
def one_digit_number_letters(number):
    return one_digit_nums[number]
    
def two_digit_number_letters(number):
    if number < 20:
        return two_digit_10_to_19[number]
    else:
        number = str(number)
        return two_digit_tens[int(number[0])] + one_digit_nums[int(number[1])]
        
def three_digit_number_letters(number):
    number = str(number)
    length = one_digit_nums[int(number[0])] + 7 # some "hundred"
    if number[1] == '0':
        if number[2] == '0':
            return length
        else:
            length += 3 + one_digit_nums[int(number[2])] # "and" some digit
    else:
        length += 3 + two_digit_number_letters(int(number[1:])) # "and" some digit
    return length

if __name__ == "__main__":
    print answer() # 21124

        

        