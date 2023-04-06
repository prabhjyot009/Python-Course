#wap to find all the indexes of all the string in a list whose length is a multiple of 5.

n=int(input("Enter the number of elements:"))
l=[]
for i in range(n):
    l.append(input("Enter element:"))
print("The list is:",l)
for i in l:
    if len(i)%5==0:
        print("The index of",i,"is:",l.index(i))





