#Aim :Installing mysql connector and checking the version of mysql from python

import mysql.connector

db = mysql.connector.connect(user='root',\
      password='',host='127.0.0.1', database='test')
cursor = db.cursor()
cursor.execute("SELECT VERSION()")
data = cursor.fetchone()
#print(data)
print ("Database version : %s " % data)
db.close()
