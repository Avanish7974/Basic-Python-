# wap to make a crud operationon tuple
# CRUD - Create Read Update Delete
tup = ()
ls = list(tup)
# print(ls)
print(type(tup))
while(True):
    ch=int(input("Enter Choice : "))
    if(ch == 1):
        n= int(input("Enter the number of data : "))
        for i in range(n):
            data = input("enter data value : ")
            ls.append(data)
    elif(ch==2):
        print(ls)
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
    elif(ch==6):
        break  
    # ls3 = tuple(ls)       
    # print(type(ls3))        
           
ls3 = tuple(ls)       
print(type(ls3))


#  wap to append all the prime number in a list        
                
# methods or function of 