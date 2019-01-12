import sqlite3

'''
Steps:
 1. Connect to a database
 2. Create a cursor object
 3. Write an SQL query
 4. Commit changes
 5. Close database connection
'''

conn = sqlite3.connect('database.db')

c = conn.cursor()

sql = '''

CREATE TABLE IF NOT EXISTS users (
           id integer unique primary key autoincrement,
           name text
);

'''
c.execute(sql)
conn.commit()
conn.close()