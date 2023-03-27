#print patterns:
# *
# **
# ***
# ****
# *****

# i=1
# while(i<=5):
#     j=1
#     while(j<=i):
#         print("*",end='')
#         j=j+1
#     print()
#     i=i+1
    
# 1
# 22
# 333
# 4444
# 55555

# i=1
# while i<=5:
#     j=1
#     while(j<=i):
#         print(j,end='')
#         j=j+1
#     print()
#     i=i+1
    
#Reverse order
#     *
#    **
#   ***
#  ****
# *****

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
    
#reverse in numbers:

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
    
#Pyramid
#     *
#    ***
#   ****
#  ******
# ********
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
    
#Pyramid numbers:
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
n=int(input("Enter number of rows:"))
i=1
while n>0:
    b=1
    while b<i:
        print(" ",end='')
        b=b+1
    j=1
    while j<=(n*2)-1:
        print("*",end='')
        j=j+1
    print()
    n=n-1
    i=i+1