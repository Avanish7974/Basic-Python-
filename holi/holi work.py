# 1. No return no argument 
def noreturn_noargument():
    a=10
    b=10
    c=a+b
    print("addition = ",c)
noreturn_noargument()

# 2. No Return With  argument 
def noreturn_withargument(n):
    for i in range(1,n+1,1):
        for j in range(1,i+1,1):
            print(i,end=" ")
        print()    
 
noreturn_withargument(5)        

# 3. Return With no Argument
def return_noargument():
    a=10
    b=20
    c=a+b
    d = a*b
    return c,d
x = return_noargument()
add = 0
print(x)
for i in x:
    add = add + i
    print(add)
    
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

while(True):
    ch=int(input("Enter THe number : "))
    if(ch==1):
        print("press 1")
    elif(ch==2):
        print("press 2")    
    elif(ch==3):
        print("press 3")
    elif(ch==4):
        print("press 4") 
        break
    else:
        print("Wrong")
