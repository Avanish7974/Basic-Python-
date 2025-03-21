# lambda function is a one line function and it is also called annonomus function in python 
# annonomus function is beenaam function



# NOTE : Lambda function is a return type function 

x = lambda y:y*12
print(x)
# this program return this  0x0000017FD08BCA40> whic is 

x = lambda y:y*12
print(x(12))

x = lambda y=18:y*12
print(x(12))

x = lambda y,z:y+z
print(x(12,45))