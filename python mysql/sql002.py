class dbconn:
    def __init__(self):
        import mysql.connector
        self.mydb=mysql.connector.connect(
            host="localhost",
            user="root",
            password="0000",
            database="python"
        )
        self.mycursor=self.mydb.cursor()
    def recordinsert(self,rollno,name,address,class1):
        self.rollno = rollno
        self.name = name
        self.address = address
        self.class1 = class1
        sql="insert into data2 (rollno,name,address,class1) values(%s,%s,%s,%s)"    
        value = [self.rollno,self.name,self.address,self.class1]
        self.mycursor.execute(sql,value)
        self.mydb.commit()
        print(" Successfully added")
