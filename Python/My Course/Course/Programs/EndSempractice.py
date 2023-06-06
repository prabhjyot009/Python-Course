size=int(input("Enter Size:"))
arr=[]
for i in range(size):
    arr.append(input())
print("Enter an element to search")
element=[]
chk=0
for i in range(size):
    if element==arr[i]:
        index=i
        chk=1
if chk==1:
    print("Element found at index",str(index))
else:
    print("Not found")