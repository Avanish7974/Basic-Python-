# # 2. Not return with argument 
def noreturn_withargument(n):
    for i in range(1,n+1,1):
        for j in range(1,i+1,1):
            print(i,end=" ")
        print()    
          
    
noreturn_withargument(5)        

# # 2. Default argument 
def noreturn_withargument(n=10):
    for i in range(n,0,-1):
        for j in range(1,i+1,1):
            print(i,end=" ")
        print()    
          
    
noreturn_withargument()      