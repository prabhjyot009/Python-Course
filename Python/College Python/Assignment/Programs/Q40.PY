import numpy as np
def unique(list1):
    x = np.array(list1)
    print(np.unique(x))
list1 = [10, 20, 10, 30, 40, 40]
print("the unique values from 1st list is")
unique(list1)