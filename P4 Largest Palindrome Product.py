'''
Problem 4: Largest palindrome product
    A palindromic number reads the same both ways. The largest palindrome made
    from the product of two 2-digit numbers is 9009 = 91 x 99.
    Find the largest palindrome made from the product of two 3-digit numbers
'''
def answer():
    '''
    Unfortunately this is not the most efficient method I could think of. 
    Idealy the next product to check is always the next largest. But because 
    the distribution of the value of the product of two numbers (visually, the 
    area of the rectangle with sides length of the two numbers) is not linear,
    I could not come up with a straightforward algorithm on the top of my head.
    
    Luckily this is still a easy(fast) probelm to solve for the computer, even 
    though it had to compute every product.
    '''
    num_range = range(100, 1000)
    palindromes = []
    for num1 in num_range:
        for num2 in num_range[num_range.index(num1):]:
            if is_palindrome(num1 * num2):
                palindromes.append(num1 * num2)
    return max(palindromes)
def is_palindrome(num):
    num_str = str(num)
    for index in range(len(num_str) / 2):
        if num_str[index] != num_str[-(index + 1)]:
            return False
    return True

if __name__ == "__main__":
    print answer() # 906609

    