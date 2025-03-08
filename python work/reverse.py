# program to reverse the digit
n = int(input("Enter the number : "))
sum = 0
while(n>0):
    rem = n%10
    sum = sum*10 + rem
    n = n//10
print("The Reverse of given digit is : ",sum)