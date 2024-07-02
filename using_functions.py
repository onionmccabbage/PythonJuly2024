# in Python we may gather code together into a reuseable function
def checkEven(n):
    '''this is a docstring
    we can declare the purpose of our function
    We will return True if a value is even and False otherwise'''
    if n%2 == 0: # % will return the remainder after division
        return True # careful - Python is a case-sensitive language 
    else:
        return False


# we may call our functions whenever we like
result = checkEven(42) # at this point our funtion will be executed
print(result)