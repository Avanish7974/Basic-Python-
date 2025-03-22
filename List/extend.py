list= [40,20,30,78,23,99]
list.extend([1,2,3,4])
print(list)
ret1 = list.pop()
print(list)
print(ret1)
# Pop remove the last element and also return
# but remove only remove given element not return
ret2 = list.remove(99)
print(list)
print(ret2)
# removes the element
ret3 = list.count(2)
print(list)
print(ret3)
# count how many time element comes
ret4 = list.index(1)
print(list)
print(ret4)
# prints the index position of element
list.insert(1,"hello")
print(list)
# insert elemnt at specific index
list.remove("hello")
print(list)
list.sort()
print(list)
# sort the list in ascending order
list.reverse()
print(list)


