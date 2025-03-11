# while(True):
#     # here int do type casting type casting of string to int 
#     ch = int(input("Enter your Choice : \n\t"))
#     # \n do the line change
#     # \t do the space of one tab 4 to 5 space
#     if(ch==1):
#         print("press 1")
#     elif(ch==2):
#         print("press 2") 
#     elif(ch==3):
#         print("print3")
#     elif(ch==4):
#         print("print4")   
#         break
#     else:
#         print("wrong")

while(True):
    print("welcome to restaurant : ")
    print("Press 1 fro samosa \n press 2 for jalebi : ")
    ch = int(input("enter your choice : "))
    if(ch==1):
        print("The price of one samosa is : 12")
        sa = int(input(" How many samosa you want :  "))
        ch = 12*sa
        if(ch>=12):
            print("Your price is : ",ch)
            break
 

    elif(ch==2):
        print("The price of one jalebi is : 12")
        da = int(input(" How many jalebi you want :  "))
        dh = 12*da
        if(dh>=12):
            print("Your price is : ",dh)
            break 


print("kl")

