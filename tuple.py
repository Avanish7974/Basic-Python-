# tuple
# When we wan to represent a group of individual object into an single entity where duplicate and homgeneous and hetrogeneous object is to be allowed and insertion order is to be preserved but we want immutable behaviour of the object then we will use a tuple

# Every tuple represent in all the object ellement within paranthesis with coma seperator
# tuple is immutable
ls = [1,2,3,4,'hlo']
ls.sort
print(ls)
print(type(ls))
tup1 = (1,2,3,4,5,6,7)
print(tup1)
print(type(tup1))
print(max(tup1))
ls1 = list(tup1)
print(ls1)

# tup2=tuple(ls)
# print(tup2)
# print(type(tup1))
# tup3=tuple(tup1)
# print(tup3)