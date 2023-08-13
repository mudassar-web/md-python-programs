"""Aim : Create database FY<rollno> in mysql and
from python create table student and insert record
in table""" 

import mysql.connector
db = mysql.connector.connect(user='root',\
      password='',  host='127.0.0.1', database='fycs')
cursor = db.cursor()
cursor.execute("""create table students
      (rollno int,sname text,class text)""")
cursor.execute("insert into students values(1,'Asif','MSc')")
cursor.execute("insert into students values(2,'Ajay','BSc')")
cursor.execute("insert into students values(3,'James','BA')")
cursor.execute("select count(*) from students")
data = cursor.fetchone()
print ("Row count: %s" % data)
#print ("Row count: ",str(data))
db.commit()
db.close()
