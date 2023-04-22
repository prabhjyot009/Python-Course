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
print("this is half pattern:")
for i in range(5): #5 is the number of rows and i is the row number and i starts from 0 and goes till 4 as 5 is not included
    for j in range(i+1):#i+1 is the number of columns. j is the column number and j starts from 0 and goes till i+1 as i+1 is not included.
        print("*",end='')#end='' is used to print in same line
    print()#this is used to print in next line
    
    