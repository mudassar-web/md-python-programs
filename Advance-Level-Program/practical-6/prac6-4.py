"""Aim : Program to show database connectivity

Write a program to insert the following information:
Table: Item

Itemno	Iname		    Price	Quantity
101		Geometry Box 	50 	    100
102		Soap 		    100 	50
103		Perfume		    150	    25
104		Pen		        50	    200
105		Pencil		    20	    100

Write queries based upon Item table given
a) Display all items information.
#b) Display item name and price value.
c) Display soap information.
d) Display the item information whose name starts with letter 'p'.
e) Display a report with item number, item name and total price. (total price = price * quantity).
f) Display item table information in ascending order based upon item name.
#g) Display item name and price in descending order based upon price.
h) Display item name, whose price is in between 50 to 100.
i) Add new column totalprice with number (10, 2).
j) Increase price value by 100.
k) Fill up totalprice = price * quantity.
l) Remove pen information.
#m) Remove totalprice column.
#n) Remove whole item structure."""

import mysql.connector

db=mysql.connector.connect(user='root',password='',
            host='127.0.0.1',database='fycs')
cursor=db.cursor()
"""
cursor.execute("create table Item(ItemNo int,Iname text,Price int,Quantity int)")
cursor.execute("insert into Item values(101,'Geometry Box',50,100)")
cursor.execute("insert into Item values(102,'Soap',100,50)")
cursor.execute("insert into Item values(103,'Perfume',150,25)")
cursor.execute("insert into Item values(104,'Pen',50,200)")
cursor.execute("nsert into Item values(105,'Pencil',20,100)")
"""
cursor.execute("select * from Item")
results=cursor.fetchall()
print('{:5s}\t{:15s}\t{:5s}\t{:5s}'.format('Itemno','Iname','Price','Quantity'))
for row in results:
    itemno=row[0]
    iname=row[1]
    price=row[2]
    qty=row[3]
    print('{:5d}\t{:15s}\t{:5d}\t{:5d}'.format(itemno,iname,price,qty))
    
"""
print('-'*35)
cursor.execute("select Iname,Price from Item")
results=cursor.fetchall()
print('{:15s}\t{:5s}'.format('Iname','Price'))
for row in results:   
    iname=row[0]
    price=row[1]
    print('{:15s}\t{:5d}'.format(iname,price))
"""

print('-'*35)
cursor.execute("select * from Item where Iname='Soap'")
results=cursor.fetchall()
print('{:5s}\t{:15s}\t{:5s}\t{:5s}'.format('Itemno','Iname','Price','Quantity'))
for row in results:
    itemno=row[0]
    iname=row[1]
    price=row[2]
    qty=row[3]
    print('{:5d}\t{:15s}\t{:5d}\t{:5d}'.format(itemno,iname,price,qty))
    
print('-'*35)
cursor.execute("select * from Item where Iname like 'P%'")
results=cursor.fetchall()
print('{:5s}\t{:15s}\t{:5s}\t{:5s}'.format('Itemno','Iname','Price','Quantity'))
for row in results:
    itemno=row[0]
    iname=row[1]
    price=row[2]
    qty=row[3]
    print('{:5d}\t{:15s}\t{:5d}\t{:5d}'.format(itemno,iname,price,qty))

print('-'*35)
cursor.execute("select Itemno,Iname,(Price*Quantity) from Item")
results=cursor.fetchall()
print('{:5s}\t{:15s}\t{:5s}'.format('Itemno','Iname','Total Price'))
for row in results:
    itemno=row[0]
    iname=row[1]
    price=row[2]
    print('{:5d}\t{:15s}\t{:5d}'.format(itemno,iname,price))

print('-'*35)
cursor.execute("select * from Item order by iname")
results=cursor.fetchall()
print('{:5s}\t{:15s}\t{:5s}\t{:5s}'.format('Itemno','Iname','Price','Quantity'))
for row in results:
    itemno=row[0]
    iname=row[1]
    price=row[2]
    qty=row[3]
    print('{:5d}\t{:15s}\t{:5d}\t{:5d}'.format(itemno,iname,price,qty))

""" 
print('-'*35)
cursor.execute("select * from Item order by price desc")
results=cursor.fetchall()
print('{:5s}\t{:15s}\t{:5s}\t{:5s}'.format('Itemno','Iname','Price','Quantity'))
for row in results:
    itemno=row[0]
    iname=row[1]
    price=row[2]
    qty=row[3]
    print('{:5d}\t{:15s}\t{:5d}\t{:5d}'.format(itemno,iname,price,qty))
"""

print('-'*35)
cursor.execute("select Iname,Price from Item where price>=50 and price<=100")
results=cursor.fetchall()
print('{:15s}\t{:5s}'.format('Iname','Price'))
for row in results:   
    iname=row[0]
    price=row[1]
    print('{:15s}\t{:5d}'.format(iname,price))
    
"""
cursor.execute("alter table Item add TotalPrice numeric(10,2)")

cursor.execute("update Item set price=price+100")

cursor.execute("update Item set totalprice=price*quantity")

"""


print('-'*35)
cursor.execute("select * from Item")
results=cursor.fetchall()
print('{:5s}\t{:15s}\t{:5s}\t{:5s}\t{:5s}'.format('Itemno','Iname','Price','Quantity','Total Price'))
for row in results:
    itemno=row[0]
    iname=row[1]
    price=row[2]
    qty=row[3]
    tp=row[4]
    print('{:5d}\t{:15s}\t{:5d}\t{:5d}\t{:5f}'.format(itemno,iname,price,qty,tp))

"""
cursor.execute("delete from Item where iname='pen'")

cursor.execute("alter table Item drop totalprice")

cursor.execute("drop table Item")
"""

db.commit()
db.close()
