# #print patterns:
# # *
# # **
# # ***
# # ****
# # *****

# i=1
# while(i<=5):
#     j=1
#     while(j<=i):
#         print("*",end='')
#         j=j+1
#     print()
#     i=i+1
    
# # 1
# # 22
# # 333
# # 4444
# # 55555

# i=1
# while i<=5:
#     j=1
#     while(j<=i):
#         print(j,end='')
#         j=j+1
#     print()
#     i=i+1
    
# #Reverse order
# #     *
# #    **
# #   ***
# #  ****
# # *****

# i=1
# while i<=5:
#     b=1
#     while b<=5-i:
#         print(" ",end='')
#         b=b+1
#     j=1
#     while j<=i:
#         print("*",end='')
#         j=j+1
#     print()
#     i=i+1
    
# #reverse in numbers:

# i=1
# while i<=5:
#     b=1
#     while b<=5-i:
#         print(" ",end='')
#         b=b+1
#     j=1
#     while j<=i:
#         print(i,end='')
#         j=j+1
#     print()
#     i=i+1
    
# #Pyramid
# #     *
# #    ***
# #   ****
# #  ******
# # ********
# i=1
# k=1
# while i<=5:
#     b=1
#     while b<=5-i:
#         print(" ",end='')
#         b=b+1
#     j=1
#     while j<=k:
#         print("*",end='')
#         j=j+1
#     k=k+2
#     print()
#     i=i+1
    
# #Pyramid numbers:
# i=1
# k=1
# while i<=5:
#     b=1
#     while b<=5-i:
#         print(" ",end='')
#         b=b+1
#     j=1
#     while j<=k:
#         print(k,end='')
#         j=j+1
#     k=k+2
#     print()
#     i=i+1

#Reverse Pyramid:
# n=int(input("Enter number of rows:"))
# i=1
# while n>0:
#     b=1
#     while b<i:
#         print(" ",end='')
#         b=b+1
#     j=1
#     while j<=(n*2)-1:
#         print("*",end='')
#         j=j+1
#     print()
#     n=n-1
#     i=i+1


#patterns using for loop:
#increasing triangle:
#*
#**
#***
#****
#*****

print("Increasing triangle")

n=5
for i in range(n):
    for j in range(i+1):
        print("*",end=' ')
    print()
    
#decreasing triangle:
#*****
#****
#***
#**
#*
print("Decreasing triangle")

n=5
for i in range(n):
    for j in range(i,n):
        print("*",end=' ')
    print()
    
#Right sided triangle:
#     *
#    **
#   ***
#  ****
# *****

#1.decreasing pattern of space
#2.increasing pattern of stars

print("Right sided triangle")
n=5
for i in range(n):
    for j in range(i,n):
        print(" ",end=' ')
    for j in range(i+1):
        print("*",end=' ')
    print()
    
#Left side triangle:

# *****
#  ****
#   ***
#    **
#     *

#1.Increasing triangle of space
#2.Decreasing triangle of stars

print("Left sided triangle")
n=5
for i in range(n):
    for j in range(i+1):
        print(" ",end=' ')
    for j in range(i,n):
        print("*",end=' ')
    print()
    
#Hill pattern:

#     *
#    ***
#   *****
#  *******
# *********

#1.decreasing space
#2.increasing stars
#3.increasing stars

print("Hill Pattern")
n=5;
for i in range(n):
    for j in range(i,n):
        print(" ",end=' ')
    for j in range(i): #we will remove 1 coloumn(i+1)not like this
        print("*",end=' ')
    for j in range(i+1):
        print("*",end=' ')
    print()
    
#Reverse Hill Pattern:

#1.increasing space
#2.decreasing stars
#3.decreasing stars

print("Reverse Hill Pattern")
n=5;
for i in range(n):
    for j in range(i+1):
        print(" ",end=' ')
    for j in range(i,n-1): #we will remove 1 coloumn(n-1)not like this
        print("*",end=' ')
    for j in range(i,n):
        print("*",end=' ')
    print()
    
#diamond:
print("Diamond Pattern")
n=5;
for i in range(n-1):#we will reemove n to n-1 to reduce 1 row
    for j in range(i,n):
        print(" ",end=' ')
    for j in range(i): 
        print("*",end=' ')
    for j in range(i+1):
        print("*",end=' ')
    print()
for i in range(n):
    for j in range(i+1):
        print(" ",end=' ')
    for j in range(i,n-1):
        print("*",end=' ')
    for j in range(i,n):
        print("*",end=' ')
    print()
    
#Right downward triangle:

#1.decreasing star
#2.increasing space:

n=5
for i in range(n):
    for j in range(i,n):
        print("*",end=' ')
    for i in range(i+1):
        print(" ",end=' ')
    print()
    
#left downward triangle:
#2.increasing space
#1.decreasing star

n=5
for i in range(n):
    for j in range(i+1):
        print(" ",end=' ')
    for i in range(i,n):
        print("*",end=' ')
    print()
    
#number program:

print("Diamond number")
n=5;
p=1
for i in range(n-1):#we will reemove n to n-1 to reduce 1 row
    for j in range(i,n):
        print(" ",end=' ')
    for j in range(i): 
        print(p,end=' ')
    for j in range(i+1):
        print(p,end=' ')
    p+=1
    print()
for i in range(n):
    for j in range(i+1):
        print(" ",end=' ')
    for j in range(i,n-1):
        print(p,end=' ')
    for j in range(i,n):
        print(p,end=' ')
    p+=1
    print()

print("Diamond number") 
n=5;
p=1
for i in range(n-1):#we will reemove n to n-1 to reduce 1 row
    for j in range(i,n):
        print(" ",end=' ')
    for j in range(i): 
        print(p,end=' ')
    for j in range(i+1):
        print(p,end=' ')
    p+=1
    print()
for i in range(n):
    for j in range(i+1):
        print(" ",end=' ')
    for j in range(i,n-1):
        print(p,end=' ')
    for j in range(i,n):
        print(p,end=' ')
    p-=1
    print()
    
    
