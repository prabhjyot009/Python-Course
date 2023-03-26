#wap to print 1 to n natural number

n=int(input("Enter the number upto which you want to print:"))
i=1
sum=0
while i<=n:
    sum=sum+i
    print(i)
    i=i+1
print("Sum is",sum)
