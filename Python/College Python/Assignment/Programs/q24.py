# wap to find the indexes of all number in a given list below given threshold.

n=int(input("Enter the number of elements:"))
l=[]
for i in range(n):
    l.append(int(input("Enter element:")))
print("The list is:",l)
t=int(input("Enter the threshold:"))
for i in l:
    if i<t:
        print("The index of",i,"is:",l.index(i))