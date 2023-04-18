#write a program to create list with different type of string to generate another list such that it will have count of all the alphabet in it.

x=input("Enter the string: ")
y=list(x)
z=[]
for i in y:
    z.append(y.count(i))
print(z)

b={}
for i in range(len(y)):
    b[y[i]]=z[i]
print(b)

print(sorted(b.items()))