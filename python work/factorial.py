# Program to print sum of  Fatorial of number
n = int(input("Enter the number : "))
sum = 1
while(n>0):
    print("The factorial of number is : ",n)
    sum = sum * n
    n -=1
print("The factorial is ", sum) 

