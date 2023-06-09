#Mean:

def mean(list):
    sum = 0
    N = len(list)
    for i in list:
        sum += i
    return sum/N

list = [1,2,3,4,5,6,7,8,9,10]
print("The value of mean is",mean(list))

#Median:

def median(list):
    list.sort()
    N = len(list)
    if N%2!=0:
        i=(N-1)//2
        return list[i]
    else:
        i1=(N-1)//2
        i2=(N)//2
        val = (list[i1]+list[i2])/2
        return val
    
list = [1,2,3,4,5]
print("The value of median is",median(list))

#Mode:

def mode(list):
    v1 = None
    c1 = 0
    
    for i in list:
        x=c1
        c1=max(list.count(i),c1)
        if x!=c1:
            v1=i
    return c1,v1

list = [4,6,8,5,3,4]
c1,v1 = mode(list)
print("The value of mode is",v1,"and it occurs",c1,"times")

#Standard Deviation:

import math
import numpy as np

def standard_deviation(list):
    mean=np.mean(list)
    sum1=0
    for i in list:
        sum2=(i-mean)**2
        sum1+=sum2
        
    ele=len(list)
    ans=sum1/(ele-1)
    ans=math.sqrt(ans)
    return ans

list = [1,2,3,4,5]
print("The value of standard deviation is",standard_deviation(list))
