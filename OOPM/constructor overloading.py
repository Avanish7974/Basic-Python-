class classa:
    def __init__(self):
        print("This is class A")
class classb(classa):
    def __init__(self):
        super().__init__()     
        print("This is class b")
ob=classb()           
