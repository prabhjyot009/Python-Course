l1 = [1, 4, 6, 2, 15]
l1.pop(2)
print(l1)  # why: 2 means 2nd index

# copy
l2 = l1.copy()
print(l2)

# shallow copy
l4 = l1[

    :]
print(l4)  # why: l4 is a copy of l1 but not a reference to l1 so if we change l1 it will not affect l4 and vice versa but if we change the elements of l1 it will affect l4 and vice versa

# index function
print(l1.index(15))  # why: 4 means 4th index

# complex list
l5 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
a = l5[2:5]

# max and min function
print(max(l1))
print(min(l1))

# count function
print(l1.count(1))
