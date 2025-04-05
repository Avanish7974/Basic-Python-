# when we perform addition,subtraction,multiplication and so on ,on a object of an class we can overload the operator using magic method 

# these are magic methods
class class1:
    def __init__(self,PARA):
        self.para=PARA
    def __mul__(self,other):
        return self.para*other.para
    def __le__(self,other):
        return self.para<=other.para
    def __ls__(self,other):
        return self.para<=other.para
ob1 = class1(100)
ob2 = class1(200)
print(ob1*ob2)   
print(ob1<=ob2)
print(ob1<ob2)



class mycls:
    def func1(self,para):
        self.para=para
    def __add__(self,other):
        return self.para + self.other
ob = mycls(100)
print(ob)        
    