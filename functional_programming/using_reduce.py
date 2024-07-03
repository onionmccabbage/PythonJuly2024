from functools import reduce

# here are some simple utility functions
def multThem(a,b):
    ''' return the product of a*b '''
    return a*b

def useReduce(v):
    '''reduce will repeatedly apply a function, returning a single result'''
    total = reduce( multThem, v )
    return total

if __name__ == '__main__':
    v = [i for i in range(1,6)]
    r = useReduce(v)
    print(f'The product of {v} is {r}')