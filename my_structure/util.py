def checkIfPrime(n):
    '''return True if n is prime, False otherwise'''
    primes_t = (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97)
    # logic may check ==, < > <= >= != or in
    if n in primes_t: # we can check if a value is in a collection
        return True
    else:
        return False
    
# we may exercise the code to see if it works as expected
c = 43
print(checkIfPrime(c)) # True