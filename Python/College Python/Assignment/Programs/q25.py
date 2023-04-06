#wap to take string as a input store all the character in the string into a list with one chracter ahead of it.
n=input("Enter the string:")
l=[]
for i in n:
    l.append(i)
print("The list is:",l)
for i in range(len(l)):
    print(l[i],end="")
    print(l[i],end="")