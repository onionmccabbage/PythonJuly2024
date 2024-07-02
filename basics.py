# this is a Python comment
# we may declare variables like this

a = 3  # this is an integer (a whoel number)
b = 7.4 # this is a float (it has decimal part)

print(a+b)
print(type(a), type(b))
print(a/b, a-b, a*b)

# we also have string data (an indexed collection of characters)
s = 'this is a string of characters'
print(s, type(s))
# we may slice any indexed collection
print(s[0]) # this is the character at postition zero, in this case the letter t
print(s[8:15]) # [start:stop-before]

# other collections
# tuple: an indexed collection of any data type IMMUTABLRE (we cannot alter members of the collection)
t = (5 ,4.3, True, False, 'hello', None) # a colecioton of arbitrary values
print(t, type(t))
# list: an indexed collecion of any data type: MUTABLE (we may alter members)
l = [77, True, 'hi', 42.222]
# we may alter the list
l.append('also') # also insert, remove and pop
l[2] = 'altered'
print(l, type(l))

# we may loop over any indexed collection
for i in s:
    print(i)
    
for i in t: # the colon indicates a clock of code
    print(i) # every line within the block of code must be indented