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

# some other DB conn mechanisms
# see https://wiki.python.org/moin/DatabaseInterfaces
# DB2
# import DB2 # remember to pip install first!!
# conn = DB2.connect(dsn='ibm-DB', uid='analyst', pwd='db2pwd')

# Sybase
# import Sybase
# conn = Sybase.connect('SYBASE', 'username', 'passwd', 'databasename')

# Oracle
# import cx_Oracle
# conn = cx_Oracle.connect('username', 'passwd', 'hostname:port/SID')
# conn2 = cx_Oracle.connect('username/passwd@hostname:portno/SID')
# dsn_tns = cx_Oracle.makedsn('hostname', portno, 'SID')
# conn3 = cx_Oracle.connect('username', 'passwd', dsn_tns)

# MySQL
# import MySQLdb
# conn = MySQLdb.connect(host = "hostname", user = "username", passwd = "password", db = "dbname")

# PySQLite
# from pysqlite2 import dbapi2 as sqlite
# conn = sqlite.connect("mydb", connectionproperties)

# ODBC
# import odbc
# conn = odbc. odbc("myDSN/username/password")