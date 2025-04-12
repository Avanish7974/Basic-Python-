# Exception handling in Python is a mechanism to manage errors that occur during the execution of a program. When an error, or exception, arises, it can disrupt the normal flow of the program. Exception handling allows the program to gracefully handle these errors, preventing abrupt termination and potentially recovering from the error.
# An exception is a python object that represents error there are basically two types of error 1. SyntaxError 2. logical error
# the logical error is known as Exception and python have capability to handle logical error it is called exception error handling

# try:
#     the code will generate an error
# except:
#     this code display an Exception
a = int(input("Enter the no.1 :"))
b = int(input("Enter the no.2 :"))                
try:
    c=a/b
    print(c)
except:
    print("Cannot be divided by Zero")    
else:
    print(c)    
# we can also use else keyword with try and except     

