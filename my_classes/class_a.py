# what are our options?
v_t = ('Edith', 34.2, 6.0)
v_l = ['Edith', 34.2, 6.0]
v_d = {'name':'Edith', 'hours':34.2, 'rate':6.0}

v_l[1] = 'nonsense' # oh dear...
v_d['rate'] = -7 # oops

# a class gives us the chance to validate data and ensure rigour
class Volunteer:
    '''This class will encapsulate a volunteer
    Properties: name (a non-empty string)
    hours (a positive float)
    rate(a positive float)'''
    # NB every function inside a class MUST take 'self' as an argument
    def __init__(self, n): # a bit like a constructor in Java
        self.name = n # self refers to whatever instance we are building

if __name__ == '__main__':
    # we may have as many instances of a class as we need
    e = Volunteer('Edith') # we now have an instance of our class
    f = Volunteer('Floella') # ...another instance
    print(e.name, f.name)


