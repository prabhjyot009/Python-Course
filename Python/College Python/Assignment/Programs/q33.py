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

#algorithm
# step 1:start
# step 2:define a function unique(l)
# step 3:initialize l1=[]
# step 4:for i in l
# step 5:if i not in l1
# step 6:l1.append(i)
# step 7:return l1
# step 8:stop

#objective:
# to return a new list with unique elements of the first list.