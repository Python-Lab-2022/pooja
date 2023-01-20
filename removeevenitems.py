evenList=[]
ListNumber=int(input("Enter the total list items="))
for i in range(1,ListNumber+1):
    ListValue=int(input("Enter the %d list items=" %i))
    evenList.append(ListValue)
print("List items=",evenList)
evenList=[ev for ev in evenList if ev %2!=0]
print("List items after removing even items=",evenList)
