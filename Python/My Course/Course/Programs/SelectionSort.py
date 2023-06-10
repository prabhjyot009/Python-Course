x=[1,4,2,9,6,5,4,0]
for i in range(0,len(x)-1):
    for j in range(i+1,len(x)):
        if x[i]>x[j]:
            c=x[i]
            x[i]=x[j]
            x[j]=c
print(x)