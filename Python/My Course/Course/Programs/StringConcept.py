# name="Singh"
# for i in name:
#     print(i,end='')#i zero se lehke name ke last index tak chalega 0 se lehke 4 tak.

    
# #replication operator *:
# name ="Singh"
# print(2*name)

# print(3*"singh")

# #membership operator
# name="Singh"
# print("S" in name) #will give ouput true

# #String Slicing: Syntax: string[start:end]

# name="Singh"
# print(name[1:-1])  #-1 se last karna hai

# name="Singhs"
# print(name[1:5])  #4 tak karna hai

# name="Singh Brar"
# print(name[6:],name[:5])

# name="Hello World"
# print(name[3:-2])


# #Length function:
# name="singh"
# print(len(name))

# name=input("Enter your name:")
# print(len(name))

# name=input("Enter")
# for i in range(0,len(name)):
#     print(i,end="")

#Reverse of a String

# name=input("Enter:")
# print(name[-1::-1])

#for loop:

# a=input("Enter:")
# for i in range((len(a)-1)-1,-1): #range(start,stop,step)
#      print(a[i],end='')

#vovel count and consonant count:

# a=input("Enter:")
# vovel=0;
# constant=0;
# for i in range(0,len(a)):
#     if a[i]!='':
#         if a[i]=='a' or a[i]=='e' or a[i]=='i' or a[i]=='o' or a[i]=='u' or a[i]=='A' or a[i]=='E' or a[i]=='I' or a[i]=='O' or a[i]=='U':
#             vovel+=1
#         else:
#             constant+=1
# print("Total Vovels:",vovel)
# print("Total Constants:",constant)

#capitalize function:
# a="ram ji"
# print(a.capitalize())

# #find function:
# a="hello Sir"
# b="lo"
# print(a.find(b,0,len(a))) 

#palindrome string using slicing:
# a=input("Enter:")
# b=a[-1::-1] #sis: -3-2-1:index (-1:s se -1 i -1 s)
# if b==a:
#     print("Palindrome")
# else:
#     print("Not palindrome")
    
# a=input("Enter:")
# b=a
# for i in range(-1,0):
#     if b==a:
#         print("Palindrome")
        
#isalnum function:
n="sir12"
print(n.isalnum())

#isdigit() function:
n="123";
print(n.isdigit())

