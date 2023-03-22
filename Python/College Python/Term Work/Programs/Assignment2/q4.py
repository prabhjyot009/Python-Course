#Write a program that appends the square of each number to a new list using while loop.

x = [1, 2, 3, 4, 5]
y = []
i = 0
while i < len(x):
    y.append(x[i] ** 2)
    i += 1
print(y)
