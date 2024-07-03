# we may import anyting from any other module
from class_a import Volunteer

# we may choose to write a clas which inherits from some other class
class VolunteerGroup(Volunteer):
    '''we now have all the properties and methods inherited from 'Volunteer' '''
    def __init__(self, n, h, r, num_people): # a group is several people
        # we call the __init__ of the parent class
        super().__init__(n ,h, r)
        self.num_people = num_people # we probably want to validate this....

# what does Python think this module is called.....?
print(f'Python has assigned the following name to this module: {__name__}') # Python will ALWAYS assign a name to the running module

if __name__ == '__main__':
    # we may create instances
    grA = VolunteerGroup('Group A', 456.55, 0.44, 6)
    print(f'{grA.name} carried out {grA.hours} voluntary work among {grA.num_people} people')