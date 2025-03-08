# program to print fibonaci series
n = int(input("Enter the number : "))
x = 0
y = 1
z = 0
while(z<=5):
    print("The fibonaci series is : ")
    print(z)
    x=y
    y=z
    z=x+y
