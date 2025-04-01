# Constructor in python
# constructor are special type of function that can call automatically when we create an object of a class in python.
# To create a constructor in python we use __init__() when constructor are calls automatically they can initialized a memory 

class myclass:
    def __init__(self,fnm,snm):
        self.fnm=fnm
        self.snm=snm
        print("Hello")
    def myfunction(self):
        print("User define",self.fnm,self.snm)
obj = myclass("Avanish","Singh")
obj.myfunction()            
    

