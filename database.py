import sqlite3

# Connect to sqlite (creates 'geek.db' if it doesn't already exist)
connection_obj = sqlite3.connect('geek.db')

# Create a cursor object
cursor_obj = connection_obj.cursor()

# Drop table if it already exists (to start fresh)
cursor_obj.execute("DROP TABLE IF EXISTS GEEK")

# Create the GEEK table
table = """
CREATE TABLE GEEK(
    Email VARCHAR(255) NOT NULL,
    Name VARCHAR(25) NOT NULL,
    Score INT
);
"""

cursor_obj.execute(table)

# Insert some data into the GEEK table
data = [
    ("geekk1@gmail.com", "Geek1", 25),
    ("geekk2@gmail.com", "Geek2", 15),
    ("geekk3@gmail.com", "Geek3", 36),
    ("geekk4@gmail.com", "Geek4", 27),
    ("geekk5@gmail.com", "Geek5", 40),
    ("geekk6@gmail.com", "Geek6", 14),
    ("geekk7@gmail.com", "Geek7", 10)
]

cursor_obj.executemany("INSERT INTO GEEK (Email, Name, Score) VALUES (?, ?, ?)", data)

# Commit the changes
connection_obj.commit()

# Query and display all rows from the GEEK table
cursor_obj.execute("SELECT * FROM GEEK")
rows = cursor_obj.fetchall()
print("GEEK table contents:")
for row in rows:
    print(row)

# Close the connection
connection_obj.close()