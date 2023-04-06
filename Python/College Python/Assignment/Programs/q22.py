#wap as , seprated value as input and store the input in list and tuple using for loop.

n=input("Enter values:")
l=[]
t=()
for i in n:
    l.append(i)
    t=tuple(l)
print("The list is:",l)
print("The tuple is:",t)