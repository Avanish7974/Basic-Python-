# find the no. of factor of any no. also show the factor taken input
n = int(input("Enter the number : "))
sum = 0
i = 1
fact = 1
while(i<=n):
    print("The Factorial Of number is : ",n)
    fact = fact*i
    sum = sum + fact
    n-=1
print("The sum of number is : ",sum)    

