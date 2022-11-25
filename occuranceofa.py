list=[]
c=0
n=int(input("enter the number of names:"))
for i in range(0,n):
    list.append(str(input()))
for i in list:
    for j in i:
        if j=="a":
            c=c+1
print(c)
