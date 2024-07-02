# in Python we may gather code together into a reuseable function
def checkEven(n):
    '''this is a docstring
    we can declare the purpose of our function
    We will return True if a value is even and False otherwise'''
    if n%2 == 0: # % will return the remainder after division
        return True # careful - Python is a case-sensitive language 
    else:
        return False

def checkNum():
    '''We ask the user for a value and return the numeric part or else a string'''
    r = input('Please enter a value: ')
    # here we check if they entered a numeric value (careful every input is ALWAYS a string)
    if r.isnumeric(): # we check if the string looks like a numeric value
        return int(r) # convert it to an integer
    else:
        return 'that is not an integer value'

# we may call our functions whenever we like
result = checkEven(42) # at this point our funtion will be executed
print(result)
print(  checkNum()  )