# sometimes we need our code to run endlessly
from random import randint


# here is a run loop
while True:
    r = randint(0,10)
    print(r)
    if r==5:
        break # this will stop the while loop - our code will end


