import sqlite3

def readDB():
    '''read and display everything in our database'''
    conn = sqlite3.connect('my-db')
    curs = conn.cursor()
    st = '''
    SELECT creature, qty, cost FROM zoo
    '''
    curs.execute(st)
    conn.commit()
    # we can now access any rows of data returned
    rows = curs.fetchall()
    return rows

if __name__ == '__main__':
    results = readDB()
    for animal in results:
        print(f'we have {animal[1]} {animal[0]} each costing {animal[2]}')