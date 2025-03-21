n = int(input("Size of list : "))

list = []
for i in range(n):
    data = input("Enter data : ")
    list.append(data)
print(list)    

# BY USING WHILE LOOP
n = int(input("Size of list : "))
list = []
i=0
while(i<n):
    data = input("Enter data : ")
    list.append(data)
    i+=1
    
print(list)   

