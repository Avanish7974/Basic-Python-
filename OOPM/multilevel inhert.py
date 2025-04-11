# multilevel inheritance - in multilevel inheritance the one class can be inherited by another and further this
# class are also inherited by another class so that we get multileveel


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

class sbi:
    def rbiroi(self):
        accno = 12345
        bal = 76777
        ir = bal*0.1
        return ir
class SBI(RBI):
    def sbiroi(self):
        return "7%"    
class PNB(SBI):
    def pnbroi(self):
        return "6%"
class ICICI(PNB):
    def iciciroi(self):
        return "12%"            
    
ob = ICICI()
print("ICICI ROI ",ob.iciciroi())
print("Roi rbi",ob.rbiroi())  

print()