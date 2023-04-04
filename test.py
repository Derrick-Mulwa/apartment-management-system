import mysql.connector

# read the binary data from the file
with open(r"C:\Users\Administrator\Downloads\-2-bedroom-apartments-for-sale-in-juja-6x2id.jpg", 'rb') as f:
    file_data = f.read()

# connect to the database
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
)

# insert the binary data into the database as a longblob
mycursor = conn.cursor()
query = "INSERT INTO apartment_name.properties(house_number, picture) VALUES (%s, %s)"
values = ('Friendscorner Apartments', file_data)
mycursor.execute(query, values)
conn.commit()
# mycursor.execute("SELECT count(*) FROM apartment_name.properties;")
# count = [i for i in mycursor][0][0]

# print(count)
