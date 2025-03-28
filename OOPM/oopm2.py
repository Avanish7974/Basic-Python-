class myclass:
    def display():
        print("Mtehodes of an class")
obj = myclass
obj.display()

class myclass:
    def display(abc):
        print("Mtehodes python of an class")
obj = myclass()
obj.display()

# wapp to create a class in which there are four methods inside the class 
# and these four methods of all four different user define data type

class myclass:
    def display():
        a = int(input("Enter 1 numb :"))
        b = int(input("enter 2 num : "))
        c = a+b
        print("Addition is : ",c)
    def noreturn_withargument(n):
        for i in range(1,n+1,1):
          for j in range(1,i+1,1):
            print(i,end=" ")
          print()
obj = myclass
obj.display()
obj.noreturn_withargument(5)
