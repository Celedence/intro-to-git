import sqlite3
connection = sqlite3.connect("my_friends.db")
# create cursor object
c = connection.cursor()
# execute some sql
# c.execute("CREATE TABLE friends (first_name TEXT, last_name TEXT, closeness INTEGER);")
# insert_query = """INSERT INTO friends VALUES ('Merryweather', 'Lewis', 7)"""

data = ("Steveo", "MCrackin", 9)

query = f"INSERT INTO friends VALUES (?, ?, ?)"


c.execute(query, data,)
connection.commit()
connection.close()