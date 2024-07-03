import datetime

def getDate():
    '''retrieve a date-time stamp from the current computer'''
    return datetime.datetime.now() # or today()

if __name__ == '__main__':
    print(getDate())