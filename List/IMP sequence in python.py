# Sequence in Python
# # LIST
# 1. LIST - When We Want To Represent A group Of Individual Entity In a Single Entity Then We Use List 
# 2. In list we can store a hitrogeneous as well as homogeneous types of data
# 3. List are muttable(changes are allowed)

# 4. Representation of list mylist = [1,2,34,5,'A','B','C','D']
# 5.  In list position are specified which is known as Index,from start to end of an list 0,1,2,3 and so   on and from end to start from -1,-2,-3 and so on 
# List is a type of data
list = [10,20,30,4.44,1,129,'a','b']
print(list)
print(len(list))
print(type(list))

x = list[0]
print(x)
# start : stop : step
y = list[0:8:2]
print(y)

# find the sum of all the element present in a list which is number usin for loop
list = [10,20,30,44,1]
ans = 0
n = (len(list))
for i in range(n):
    ans = ans + list[i]
print(ans)    
for i in list:
    print(i)
print(max(list))
print(min(list)) 
print(sum(list))
# find the second largest from list without using any inbuilt method of a list 
# find the ascending and descenning of list   

