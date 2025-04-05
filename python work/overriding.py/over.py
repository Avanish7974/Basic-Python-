class classA:
    def myfun(self):
        print("This is class A")
class classB(classA):
    def myfun(self):
        print("This is class B")
class classC(classB):
    def myfun(self):
        print("This is class C")

ob=classC()
ob.myfun()        

class classA:
    def myfun(self):
        print("This is class A")
class classB(classA):
    def myfun(self):
        super().myfun()     
        print("This is class B")
class classC(classB):
    def myfun(self):
        print("This is class C")

ob=classC()
ob.myfun()        