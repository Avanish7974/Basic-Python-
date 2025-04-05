class classA:
    def myfun(self):
        print("This is class A")
class classB:
    def myfun(self):
        print("This is class B")
class classC:
    def myfun(self):
        print("This is class C")
class classD:
    def myfun(self):
        print("This is class D")   
                             
def f(obj):
    obj.myfun()
obj1=classD()
f(obj1)
l = [classA(),classB(),classC(),classD()]
for i in l:
    print(i) #this return address
    f(i)     #this value
