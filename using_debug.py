# ask for a name and number of hours voluntary work done
# then write these to a text file

def askName():
    '''retrieve a valid name: a non-empty string'''
    n = ''
    while n=='':
        n = input('Please enter a name: ')
    return n

def askHours():
    '''retrieve valid hours'''
    hrs = 0
    while hrs <= 0:
        h = input('Please enter how many hours: ')
        #validate it is a float
        try:
            hrs = float(h)
        except:
            pass
        # remember to return the numeric value (not the string value)
        return hrs # we must remember to actually return a value!!!!

def commitData(n, h):
    '''nicely format and write to a file'''
    # we may format numbers to a particular precision
    output = f'{n} spent {h:0.2f} hours volunteering'
    fout = open('vol.txt', 'at')
    print(output, file=fout)# or any of the options

if __name__ == '__main__':
    n = askName()
    h = askHours()
    commitData(n, h)