print("Print Second max value ")
list= [40,20,30,78,23,99]
n = len(list)
max = 0
max2 = 0
for i in range(n):
    if(list[i]>max):
        max2 = max
        max = list[i]

print("The maximum value in array is : " ,max)  
print("The Second maximum value in array is : " ,max2)
