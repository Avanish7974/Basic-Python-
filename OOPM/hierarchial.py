# in this class one class accessed by more than one class is known as hierarchial 
class BANK:
    def rbiroi(self,amt):
        self.amt = amt
        self.ir =self.amt*12/100
        print("RBIROI ",self.ir)
class sbibank(BANK):
    def sbiroi(self,amt):
        self.amt = amt
        self.ir =self.amt*12/100
        print("sbiROI ",self.ir)
class iciciBANK(BANK):
    def iciciroi(self,amt):
        self.amt = amt
        self.ir =self.amt*12/100
        print("iciciROI ",self.ir) 
obj = iciciBANK()
obj.iciciroi(1000)
obj.rbiroi(15000)                       
