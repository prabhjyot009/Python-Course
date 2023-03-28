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
# i=int(input("Enter Num"))
# og=i
# sum=0
# while i>0:
#     sum=sum+(i%10)*(i%10)*(i%10)
#     i=i//10
# if og==sum:
#     print("Armstrong")
# else:
#     print("Not Armstrong")
    
#product of digits:
# n = int(input("Enter Number"))
# pro = 1
# while n > 0:
#     pro = pro * (n % 10)
#     n = n // 10
# print(pro)

#sum of even digits and product of odd digits
# n = int(input("Enter number"))
# sum = 0
# pro = 1
# while n > 0:
#     if n % 2 == 0:
#         sum = sum + n % 10
#         n = n // 10
#     else:
#         pro = pro * (n % 10)
#         n = n // 10
# print("Sum of even numbers:",sum)
# print("Product of Odd numbers:",pro)

#Reverse a number
# n=int(input("Enter"))
# rev=0
# while(n>0):
#     rev=(rev*10)+n%10
#     n=n//10
# print("reverse is:",rev)

#Palindrome:
# n=int(input("Enter"))
# rev=0
# temp=n
# while(n>0):
#     rev=(rev*10)+n%10
#     n=n//10
# if rev==temp:
#     print(rev,"is Palindrome")
# else:
#     print(rev,"is Not Palindrome")

#prime or not
# n=int(input("Enter"))
# i=1
# count=0
# while(i<=n):
#     if(n%i==0):
#         count+=1
#     i+=1
# if(count==2):
#     print("Prime")
# else:
#     print("Composite")
    
#Factorial
# n=int(input("Enter: "))
# fact=1
# while(n>0):
#     fact=fact*n
#     n-=n-1
# print(fact)

# Q1
# i=1
# while i<=10:
#     print(i)
#     i=i+1

# Q2
# n=int(input("Enter number:"))
# i=1
# while i<=n:
#     print(i)
#     i=i+1

# Q3
# i=10
# while i>=1:
#     print(i)
#     i=i-1

# Q4
# n=int(input("Enter:"))
# i=1
# sum=0
# while n>=i:
#     sum=sum+i
#     i=i+1
# print(sum)

# Q5
# n=int(input("Enter:"))
# i=1
# sum=0
# while i<=n:
#     sum=sum+i
#     i=i+1
#     print(sum)

# Q6
# n=int(input("Enter:"))
# i=1
# sum=0
# while i<=n:
#     sum=sum+(i*i)
#     i=i+1
# print(sum)


    