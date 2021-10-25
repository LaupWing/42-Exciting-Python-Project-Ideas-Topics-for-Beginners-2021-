import sqlite3

connection = sqlite3.connect("contact.db")

cursor  = connection.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS
contacts(phonenumber INTEGER, name TEXT)""")
cursor.execute("INSERT INTO contacts VALUES ('0654754116','Loc Nguyen')")

connection.commit()
connection.close()