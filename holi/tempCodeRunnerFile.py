# 1. No return no argument 
def noreturn_noargument():
    a=10
    b=10
    c=a+b
    print("addition = ",c)


# 2. No Return With  argument 
def noreturn_withargument(n):
    for i in range(1,n+1,1):
        for j in range(1,i+1,1):
            print(i,end=" ")
        print()    
 
      

# 3. Return With no Argument
def return_noargument():
    a=10
    b=20
    c=a+b
    d = a*b
    return c,d

    
# 4. return with  argument
def return_argument(a,b):
    
    c=a+b
    d = a*b
    return c,d

while(True):
    ch=int(input("Which Type Of function You Want To Run 1,2,3,4 : "))
    if(ch==1):
        noreturn_noargument()
        
    elif(ch==2):
        noreturn_withargument(5)
            
# 1. No return no argument 
def noreturn_noargument():
    a=10
    b=10
    c=a+b
    print("addition = ",c)


# 2. No Return With  argument 
def noreturn_withargument(n):
    for i in range(1,n+1,1):
        for j in range(1,i+1,1):
            print(i,end=" ")
        print()    
 
      

# 3. Return With no Argument
def return_noargument():
    a=10
    b=20
    c=a+b
    d = a*b
    return c,d

    
# 4. return with  argument
def return_argument(a,b):
    
    c=a+b
    d = a*b
    return c,d

while(True):
    ch=int(input("Which Type Of function You Want To Run 1,2,3,4 : "))
    if(ch==1):
        noreturn_noargument()
        
    elif(ch==2):
        noreturn_withargument(5)
            
    elif(ch==3):
        x = return_noargument()
        add = 0
        print(x)
        for i in x:
            add = add + i
            print(add)
    elif(ch==4):
        x = return_argument(10,20)
        add = 0
        print(x)
        for i in x:
             add = add + i
             print(add) 
        break
    else:
        print("Wrong")
  # 1. No return no argument 
def noreturn_noargument():
    a=10
    b=10
    c=a+b
    print("addition = ",c)


# 2. No Return With  argument 
def noreturn_withargument(n):
    for i in range(1,n+1,1):
        for j in range(1,i+1,1):
            print(i,end=" ")
        print()    
 
      

# 3. Return With no Argument
def return_noargument():
    a=10
    b=20
    c=a+b
    d = a*b
    return c,d

    
# 4. return with  argument
def return_argument(a,b):
    
    c=a+b
    d = a*b
    return c,d

while(True):
    ch=int(input("Which Type Of function You Want To Run 1,2,3,4 : "))
    if(ch==1):
        noreturn_noargument()
        
    elif(ch==2):
        noreturn_withargument(5)
            
    elif(ch==3):
        x = return_noargument()
        add = 0
        print(x)
        for i in x:
            add = add + i
            print(add)
    elif(ch==4):
        x = return_argument(10,20)
        add = 0
        print(x)
        for i in x:
             add = add + i
             print(add) 
        break
    else:
        print("Wrong")
              