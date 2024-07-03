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
        self.rate = r # NB this calls our rate setter function
    # we declare properties in order to validate our data
    @property # this is called a decorator
    def name(self): # this is the property getter
        return self.__name # the double underscore will mangle this property
    @name.setter
    def name(self, new_name): # this is the property setter
        '''only allow non-empty string for name'''
        if type(new_name) == str and new_name !='':
            self.__name = new_name # all good, we can store the name
        else:
            raise TypeError('Name must be a non-empty string')
    @property
    def hours(self):
        return self.__hours
    @hours.setter
    def hours(self, new_hours):
        '''hours must be a positive number'''
        if type(new_hours)==float and new_hours > 0:
            self.__hours = new_hours
        else:
            self.__hours = 0 # a sensible default
    # we may also give our class methods (stuff it can do)
    def totalGain(self):
        '''calculate the total of hours*rate'''
        gain = self.hours*self.rate
        return gain
    # build the getter and setter to validate the rate (same as hours)
    @property
    def rate(self):
        return self.__rate 
    @rate.setter
    def rate(self, new_rate):
        '''rate must be a positive number'''
        if type(new_rate)==float and new_rate > 0:
            self.__rate = new_rate
        else:
            self.__rate = 0

if __name__ == '__main__':
    # we may have as many instances of a class as we need
    e = Volunteer('Edith', 36.2, 6.0) # we now have an instance of our class
    f = Volunteer('Floella', 12.7, 3.6) # ...another instance
    print(f'{e.name} did {e.hours} voluntary work at {e.rate} earning €{e.totalGain():0.2f}')
    # here we check our validation is working
    # e.name = True # this should fail
    e.hours = -7 # this should default to 0
    print(e.hours)
    # whenever we try to work with class properties, they will actually use the get/set methods
    f.rate = -88 # validation fails, so defautls to zero
    g = Volunteer('Greta', 'oops', -99) # this will fail the validation
    print(g.hours, g.rate)


