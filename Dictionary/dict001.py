
d = {
    "key1":"Hello How Are",
    "key2":"i am fine",
    "key3":"What about you"
}
print(type(d))
print(d)
print(d["key1"])
print(d.keys())
print(d.values())
print(d.popitem())
print(d)
print(len(d))

d1 = {
    1:"Hello How Are",
    2:"i am fine",
    3:"What about you",

}
print(d1)
print(d1.keys())
x = d1.pop(1)
print(x)
print(d1)
# d1.clear()
# to update
print(d1)
d1[2] = "Radheshyam"   
print(d1)
# to add
d1[200] = "Radhe"   
print(d1)