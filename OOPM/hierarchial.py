# in this class one class accessed by more than one class is known as hierarchial 
class BANK:
    def rbiroi(self,amt):
        self.amt = amt
        self.ir =self.ir*12/100
        print("RBIROI ",self.ir)
class sbibank:
    def sbiroi(self,amt):
        self.amt = amt
        self.ir =self.ir*12/100
        print("sbiROI ",self.ir)
class iciciBANK:
    def iciciroi(self,amt):
        self.amt = amt
        self.ir =self.ir*12/100
        print("iciciROI ",self.ir)                