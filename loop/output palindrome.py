# user 2 value insert karega hame output first value ke baad second value tak ke  palindrome no. show karna hai
# Nested while loop - when you declare more than one loop inside another loop that type of condition is known as nested loop.
# Syntax Error initialization of outer Look
# while(condition):
#     # initialization of inner loop
#     while(condition):
#         inc/dec of inner loop 
#     ind/dnc of outer loop    

i = int(input("Enter the number : "))
j = int(input("Enter the number : "))
num =i
while(num<=j):
    temp = num
    sum = 0
    
    while(temp>0):
        rem = temp%10
        sum = sum*10 + temp
        temp = temp//10

        if(num==sum):
            print("Is palindrome",num)
            
    
    num+=1        

   

       
