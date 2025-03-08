# program to check the number is armstrong or not for three digit 
n = int(input("Enter the three digits  number : "))
ori = n
sum = 0
while(n>0):
    rem = n%10
    sum = sum + rem*rem*rem
    n = n//10
if(ori==sum):
    print("Number is armstrong : ",sum)
else:
    print("number is not armstrong : ",sum)

# program to check the number is armstrong or not for two digit 
n = int(input("Enter the two digit  number : "))
ori = n
sum = 0
while(n>0):
    rem = n%10
    sum = sum + rem*rem
    n = n//10
if(ori==sum):
    print("Number is armstrong : ",sum)
else:
    print("number is not armstrong : ",sum)      