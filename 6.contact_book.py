import sqlite3

connection = sqlite3.connect("contact.db")

cursor  = connection.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS
contacts(phonenumber TEXT, name TEXT)""")


while True:
   try:
      choice = int(input('Press 1 to show contacts and 2 to add: '))
      if choice == 1:
         name = input('Name: ')
         phonenumber = input('Phonenumber: ')
         cursor.execute(f"INSERT INTO contacts VALUES ('{phonenumber}','{name}')")
         connection.commit()
         connection.close()
         break
      elif choice == 2:
         for row in cursor.execute('SELECT * FROM contacts ORDER BY name'):
            print(row)
         connection.close()
         break
      else:
         raise ValueError('Invalid input')
   except:
      print('Not a valid input')