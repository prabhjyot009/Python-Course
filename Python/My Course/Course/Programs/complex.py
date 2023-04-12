#count frequency in list using count function and append function and for loop
l1 = [ 1,4, 6,2,1,2]
l2 = []
for i in l1:
    if i not in l2:
        l2.append(i)
print(l2)

for i in l2:
    print(i,"occurs",l1.count(i),"times")