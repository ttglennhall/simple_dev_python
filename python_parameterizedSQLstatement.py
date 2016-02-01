# The sqlite3 module is used to work with the SQLite database.
import sqlite3 as lite

cities = (('Las Vegas', 'NV'), ('Atlanta', 'GA'))

weather = (('Las Vegas', 2013, 'July', 'December', 15), ('Atlanta', 2013, 'July', 'January', 22))

# Here you connect to the database. The `connect()` method returns a connection object.
con = lite.connect('data/getting_started.db')

with con:
  # From the connection, you get a cursor object. The cursor is what goes over the records that result from a query.
  cur = con.cursor()    
  cur.executemany("INSERT INTO cities VALUES(?,?)", cities)
  cur.executemany("INSERT INTO weather VALUES(?,?,?,?,?)", weather)
  
  cur.execute('SELECT SQLITE_VERSION()')
  # You're fetching the data from the cursor object. Because you're only fetching one record, you'll use the `fetchone()` method. If fetching more than one record, use the `fetchall()` method.
  data = cur.fetchone()
  # Finally, print the result.
  print("SQLite version: %s" % data)