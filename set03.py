# wap to make crud operation in set

# CRUD - Create Read Update Delete
s = set()
while(True):
    ch=int(input("Enter Choice : "))
    if(ch == 1):
        n= int(input("Enter the number of data : "))
        for i in range(n):
            data = input("enter data value : ")
            set.add(data)
    elif(ch==2):
        print(set)
    elif(ch==3):
        n = int(input("Enter the number of data to remove  : "))
        for i in range(n):
            data = input("Entet thr data to remove : ")
            ls.remove(data)
    elif(ch==4):
        n = int(input("Enter the index : "))
        data = int(input("Enter the data :"))
        ls[n]=data
    elif(ch==5):
        n= int(input("Enter the number of data : "))
        for i in range(n):
            n1 = int(input("Enter the index : "))
            data = input("enter data value : ")
            ls.insert(n1,data)             
        
                
