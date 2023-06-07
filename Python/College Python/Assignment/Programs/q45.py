#.	Write a python program to count the frequency of unique values in numpy array.

import numpy as np

arr=np.array([1,2,3,4,4,5])
print(arr)
print(np.unique(arr,return_counts=True))

#algorithm to count the frequency of unique values in numpy array.
#step1: start
#step2: import numpy as np
#step3: define a variable arr and assign np.array([1,2,3,4,4,5]) to it
#step4: print arr
#step5: print np.unique(arr,return_counts=True)
#step6: stop