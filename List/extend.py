
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