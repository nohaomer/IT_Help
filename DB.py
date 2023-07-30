import sqlite3
conn = sqlite3.connect('ping.db')

# Creating a cursor object using the
# cursor() method
cursor = conn.cursor()

# Creating table
table = """CREATE TABLE Switches(
ID INTEGER PRIMARY KEY AUTOINCREMENT,
IP VARCHAR(255),
Name VARCHAR(255),
Location VARCHAR(255));

"""
# cursor.execute(table)
# Queries to INSERT records.
cursor.execute(
'INSERT INTO Switches (IP,Name,Location) VALUES (?, ?, ?)',( '8.8.8.8', 'DNS', 'MY home'))

cursor.execute('INSERT INTO Switches (IP,Name,Location)VALUES (?, ?, ?)',('10.0.100.138','GW','EGPI'))

# Display data inserted
# print("Data Inserted in the table: ")
# data = cursor.execute('''SELECT * FROM Devices''')
# for row in data:
#     print(row)

# Commit your changes in the database
conn.commit()

# Closing the connection
conn.close()