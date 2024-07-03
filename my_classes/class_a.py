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
    def __init__(self, n, h, r): # a bit like a constructor in Java
        self.name = n # self refers to whatever instance we are building
        self.hours = h # NB each property may be of ANY data type (number, str, list, tuple, dict...)
        self.rate = r
    # we may also give our class methods (stuff it can do)
    def totalGain(self):
        '''calculate the total of hours*rate'''
        gain = self.hours*self.rate
        return gain

if __name__ == '__main__':
    # we may have as many instances of a class as we need
    e = Volunteer('Edith', 36.2, 6.0) # we now have an instance of our class
    f = Volunteer('Floella', 12.7, 3.6) # ...another instance
    print(f'{e.name} did {e.hours} voluntary work at {e.rate} earning {e.totalGain()}')


