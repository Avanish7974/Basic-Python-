print("Hlo")
# EVAL IS EVALUTAION
# it basically do the work of calculator
ch=eval(input("Enter Your choice : "))
print(ch)
# 10*20
print("hlo")
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

# n = 12345
# sum = 0
# while(n>0):
#     rem = n%10
#     sum = sum*10 + rem
#     n = n//10

# print(sum)    

# # program for sum of given no.
# n = 245
# sum = 0
# while(n>0):
#     rem = n%10
#     sum = sum+ rem
#     n = n//10

# print(sum)

# # # program to square of given number
# n = 999
# sum = 0
# while(n>0):
#     rem = n%10
#     sum = sum+ rem*rem
#     n = n//10

# print(sum)

# # program to cude of given no.
# n = 153
# sum = 0
# while(n>0):
#     rem = n%10
#     sum = sum+ rem*rem*rem
#     n = n//10

# print(sum)

# # program for armstrong number
# n = 153
# ori = n
# sum = 0
# while(n>0):
#     rem = n%10
#     sum = sum+ rem*rem*rem
#     n = n//10

# print(sum)
# if(ori==sum):
#     print("Number is armstrong")
# else:
#     print("no. is not armstrong")

# # program for multiply of given no.
# n = 234
# sum =1
# while(n>0):
#     rem = n%10
#     sum = sum* rem
#     n = n//10

# print(sum)
# # progfram to print factorial of given no.
# n = 5
# fact = 1
# while(n>0):
#     fact = fact*n
#     n-=1
# print(fact)    

# program to print fibonaci series
n = 5
x = 0
y = 1
z = 0
while(z<=5):
    print(z)
    x=y
    y=z
    z=x+y
n = 5
x = 0
y = 1
z = 0
while(z<=5):
    print(z)
     
    

