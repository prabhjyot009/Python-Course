#Write a program that appends the square of each number to a new list using while loop.

x = [1, 2, 3, 4, 5]
y = []
i = 0
while i < len(x):
    y.append(x[i] ** 2)
    i += 1
print(y)


#objective of the program is to append the square of each number to a new list using while loop.

#algorithm

#1.	Declare a list x
#2.	Declare an empty list y
#3.	Declare a variable i and assign it the value 0
#4.	While i is less than the length of x
#5.	Append the square of the element at index i of x to y
#6.	Increment i by 1
#7.	Print y