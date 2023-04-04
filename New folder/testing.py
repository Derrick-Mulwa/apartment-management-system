import mysql.connector

db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "root"
)

mycursor = db.cursor()

session_user_id = '24568121'

mycursor.execute(f"SELECT first_name, last_name, house_number FROM apartment_name.details WHERE id_number = '{session_user_id}';")

v = [i for i in mycursor][0]
first_name =  v[0]
house = v[2]

full_names = f'{v[0]} {v[1]}'
from datetime import datetime

print(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")