# Python review exercise: guess the random number between 0-100
from random import randint # we need a way to make random numbers

# a function to see if a value is a square number
def isSquare(n):
    '''check if a number is a square number'''
    if (n*n)**0.5 == n: # taking the **0.5 power is the square root
        return True
    else:
        return False

def game():
    ''' ask user to guess a random integer 0-100 '''
    target = randint(0,100) # up to 100 inclusive
    # create collections of odds, evens, squares and primes
    odd_ints     = range(1,100, 2) 
    even_ints    = range(0, 101, 2)
    squares_list = [i*i for i in range(0, 11)]
    primes_t = (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97)
    # set some boolean flags regarding the nature of our target number
    is_odd    = target in odd_ints
    is_even   = target in even_ints
    is_square = target in squares_list
    is_prime  = target in primes_t
    guess = 999 # set an initial value that is out of range
    # keep the game running
    while guess != target:
        # we really need to validate the input...
        guess_text = input('guess:')
        if guess_text.isnumeric():
            guess_int = int(guess_text)
        else:
            print('try again')
        # conditionally act on the guess
        if guess == target: # did they get it right
            print(f'correct it was {target}' )
            # since guess now equals target, the while loop will end
        elif guess == -2: # do they want a clue
            print (f'CLUE: odd: {is_odd} even: {is_even} square: {is_square} prime: {is_prime}' )
        elif guess == -1: # do they want to quit
            print (f'it was {target}' )
            guess = target # break # stops the current loop
        elif guess > target: # is the guess too high
            print('too high')
        elif guess < target: # is the guess too low (could be an else clause)
            print('too low')

if __name__ == '__main__':
    game()
