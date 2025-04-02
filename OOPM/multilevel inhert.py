
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