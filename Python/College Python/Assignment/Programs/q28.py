#wap to find a largest string in a list and display its index value and convert the string into uppercase store all thge characters into tuple using for loop and without using function and take input from user.

a = []
n = int(input("Enter the number of elements in list: "))
for i in range(n):
    a.append(input("Enter the element: "))
print("The list is: ",a)
max = a[0]
for i in a:
    if len(i) > len(max):
        max = i
print("The largest string is: ",max)
print("The index of largest string is: ",a.index(max))
print("The string in uppercase is: ",max.upper())
t = tuple(max)
print("The tuple is: ",t)
#without using upper() function