#wap to count frequency of every element in a list.

n=int(input("Enter the number of elements:"))
l=[]
for i in range(n):
    l.append(input("Enter element:"))
print("The list is:",l)
for i in l:
    print("The frequency of",i,"is:",l.count(i))