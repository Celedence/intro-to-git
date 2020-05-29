import sqlite3
connection = sqlite3.connect("my_friends.db")

c = connection.cursor()

people = [
    ("Ronald", "McDonald", 6),
    ("Danny", "Goodi", 7),
    ("Homer", "Simpson", 4),
    ("Alex", "Skolnick", 8)
]

# c.executemany("INSERT INTO friends VALUES (?,?,?)", people)

for person in people:
    c.execute("INSERT INTO friends VALUES (?,?,?)", person)
    print("inserting data")


# c.execute(query, data)

connection.commit()
connection.close()