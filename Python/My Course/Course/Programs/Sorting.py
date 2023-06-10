#Selection Sorting:
x=[1,4,2,9,6,5,4,0]
for i in range(0,len(x)-1):
    for j in range(i+1,len(x)):
        if x[i]>x[j]:
            c=x[i]
            x[i]=x[j]
            x[j]=c
print(x)

#Bubble Sorting:
for i in range(0,len(x)):
    for j in range(0,len(x)-1):
        if x[j]>x[j+1]:
            c=x[j]
            x[j]=x[j+1]
            x[j+1]=c
print(x)

#Insertion Sorting:
for i in range(1,len(x)):
    c=i
    while c>0 and x[c]<x[c-1]:
        a=x[c]
        x[c]=x[c-1]
        x[c-1]=a
        c-=1
print(x)