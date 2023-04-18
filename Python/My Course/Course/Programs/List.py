# a=["ram",1,"shyam",12.5]
# print(a)
# print(a[0][-1::-1]) #revrse of 1st element
# print(a[-1])
# a[1]=100
# print(a[1])



# l=[]
# a=int(input("Enter"))
# for i in range(0,a):
#     a=int(input("Enter next:"))
#     if(a%5==0 and a!=100):
#         l.append(a);
#     else:
#         break;
# print(l)

# a=[]
# size=int(input("Enter size:"))
# for i in range(size):
#     num=int(input("Enter elements"))
#     a.append(num)
# print("The elements in list are:",a)
# sum=0
# for i in range(size):
#     sum=sum+a[i]
# print(sum)
# print(max(a))

'''
a=[]
size=int(input("Enter size:"))
for i in range(size):
    num=int(input("Enter values:"))
    a.append(num)
print(a)
odd=0
even=0
for i in range(size):
    if a[i]%2==0:
        even=even+1
    else:
        odd=odd+1
print("Total number of odd nos. are:",even)
print("Total number of odd nos. are:",odd)'''

'''
a=[]
size=int(input("Enter size:"))
for i in range(size):
    num=int(input("Enter values:"))
    a.append(num)
print(a)
sum=0
pro=1
for i in range(size):
    if a[i]%2==0:
        sum=sum+a[i]
    else:
        pro=pro*a[i]
print("sum of even nos. are:",sum)
print("pro of odd nos. are:",pro)'''

a=[]
size=int(input("Enter size:"))
for i in range(size):
    num=int(input("Enter values:"))
    a.append(num)
key=int(input("Enter the elemnt you want to search:"))
flag=0
pos=0
for i in range(size):
    if a[i]==key:
        flag=1
        pos=i+1
        break;
if(flag==1):
    print("element found at position,",pos)
else:
    print("Element not found")
    
#program to count frequency of a number:
