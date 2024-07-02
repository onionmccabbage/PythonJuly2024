# we may need to import other features from python
import random # this is a library in python
import util # this imports our own module

def makeRandomInt():
    '''return a random integer between 0 and 100'''
    r = random.randint(0, 100)
    return r

# we may call our function whenever we need it
n = makeRandomInt() # this will grab a random integer
print(n)
# we can use our utility fnction to check if the random number is alaos a prime number

