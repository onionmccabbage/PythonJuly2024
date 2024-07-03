# remember, the idea of functions is to make code re-useable
# sometimes we want a function without needing to re-use it
# thats when we use lambdas

def showPower(x,y):
    '''return x to the power of y'''
    return x**y # NB ** will raise a number to a power

def flip(f): # we can pass a function into another function
    ''' flip the arguments of the incoming function'''
    return lambda x, y:f(y,x) # a lambda is just a temporary function

if __name__ == '__main__':
    print(showPower(3,2)) # 9
    print(showPower(4,3)) # 64
    print(showPower(25,0.5)) # 5.0

    s = flip(showPower)
    print( s(3,2) ) # 2**3