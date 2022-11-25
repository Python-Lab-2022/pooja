list=[2,5,7,9,1]
list1=[2,7,6,1,9]
print("length of list:")
print(len(list))
print("length of list1:")
print(len(list1))

if len(list)==len(list1):
    print("same length")
   
else:
    print("different length")


a=sum(list)
print("sum of list:")
print(a)
b=sum(list1)
print("sum of list1:")
print(b)
if a==b:
    print("sum is same")
else:
    print("sum is not same")

common=set(list).intersection(list1)
print(common,"common")
