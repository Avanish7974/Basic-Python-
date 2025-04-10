import sql002

obj1 = sql002.dbconn
ch = int(input("Enter your choice : "))
if(ch==1):
    rollno=input("Enter roll:")
    name = input("Enter name ")
    address = input("Enter address ")
    class1 = input("Enter class : ")
    obj1.recordinsert(rollno,name,address,class1)
