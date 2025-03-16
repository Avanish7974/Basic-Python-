# Control Structure Statement (loop)
# Difference in for loop and while loop
# program that is done by for loop also runs by while loop but in for

# Wap to add first 10 natural number
n = int(input("Enter the Number : "))
i = 1
sum = 0
s = 0
su = 0
while(i<=n):
    print("while loop ",i)
    su = su + i
    if(i%2==0):
        sum = sum + i  
   
    else:
        s = s + i
    i+=1

print("The sum of Even numbers is : ",sum) 
print("The sum of odd numbers is : ",s) 
print("The sum of while  loop is : ",su) 

# wap to find the 1-2+3-4+5---- input taken from user
# wap to find factorial of any number take input
# find the sum of factorial 1 + factorial 2 + fact 3---- 
# wap to find the sum of factorial 1 - fact 2+ fact 3-fact 4-----
# find the no. of factor of any no. also show the factor takee input
# wap to print fibonacci series input take
# wap to reverse the input digit 
# wap to sum th input digit
# wap to check the no. is prime or not in three different ways  
# wap to check no. is palindrome or not
# wap to check is armstrong
 