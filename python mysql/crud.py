# test mysql connection - to check the installation was successful or not write mysql.connector

import mysql.connector
print("Done")

mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="0000",
    database="python"

)
mycursor=mydb.cursor()
print("record manamegent system")
ch = int(input("Enter your choice : "))
if ch==1:
    rollno=input("Enter roll:")
    name = input("Enter name ")
    address = input("Enter address ")
    class1 = input("Enter class : ")
    sql="insert into data2 (rollno,name,address,class1) values(%s,%s,%s,%s)"
    value = [rollno,name,address,class1]
    mycursor.execute(sql,value)
    mydb.commit()
    print("added")d