dict={}
string=input("enter the string:")
for n in str1:
    if n in dict:
        dict[n]+=1
    else:
        dict[n]=1
print("character frequency")
for k,v in dict.items():
    print(k,v)
