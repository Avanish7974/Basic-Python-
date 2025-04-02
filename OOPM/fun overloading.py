# function Overloading
# When we declare more than one function with having same name but passing parameter is different this concept is known as function ovrloading or method overloading

# function Overriding

# When we declare more than one function with having same name and passing parameter is also same  this concept is known as function ovveriding or method overriding

class dadaji :
    def dadaji1(self):
        print("This is the property of Dadaji ")
class betaji(dadaji):
    def betaji1(self):
        print("This is the property of betaji ")  
class potaji(betaji):
    def potaji1(self):
        print("Property of potaji")              
ob = potaji()
ob.dadaji1()
ob.potaji1()
ob.betaji1()