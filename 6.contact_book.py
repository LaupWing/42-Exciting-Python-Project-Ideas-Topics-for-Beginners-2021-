import sqlite3

connection = sqlite3.connect("contact.db")

cursor  = connection.cursor()

command1 = """CREATE TABLE IF NOT EXISTS
stores(contact_id INTEGER PRIMARY KEY, phonenumber INTEGER, name TEXT)"""

cursor.execute(command1)