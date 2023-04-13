#wap to take numbers as input from the user generate character with respect to the number and convert it into a string using for loop and without using function.
a = []
n = int(input("Enter the number of elements in list: "))
for i in range(n):
    a.append(int(input("Enter the element: ")))
print("The list is: ",a)
s = ""
for i in a:
    s =s+ chr(i)
print("The string is: ",s)

