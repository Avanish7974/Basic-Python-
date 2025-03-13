print("Hlo")
# EVAL IS EVALUTAION
# it basically do the work of calculator
ch=eval(input("Enter Your choice : "))
print(ch)
# 10*20
print("hlo")
k = int(input("Enter the Starting number : "))
j = int(input("Enter the ending number : "))
if k>0:
    for i in range(k,j+1):
        cnt = 0
        for j in range(1,i+1):
            if(i%j==0):
                cnt+=1
        if(cnt==2):
            print("prime number are ",i) 
        elif(cnt==4):
            print("4 factors are ",i)           

# n = 12345
# sum = 0
# while(n>0):
#     rem = n%10
#     sum = sum*10 + rem
#     n = n//10

# print(sum)    

# # program for sum of given no.
# n = 245
# sum = 0
# while(n>0):
#     rem = n%10
#     sum = sum+ rem
#     n = n//10

# print(sum)

# # # program to square of given number
# n = 999
# sum = 0
# while(n>0):
#     rem = n%10
#     sum = sum+ rem*rem
#     n = n//10

# print(sum)

# # program to cude of given no.
# n = 153
# sum = 0
# while(n>0):
#     rem = n%10
#     sum = sum+ rem*rem*rem
#     n = n//10

# print(sum)

# # program for armstrong number
# n = 153
# ori = n
# sum = 0
# while(n>0):
#     rem = n%10
#     sum = sum+ rem*rem*rem
#     n = n//10

# print(sum)
# if(ori==sum):
#     print("Number is armstrong")
# else:
#     print("no. is not armstrong")

# # program for multiply of given no.
# n = 234
# sum =1
# while(n>0):
#     rem = n%10
#     sum = sum* rem
#     n = n//10

# print(sum)
# # progfram to print factorial of given no.
# n = 5
# fact = 1
# while(n>0):
#     fact = fact*n
#     n-=1
# print(fact)    

# program to print fibonaci series
n = 5
x = 0
y = 1
z = 0
while(z<=5):
    print(z)
    x=y
    y=z
    z=x+y
n = 5
x = 0
y = 1
z = 0
while(z<=5):
    print(z)
     
    

# 4. return with  argument
def return_noargument(a,b):
    
    c=a+b
    d = a*b
    return c,d
x = return_noargument(10,20)
add = 0
print(x)
for i in x:
    add = add + i
    print(add)

# WAP using function wih all 4 type. Also use while loop and for loop to make a choice based of 20 program in which 10 are from patterns and 10 are from armstron,lcm,hcf,prime etc.
    
# note : user can exit from the program only on press 21    
# select salary from c1 inner join c2 on c1.c_id>c2.c_id;
# row draw by i and x axis
# column draw by j and y axis

# to print square
for i in range(1,6):
    for j in range(1,6):
        print(i,end=" ")
    print()    

# to print left triangle    

print("Hlo")
# EVAL IS EVALUTAION
# it basically do the work of calculator
ch=eval(input("Enter Your choice : "))
print(ch)
# 10*20
print("hlo")
k = int(input("Enter the Starting number : "))
j = int(input("Enter the ending number : "))
if k>0:
    for i in range(k,j+1):
        cnt = 0
        for j in range(1,i+1):
            if(i%j==0):
                cnt+=1
        if(cnt==2):
            print("prime number are ",i) 
        elif(cnt==4):
            print("4 factors are ",i)           

# n = 12345
# sum = 0
# while(n>0):
#     rem = n%10
#     sum = sum*10 + rem
#     n = n//10

# print(sum)    

# # program for sum of given no.
# n = 245
# sum = 0
# while(n>0):
#     rem = n%10
#     sum = sum+ rem
#     n = n//10

# print(sum)

# # # program to square of given number
# n = 999
# sum = 0
# while(n>0):
#     rem = n%10
#     sum = sum+ rem*rem
#     n = n//10

# print(sum)

# # program to cude of given no.
# n = 153
# sum = 0
# while(n>0):
#     rem = n%10
#     sum = sum+ rem*rem*rem
#     n = n//10

# print(sum)

# # program for armstrong number
# n = 153
# ori = n
# sum = 0
# while(n>0):
#     rem = n%10
#     sum = sum+ rem*rem*rem
#     n = n//10

# print(sum)
# if(ori==sum):
#     print("Number is armstrong")
# else:
#     print("no. is not armstrong")

# # program for multiply of given no.
# n = 234
# sum =1
# while(n>0):
#     rem = n%10
#     sum = sum* rem
#     n = n//10

# print(sum)
# # progfram to print factorial of given no.
# n = 5
# fact = 1
# while(n>0):
#     fact = fact*n
#     n-=1
# print(fact)    

# program to print fibonaci series
n = 5
x = 0
y = 1
z = 0
while(z<=5):
    print(z)
    x=y
    y=z
    z=x+y
n = 5
x = 0
y = 1
z = 0
while(z<=5):
    print(z)
     
    

# 4. return with  argument
def return_noargument(a,b):
    
    c=a+b
    d = a*b
    return c,d
x = return_noargument(10,20)
add = 0
print(x)
for i in x:
    add = add + i
    print(add)

# WAP using function wih all 4 type. Also use while loop and for loop to make a choice based of 20 program in which 10 are from patterns and 10 are from armstron,lcm,hcf,prime etc.
    
# note : user can exit from the program only on press 21    
# select salary from c1 inner join c2 on c1.c_id>c2.c_id;
# row draw by i and x axis
# column draw by j and y axis

# to print square
for i in range(1,6):
    for j in range(1,6):
        print(i,end=" ")
    print()    

# to print left triangle    

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


# k = int(input("1 : "))

# n = int(input("2 : "))
for i in range(7):

    for j in range(5):
        if( i== 3 or j==2 or (j==4 and i>=3) or   (j==0 and i<=3) or (i==0 and j>=2) or (i==6 and j<=2) or (i==1 and j<=2) ):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()    
    

# prim