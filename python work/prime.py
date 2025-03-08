# program to check number is prime or not 
n = (int(input("Enter the number : "))) 
prime = 0

i = 1
while(i<=n):
    if(n%i==0):
        prime +=1
    i+=1
if(prime==2):
    print("Number is prime : ",n) 
else:
    print("Number is not prime : ",n) 

# Program 2 to check number is prime or not 
n = (int(input("Enter the number : "))) 
prime = 0

i = 2
while(i<n):
    if(n%i==0):
        prime +=1
    i+=1
if(prime==0):
    print("Number is prime : ",n) 
else:
    print("Number is not prime : ",n)  

# 3 method to find number is prime or not
n = (int(input("Enter the number : "))) 
prime = n/2
sum = 0
i = 2
print(prime)
while(i<=prime):
    if(n%i==0):
        sum +=1
    i+=1
if(sum==0):
    print("Number is prime : ",n) 
else:
    print("Number is not prime : ",n)  



