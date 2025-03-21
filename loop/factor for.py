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


    

