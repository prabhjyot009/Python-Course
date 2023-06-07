#.	Write a python program to count the frequency of unique values in numpy array.

import numpy as np

arr=np.array([1,2,3,4,4,5])
print(arr)
print(np.unique(arr,return_counts=True))