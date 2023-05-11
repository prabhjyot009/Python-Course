#wap that takes a list and returns a new list with unique elements of the first list.
def unique(l):
    l1=[]
    for i in l:
        if i not in l1:
            l1.append(i)
    return l1
l=[]
size=int(input("Enter size:"))
for i in range(size):
    val=int(input("Enter values:"))
    l.append(val)
print(l)
print(unique(l))