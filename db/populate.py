import sqlite3

def populateAnimals(t):
    '''iterate over all the creatures and put them in the db'''
    conn = sqlite3.connect('my_db')
    curs = conn.cursor()
    # here is a generic SQL statement
    st = '''
    INSERT INTO zoo
    VALUES (?, ?, ?)'''
    for item in t:
        curs.execute(st,( item['creature'], item['count'], item['cost']))
        conn.commit()
    conn.close()

if __name__ == '__main__':
    creatures_t = ( # normally this comes from JSON or API etc.
        {'creature':'Albatros', 'count':1,      'cost':120.99},
        {'creature':'Bear',     'count':5,      'cost':323.56},
        {'creature':'Carp',     'count':120,    'cost':87.00},
        {'creature':'Deer',     'count':121,    'cost':12.99},
        {'creature':'Elk',      'count':7,      'cost':73.47},
    )
    populateAnimals(creatures_t)