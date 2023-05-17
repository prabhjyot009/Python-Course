import numpy as np
array =np.array([[1,2,3],[4,5,6]])

print("Array is of type:",type(array))
print("Number of dimensions:",array.ndim)
print("Shape of array:",array.shape)
print("Size of array:",array.size)
print("DataType value of an array",array.dtype)

arr=np.array([[1,2,3],[4,5,6]],dtype='float')
print(arr)

b=np.array((1,2,3))
print(b)

c=np.zeros((3,4))
print(c)

f=np.arange(0,30,5)
print(f)

g=np.linspace(0,5,10)
print(g)

#add two arrays
x=np.array([1,2,3])
y=np.array([4,5,6])
z=x+y
print(z)

#subtract two arrays
x=np.array([1,2,3])
y=np.array([4,5,6])
z=x-y
print(z)

#multiply two arrays
x=np.array([1,2,3])
y=np.array([4,5,6])
z=x*y
print(z)

#multiply matrix
x=np.array([[1,2,3],[4,5,6]])
y=np.array([[1,2,3],[4,5,6]])
z=x*y
print(z)