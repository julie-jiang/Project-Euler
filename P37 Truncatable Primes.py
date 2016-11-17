'''
P37: Truncatable primes
    The number 3797 has an interesting property. Being prime itself, it is 
    possible to continuously remove digits from left to right, and remain prime 
    at each stage: 3797, 797, 97, and 7. Similarly we can work from right to 
    left: 3797, 379, 37, and 3.
    Find the sum of the only eleven primes that are both truncatable from left 
    to right and right to left.
    NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.
'''
'''
We know that a prime's last digit cannot be 2, 4, 5, 6, 8. But its middle digits
can be a prime. Therefore we can deduct the properties of a truncatable prime:
    1) It is a prime itself, duh
    2) It must begin with one of {2, 3, 5, 7}
    3) The middle digits must be from {1, 3, 7, 9}
    4) It must end with one of {3, 7}
    3) By continuously removing digits from left to right, it not only remains 
    prime but also remains truncatable prime 
    
Using these properties, we can backtrack to find all truncatable primes. 

    
'''
truncatablePrimes = []
def answer():
    findTruncatablePrimes()
    return sum(truncatablePrimes)
    
'''
Adds all truncatable primes to the list
'''
def findTruncatablePrimes():
    
    for p in {3, 7}:
        
        # Call this first to look for two digit truncatable primes, because
        # They don't have middle digits  
        findTwoDigitTruncatablePrimes(p)
        
        # Look for truncatable primes with  more than two digits
        findMoreDigitsTruncatablePrimes(p)
'''
Adds all two digit truncatable primes to the list
'''
        
def findTwoDigitTruncatablePrimes(num):
    for firstdigit in {2, 3, 5, 7}:
        newnum = int(str(firstdigit) + str(num))
        
        # If it is a truncatable prime, append!
        if prime(newnum) and truncatablePrime(newnum):
            truncatablePrimes.append(newnum)
            
'''
Adds truncatable primes with more than two digits to the list
'''
def findMoreDigitsTruncatablePrimes(num):
    for nextdigit in {1, 3, 7, 9}:
        newnum = int(str(nextdigit) + str(num))
        if prime(newnum):
            
            # If its a truncatable prime, append!
            if truncatablePrime(newnum):
                truncatablePrimes.append(newnum)
                
            # If not, it might have 2 or 5 as its first digit
            else :
                for firstdigit in {2, 5}:
                    newnewnum = int(str(firstdigit) + str(newnum))
                    # If it is a truncatable prime, append!
                    if prime(newnewnum) and truncatablePrime(newnewnum):
                        truncatablePrimes.append(newnewnum)
                
            # In any case, recurse if it is a prime
            findMoreDigitsTruncatablePrimes(newnum)
                
    
            
            
'''
Returns True if num is a truncatable prime. False otherwise.
Because this number passed from findTruncatable Primes, we can assume that 
1) the number is a prime 2) the number will remain prime if we remove the digits
one by one from left to right. So we only need to check that the number remains
prime if we remove the digits one by one from right to left.
'''
def truncatablePrime(num):
    num_str = str(num)
    for i in range(1, len(num_str)):
        if not prime(int(num_str[:-(i)])): # Remove digits from right to left
            return False
    return True
    
'''
Returns True if number is prime. False otherwise
'''
def prime(num):
    if num < 2:
        return False
    for n in range(2, int(num ** 0.5) + 1):
        if num % n == 0:
            return False
    return True
    
    
if __name__ == "__main__":
    print answer() # 748317
    