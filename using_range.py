# a range lets us generate a series of integer values
my_range = range(0, 26, 5) # (start, stop-before, step)
for i in my_range:
    print(i)

r2 = range(-99, 100, 2)
odd_tuple = tuple(r2) # all the values from the range now exist in a tuple
print(odd_tuple)

# we may generate a collection of calculated values
squares = [i*i for i in range(0,11)] # the [] return a list
print(squares)