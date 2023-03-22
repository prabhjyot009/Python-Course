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

#objective of the program is to separate positive and negative number from a list and store them in two different lists using while loop.

#algorithm

#1.	Declare a list x
#2.	Declare an empty list y
#3.	Declare an empty list z
#4.	Declare a variable i and assign it the value 0
#5.	While i is less than the length of x
#6.	If the element at index i of x is greater than 0
#7.	Append the element at index i of x to y
#8.	Else
#9.	Append the element at index i of x to z
#10.	Increment i by 1
#11.	Print y
#12.	Print z