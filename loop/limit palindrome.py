n1 = int(input("Enter the number : "))
n2 = int(input("Enter the number : "))
i =1
n1+=1

while(i<=n2):
    temp = n1
    rev = 0
    
    while(temp>0):
        r = temp%10
        rev = rev*10 + r
        temp = temp//10

        if(rev==n1):
            print("Is palindrome",rev)
            i+=1
    n1+=1  

#  wap using choice based user can exit from the program only if user can press 5      
