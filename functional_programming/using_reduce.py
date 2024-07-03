from functools import reduce

# here are some simple utility functions
def multThem(a,b):
    ''' return the product of a*b '''
    return a*b

def useReduce(v):
    '''reduce will repeatedly apply a function, returning a single result'''
    total = reduce( multThem, v ) # the two values will be a number and the result of the previous calculation
    return total

if __name__ == '__main__':
    v = [i for i in range(1,6)]
    # v = [i for i in range(-1,6)] # careful!!!
    r = useReduce(v)
    print(f'The product of {v} is {r}')