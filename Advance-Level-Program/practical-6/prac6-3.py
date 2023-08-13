#Aim : Write a python code to retrieve records from mysql and print it on th screen

import mysql.connector
db = mysql.connector.connect(user='root', password='',\
                  host='127.0.0.1', database='fycs')
cursor = db.cursor()
cursor.execute("select * from students")
results = cursor.fetchall()
print("Roll No Name Class")
print("-"*15)
for row in results:
  x = row[0]
  y = row[1]
  z = row[2]
  print(x ," " ,  y," " ,z)
db.close()
