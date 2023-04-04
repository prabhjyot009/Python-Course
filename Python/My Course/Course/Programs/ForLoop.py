# s1='PYTHON program'
# for x in s1:
#     if x not in 'aeiouAEIOU':
#      print(x)
     
# for i in range(1,11,2):
#     print(i)
    
#pattern:
# 1
# 12
# 123
# 1234
# 12345

# i=1
# while i<=5:
#     j=1
#     while j<=i:
#         print(j,end='')
#         j=j+1
#     print()
#     i=i+1
    
#same code in for loop
# for i in range(1,6):
#     for j in range(1,i+1):
#         print(j,end='')
#     print()

# program to print sum of all the no.s from 1 to 100

# sum=0
# for i in range(1,101):
#     sum=sum+i
# print(sum)

# sum=0
# for i in range(1,101):
#     if(i%2==0):
#         sum=sum+i
# print(sum)


num=int(input())

if num>1:
    for i in range(2,num):
        if num%i==0:
            print(num,"not prime")
            break
    else:
        print(num,"It is prime")
else:
    print(num,"Not prime")