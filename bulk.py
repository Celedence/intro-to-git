import sqlite3
connection = sqlite3.connect("my_friends.db")

c = connection.cursor()

people = [
    ("Ronald", "McDonald", 6),
    ("Danny", "Goodi", 7),
    ("Homer", "Simpson", 4),
    ("Alex", "Skolnick", 8)
]

c.executemany("INSERT INTO friends VALUES (?,?,?)", people)

# c.execute(query, data)

connection.commit()
connection.close()