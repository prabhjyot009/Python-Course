#wap to take strings as input in a list create a string with space seprated values from the list.

n=int(input("Enter the number of elements:"))
l=[]
for i in range(n):
    l.append(input("Enter element:"))
print("The list is:",l)
s=""
for i in l:
    s=s+i+" "
print("The string is:",s)
