# 3. return with no argument
def return_noargument():
    a=10
    b=20
    c=a+b
    d = a*b
    return c,d
x = return_noargument()
add = 0
print(x)
for i in x:
    add = add + i
    print(add)

print("hlo")    

