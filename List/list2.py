print("Sort the list in ascending order ")
list = [40,20,30,14,78]
n = (len(list))
for i in range(n):
    for j in range(0,n-i-1):
        if(list[i]>list[j+1]):
            list[j],list[j+1] = list[j+1],list[j]
print(list)           

