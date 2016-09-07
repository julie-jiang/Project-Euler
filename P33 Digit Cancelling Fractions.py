'''
P33 Digit cancelling fractions
    The fraction 49/98 is a curious fraction, as an inexperienced mathematician 
    in attempting to simplify it may incorrectly believe that 49/98 = 4/8, 
    which is correct, is obtained by cancelling the 9s.

    We shall consider fractions like, 30/50 = 3/5, to be trivial examples.

    There are exactly four non-trivial examples of this type of fraction, less 
    than one in value, and containing two digits in the numerator and 
    denominator.

    If the product of these four fractions is given in its lowest common terms, 
    find the value of the denominator.
'''
def answer():
    digit_cancel_frac = []
    
    for num in range(10, 100):
        for denom in range(10, 100):
            # Avoid fractions greater than one and avoid trivial cases
            if num >= denom or num % 10 == 0 and denom % 10 == 0: 
                pass
            else:
                for digit in str(num):
                    if digit in str(denom):
                        num_cancelled = cancel_num(str(num), str(digit))
                        denom_cancelled = cancel_num(str(denom), str(digit))
                        try:
                            if num / float(denom) == \
                               num_cancelled / float(denom_cancelled):
                                digit_cancel_frac.append((num, denom))
                                break
                        except ZeroDivisionError:
                            pass
    
    print digit_cancel_frac
    prod_num, prod_denom = 1, 1
    for num, denom in digit_cancel_frac:
        prod_num *= num
        prod_denom *= denom
    print prod_num, prod_denom
    _, simplified_prod_denom= simplify_frac(prod_num, prod_denom)
    return simplified_prod_denom
        
def cancel_num(number_str, digit_str):
    index = number_str.index(digit_str)
    if index == 0:
        return int(number_str[1])
    return int(number_str[0])
    
def simplify_frac(num, denom):
    for i in range(2, int(denom ** 0.5) + 1):
        if num % i == 0 and denom % i == 0:
            return simplify_frac(num / i, denom / i)
    if denom % num == 0 and num != 1:
        return simplify_frac(1, denom / num)
    return num, denom
if __name__ == "__main__":
    print answer() # 100
    