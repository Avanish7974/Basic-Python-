
# k = int(input("1 : "))

# n = int(input("2 : "))
for i in range(7):

    for j in range(5):
        if( i== 3 or j==2 or (j==4 and i>=3) or   (j==0 and i<=3) or (i==0 and j>=2) or (i==6 and j<=2) or (i==1 and j<=2) ):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()    
    