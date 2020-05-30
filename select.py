import sqlite3
conn = sqlite3.connect("my_friends.db")

c = conn.cursor()
c.execute("SELECT * FROM friends WHERE first_name IS 'Homer'")


print(c.fetchone())

conn.commit()
conn.close()
