# when a one class inherit the property of more than one parent class is called multiple polymorphism

class sbi:
    def sbiroi(self,amt):
        self.amt=amt
        self.ir=self.ir*7.8/100
        print("SBI ROI = ",self.ir)
class icici:
    def iciciroi(self,amt):
        self.amt=amt
        self.ir=self.ir*9.8/100
        print("icici ROI = ",self.ir)
class hdfc:
    def hdfcroi(self,amt):
        self.amt=amt
        self.ir=self.ir*12.8/100
        print("hdfc ROI = ",self.ir)                
class BANK(sbi,hdfc,icici):
    pass
obj=BANK()

        