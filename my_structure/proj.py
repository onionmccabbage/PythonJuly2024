# we may need to import other features from python
import random # this is a library in python
# CAREFUL when you import another module it runs everything in that module
import util # this imports our own module

def makeRandomInt():
    '''return a random integer between 0 and 100'''
    r = random.randint(0, 100)
    return r

if __name__ == '__main__':
    # we may call our function whenever we need it
    n = makeRandomInt() # this will grab a random integer
    print(n)
    # we can use our utility fnction to check if the random number is alaos a prime number
    isPrime = util.checkIfPrime(n)
    # we may choose to format the printed output
    # f'' creates a formatted string. We may inject any value using {}
    print(f'The random integer {n} is prime:{isPrime}')
