# sometimes we need our code to run endlessly
from random import randint

def myLoop():
    # here is a run loop
    while True:
        '''ask the user for a value. If they enter q we quit. Otherwise we capitalize their input'''
        r = input('Please enter a value')
        q = r.upper() # force the string to uppercase (also q.lower())
        if q == 'Q':
            break  # or quit, which ends the module
        # r = randint(0,10)
        else:
            print(f'{r} in uppercase is {q}')
        # if r==5:
        #     break # this will stop the while loop - our code will end

if __name__ == '__main__':
    myLoop()


