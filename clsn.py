a={
    "name":"linu",
    "class":"mca",
    "sem":"s1",
    "color":"red"
}
print(type(a))
print (a)
x=a["class"]
print(x)
for x in a:
    print(x)
for x in a:
    print(a[x])
for x,y in a.items():
    print(x,y)
for x in a.values():
    print(x)
for x,y in a.items():
    print(x,y)
    
a["color"]="red"
print (a)
a.pop("class")
print(a)    
