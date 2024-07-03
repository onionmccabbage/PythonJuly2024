class DemoClass:
    def __init__(self, q):
        self.q = q
    @property
    def q(self):
        return self.__q
    @q.setter
    def q(self, new_q):
        if type(new_q) in (int, float):
            self.__q = new_q
        elif type(new_q)==dict:
            self.__q = list()
            # we can iterate over all the members of the dict
            for (k,v) in new_q.items(): # (k,v) will reveal each key and value in the dict
                self.__q.append(v)

def demoFn(args):
    '''we can emulate overloading ...'''
    if type(args) in (int, float):
        print(f'we received a number: {args}')
    elif type(args)==dict:
        # we can iterate over all the members of the dict
        for (k,v) in args.items(): # (k,v) will reveal each key and value in the dict
            print(f'Item {k} contains {v}')

if __name__ == '__main__':
    # we may cal our function and pass in a simple number
    demoFn(3)
    # or we may pass in a complex structure
    demoFn( {'n':'Zoe', 'a':32} )
    # how about our class....?
    e = DemoClass(32)
    print(e.q)
    f = DemoClass({'n':'Zoe', 'a':32})
    print(f.q)