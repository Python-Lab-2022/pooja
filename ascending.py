n=int(input("enter the limit:"))
a=()
for i in range(0,n):
    a.append(int(input("enter the numbers:")))
for i in a:
    if i<(i+1):
        a.append(i)
print(a)

