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

