# we may import anyting from any other module
from class_a import Volunteer

# we may choose to write a clas which inherits from some other class
class VolunteerGroup(Volunteer):
    '''we now have all the properties and methods inherited from 'Volunteer' '''
    def __init__(self, n, h, r, num_people): # a group is several people
        # we call the __init__ of the parent class
        super().__init__(n ,h, r)
        self.num_people = num_people # remember - this calls our setter function
    @property
    def num_people(self):
        return self.__num_people # return the mangled value
    @num_people.setter
    def num_people(self, new_num_people):
        '''validate this is a positive integer'''
        if type(new_num_people) == int and new_num_people > 0:
            self.__num_people = new_num_people
        else:
            self.__num_people = 2 # sensible default
    # whenever we write a class we may choose to override the build in __str__ method for printing
    def __str__(self):
        return f'{self.name} has {self.num_people} volunteers who covered {self.hours} at {self.rate} gaining €{self.totalGain():0.2f}'

# what does Python think this module is called.....?
print(f'Python has assigned the following name to this module: {__name__}') # Python will ALWAYS assign a name to the running module

if __name__ == '__main__':
    # we may create instances
    grA = VolunteerGroup('Group A', 456.55, 0.44, 6)
    print(f'{grA.name} carried out {grA.hours} voluntary work among {grA.num_people} people')

    # whenever we call 'print' it always uses the __str__ method
    print(grA)