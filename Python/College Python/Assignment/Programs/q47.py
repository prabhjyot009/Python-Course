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

#algorithm to get the 1st largest value from a NumPy array
#step1: start
#step2: import numpy as np
#step3: define a variable arr and assign np.array([2,0,1,5,4,1,9]) to it
#step4: print arr
#step5: define a variable sorted_array_index and assign np.argsort(arr) to it
#step6: define a variable sort_arr and assign arr[sorted_array_index] to it
#step7: print "Sorted Array:",sort_arr
#step8: define a variable n and assign 1 to it
#step9: define a variable result and assign sort_arr[-n:] to it
#step10: print "Largest Value:",result[0]
#step11: stop