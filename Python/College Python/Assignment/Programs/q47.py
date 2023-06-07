#3.	Write a python program to get the 1st largest value from a NumPy array

import numpy as np
arr=np.array([2,0,1,5,4,1,9])
print(arr)
#sorting the array:
sorted_array_index=np.argsort(arr)
sort_arr=arr[sorted_array_index]
print("Sorted Array:",sort_arr)

n=1
result=sort_arr[-n:]
print("Largest Value:",result[0])