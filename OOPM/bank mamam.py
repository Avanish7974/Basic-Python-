class sbi:
    def sbibank(self,accno):
        self.accno = accno
        lsaccno = [123,456,765,876]
        lsaccname = ["a","b","c","d"]
        for i in lsaccno:
            if(accno==i):
                x = lsaccno.index(accno)
                print("YOur name ",lsaccname[x])
                break
            else:
                print("not match")

        
ob = sbi()
ob.sbibank(876)        