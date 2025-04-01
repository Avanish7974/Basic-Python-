# Dectructor are special type of function which is calls automatically when any object release the memory.

# To create a destructor we can use __del__() 

class myclass:
    def __init__(self):
        print("This is constructor ")
    def func1(self):
        print("This is normal function ")
    def __del__(self):
        print("Tihs is destructor ")
ob = myclass()  
ob.func1()      
