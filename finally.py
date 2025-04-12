# the finally block is specified will be execute regardless if try block raises an error or not the finally block gets executed no matter if the try block raise any error or not 
a = int(input("Enter the no.1 :"))
b = int(input("Enter the no.2 :"))                
try:
    c=a/b
    print(c)
except:
    print("Cannot be divided by Zero")    
else:
    print(c)  
finally:
    print("CODE EXECUTED")    