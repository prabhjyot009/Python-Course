a=[]
size=int(input("ENter size:"))
for i in range(size):
    num=int(input("ENter number:"))
    a.append(num)
print(a)
count=0
for i in range(size):
    if a[i]%2!=0 or a[i]==2:
        count=count+1
        print("Prime")
    else:
        print("Not prime")
print(count)