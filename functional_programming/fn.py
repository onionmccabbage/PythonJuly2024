# any imports tend to go at the top of the module
import datetime

# define any function next
def addThem(a, b):
    '''return the sum of a+b'''
    return a+b

def isOdd(n):
    '''return True if n is odd (False otherwise)'''
    if n%2 !=0: # % is integer division
        return True # we have an odd number
    else:
        return False

# Python provides 'map' as a higher order function to use other functions
def useMap():
    '''we will map all of a collection of values onto one of our utility functions'''
    values = range(0,10) #start, stop-before
    result_list = map(addThem, values, values) # 0+0, 1+1, 2+2...
    return result_list # we have a list of the sum of each of the list items

# suppose volunteers have gained income and we need to augment with company-provided extra
def calcV(x, y):
    '''for each voluntary gain x the company will augment with y'''
    total = map(addThem, x, y)
    return total

# filter lets us apply a simple function repeatedly to filter values
def useFilter():
    '''apply a function to filter results'''
    r = range(-9, 10)
    odds = filter(isOdd, r) # check each value in the range to see if it is odd
    return odds

# we may also choose to declare classes...
# (none needed here)


if __name__ == '__main__':
    r = useMap() # we have a map object (which is iterable)
    for i in r: # iterate over the resulting map object
        print(i)

    t = calcV((33, 44, 55), (16.5, 22, 27.5))
    for i in t:
        print(i)

    o = useFilter()
    for i in o:
        print(i)
    