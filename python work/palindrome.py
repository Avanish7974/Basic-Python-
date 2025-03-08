# program to check the number is palindrome or not
n = int(input("Enter the number : "))
ori = n
sum = 0
while(n>0):
    rem = n%10
    sum = sum*10 + rem
    n = n//10
print("The Reverse of given digit is : ",sum)
if(ori==sum):
    print("Number IS Palindrome")
else:
    print("number is not palindrome") 