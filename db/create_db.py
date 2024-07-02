import sqlite3 # this satabase comes with Python

def accessDB():
    '''create (or open) a database for animals
    Each animal will have a qty and cost'''
    conn = sqlite3.connect('my_db') # either create or connect to a DB
    curs = conn.cursor() # this lets us work with the database
    # we need an SQL statement
    st = '''
    CREATE TABLE zoo
    (  
        creature VARCHAR(32) PRIMARY KEY,
        qty int,
        cost float
    )
    '''
    # we use the cursor to execite and ten commit teh SQL statement
    curs.execute(st)
    conn.commit()
    conn.close()

if __name__ == '__main__':
    accessDB()