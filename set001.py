# set
# whenever we want to reprsent group of individual object as an single entity where duplicate object is not to be allowed and insertion order is not preserved then we can use a set 

# every set reprsenting all the object element within {} with , seperator.
# set is muttable
set1 = {1,2,3,4,4,4}
print(type(set1))
print(max(set1))
print(min(set1))
print(set1)
# print(set*3)
ls=list(set1)
print(type(ls))
tup = set(ls)
print(type(tup))
print(ls)
ls.remove(4)
print(ls)
set1.add("Add on")
print(set1)


s = {1,2,34,5}
fs=frozenset(s)

fs.add(7)  //it gives error
print(s)