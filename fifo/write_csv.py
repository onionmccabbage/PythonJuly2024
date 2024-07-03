# we will write a comma-separated text file

def writeCSV(w):
    '''output the incoming data as csv'''
    with open('animals.csv', 'at') as fout:
        # we loop over the tuple
        for animal in w:
            # and we loop over the dict
            for (k,v) in animal.items():
                # we now write to csv
                print(v, end=', ', file=fout) # we can specify ANY end character instead of new-line
            # then we end each line
            print('\n', file=fout) 

if __name__ == '__main__':
    creatures_t = (
        {'creature':'Albatros', 'count':1,      'cost':120.99},
        {'creature':'Bear',     'count':5,      'cost':323.56},
        {'creature':'Carp',     'count':120,    'cost':87.00},
        {'creature':'Deer',     'count':121,    'cost':12.99},
        {'creature':'Elk',      'count':7,      'cost':73.47},
    )
    writeCSV(creatures_t)
