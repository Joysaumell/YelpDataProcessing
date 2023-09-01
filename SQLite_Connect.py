import sqlite3

conn = sqlite3.connect('C:\\Users\\joysa\\OneDrive\\Living in the US\\Tableau Public\\yelp_dataset\\Yelp_Database.db')
cursor = conn.cursor()

cursor.execute("SELECT * FROM business LIMIT 10;")
rows = cursor.fetchall()

for row in rows:
    print(row)

conn.close()
