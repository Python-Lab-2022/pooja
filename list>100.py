n=int(input("enter the limit:"))
list=[]
list1=[]
for i in range(0,n):
    list.append(int(input("enter numbers:")))
print(list)
for i in list:
    if i>100:
        list1.append("over")
    else:
        list1.append(i)
print(list1)        
