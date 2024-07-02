# ask for a name and number of hours voluntary work done
# then write these to a text file

def askName():
    '''retrieve a valid name: a non-emty string'''
    n = ''
    while n=='':
        n = input('Please enter a name: ')
    return n

def askHours():
    '''retrieve valid hours'''
    hrs = 0
    while hrs <= 0:
        h = input('Please enter how many hours')
        #validate it is a float
        try:
            hrs = float(h)
        except:
            pass

def commitData():
    '''nicely format and write to a file'''

if __name__ == '__main__':
    n = askName()
    h = askHours()
    commitData()