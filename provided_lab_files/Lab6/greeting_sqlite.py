import sqlite3
conn = sqlite3.connect('greetings.db')
c = conn.cursor()
c.execute('CREATE TABLE IF NOT EXISTS greetings (name TEXT)')
c.execute('INSERT INTO greetings VALUES (?)', ('DevOps Student',))
conn.commit()
conn.close()
print("Greeting saved to database.")