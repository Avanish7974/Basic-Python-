class myclass:
    def display(self,fnm,lnm):
        self.fnm = fnm
        self.lnm = lnm
    def show(self):    

        print("Hllo display",self.fnm,self.lnm)
ob = myclass()
n1 = int(input("Enter first number :"))  
n2 = int(input("Enter Second number :"))          
ob.display(n1,n2) 
ob.show()

# WAP to make calculator using self and return type with argument function input taken frm user
