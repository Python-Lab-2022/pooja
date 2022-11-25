list=[]
n=int(input("enter the limit:"))
for i in range(0,n):
    list.append(int(input("enter numbers:")))
print(list)
sum=0
for i in list:
    sum=sum+i
print(sum)    
