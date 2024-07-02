# remember a dict is a collection of key-value pairs
# they are NOT indexed by position

d = {'type':'Penguin', 'qty':32, 'cost':0.32}
d['food'] = 'fish' # we can access any member of a dict using square brackets

print(f'{d['type']} eats {d['food']}. we have {d['qty']} costing {d['cost']} each')