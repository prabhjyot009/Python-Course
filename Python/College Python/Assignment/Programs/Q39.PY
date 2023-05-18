import numpy as np

arr1=np.array([1,2,3])
arr2=np.array([4,3,1])

lis=[]
for i in arr1:
    if i not in arr2:
        lis.append(i)
for i in arr2:
    if i not in arr1:
        lis.append(i)

arrnew=np.array(lis)
print(arrnew)
