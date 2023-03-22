#WAP to separate positive and negative number from a list and store them in two different lists using while loop.

x = [1, -2, 3, -4, 5, -6, 7, -8, 9, -10]
y = []
z = []
i = 0
while i < len(x):
    if x[i] > 0:
        y.append(x[i])
    else:
        z.append(x[i])
    i += 1
print(y)
print(z)