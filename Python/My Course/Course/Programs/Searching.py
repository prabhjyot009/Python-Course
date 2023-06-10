#Linear Search:

# x=[1,2,3,4,5]
# n=int(input("Enter Number to search"))
# flag=-1
# for i in range(0,len(x)):
#     if n==x[i]:
#         flag=i
#         break
# if flag==-1:
#     print("Number not found")
# else:
#     print("Number found at index",flag,"Position",flag+1)
    
# binary search
# y=[1,2,3,4,5,6,7,8,13,14,15,9,10,11,12]
#insertion sorting:
def sort():
    for i in range(1,len(y)):
        c=i
        while c>0 and y[c]<y[c-1]:
            a=y[c]
            y[c]=y[c-1]
            y[c-1]=a
            c-=1
    print(y)
    n= int(input("Enter element to search:"))
    first=0
    last=len(y)-1
    while first<=last:
        mid=(first+last)//2
        if y[mid]==n:
            print("Number found at Index",mid,"At Position",mid+1)
            break
        elif y[mid]>n:
            last=mid-1
        else:
            first=mid+1
        if first>last:
            print("Number not avialable")
y=[]
size=int(input("Enter Size:"))
for i in range(size):
    val=int(input("Enter elements"))
    y.append(val)
call=sort()