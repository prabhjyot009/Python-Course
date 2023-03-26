#wap to print 1 to n natural number

# n=int(input("Enter the number upto which you want to print sum of even:"))
# i=1
# sum=0
# count=0
# while(count<n):
#     if i%2==0:
#         sum=sum+i
#         count=count+1
#         print(i)
#     i=i+1
# print(sum)

#sum of square digits of a given number:

# i=int(input("Enter number"))
# sum=0
# while i>0:
#     sum=sum+(i%10)*(i%10)*(i%10)
#     i=i//10
# print(sum)

#armstrong number:
i=int(input("Enter Num"))
og=i
sum=0
while i>0:
    sum=sum+(i%10)*(i%10)*(i%10)
    i=i//10
if og==sum:
    print("Armstrong")
else:
    print("Not Armstrong")
