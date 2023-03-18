'''
12345
12345
12345
12345
12345
'''

# i = 1
# while i <= 5:
#     j = 1
#     while j <= 5:
#         print(j, end='')
#         j = j+1
#     print()
#     i = i+1

'''
1
12
123
1234
12345
'''
# i=1
# while i<=5:
#     j=1
#     while j<=i:
#         print('*',end='')
#         j=j+1
#     print(  )
#     i=i+1

'''
1 
2 3 
4 5 6 
7 8 9 10 
11 12 13 14 15 
16 17 18 19 20 21 

'''
n=int(input("Enter num:"))
i = 1
k=1
while i <= n:
    j = 1
    while j <= i:
        print(k, end=' ')
        j = j+1
        k+=1
    print()
    i = i+1

