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

# Q7
# n=int(input("Enter:"))
# i=1
# sum=0
# while i<=n:
#     sum=sum+(i*i*i)
#     i=i+1
# print(sum)

#Q8
# n=int(input("Enter:"))
# i=1
# while i<=n:
#     if(i%2==0):
#         print(i)
#     i=i+1

# Q9
# n=int(input("Enter:"))
# i=1
# sum=0
# while i<=n:
#     if i%2==0:
#         sum=sum+i
#     i=i+1
# print(sum)

# Q10
# n=int(input("Enter:"))
# i=1
# sum=0
# count=0
# while count<n:
#     if i%2==0:
#         sum=sum+i
#         count=count+1
#     i=i+1
# print(sum)

#Q.sum of digits of given number:
# n=int(input("Enter:"))
# sum=0
# while n>0:
#     sum=sum+(n%10)
#     n=n//10
# print(sum)

#Q.Product of digits of given number:
# n=int(input("Enter:"))
# pro=1
# while n>0:
#     pro=pro*(n%10)
#     n=n//10
# print(pro)

#Q.Sum of even digits and Product of odd digits:
# n=int(input("Enter"))
# sum=0
# pro=1
# while n>0:
#     if(n%2==0):
#         sum=sum+(n%10)
#         n=n//10
#     else:
#         pro=pro*(n%10)
#         n=n//10
# print(sum)
# print(pro)

#Q.sum of square of given number:
# n=int(input("Enter:"))
# sum=0
# while n>0:
#     sum=sum+(n%10)*(n%10)
#     n=n//10
# print(sum)

# Q.armstrong:
# n=int(input("Enter:"))
# sum=0
# og=n
# while n>0:
#     sum=sum+(n%10)*(n%10)*(n%10)
#     n=n//10
# if og==sum:
#     print(sum,"is armstrong")
# else:
#     print(sum,"is not armstrong")

#Q. palindrome:
# n=int(input("Enter:"))
# rev=0
# temp=n
# while n>0:
#     rev=(rev*10)+n%10
#     n=n//10
# if temp==rev:
#     print("Palindrome")
# else:
#     print("Not Palindrome")
    
# Q.factors of given number
# n=int(input("Enter:"))
# i=1
# while i<=n:
#     if n%i==0:
#         print(i)
#     i=i+1
    
# Q.prime no.
# n=int(input("Enter a no:"))
# i=1
# count=0
# while i<=n:
#     if(n%i==0):
#         count+=1
#     i+=1
# if count==2:
#     print("Prime")
# else:
#     print("Composite")
    
#Q.sum of first and last digit
# print("Enter a Number: ")
# num = int(input())
# last=0
# rem=0
# count = 0
# while num!=0:
#     if count==0:
#         last = num%10
#         count = count+1
#     rem = num%10
#     num = int(num/10)
# sum = rem + last
# print("\nSum of first and last digit =", sum)

#Q. sum of first and last digit
# We have a number.
# number = 1247
 
# # Assigning last digit of the number in res
# # variable.
# res = number % 10
 
# # Now, continue a loop until
# # the number becomes less than 9.
# while number > 9:
 
#     # integer division of the number and reassigning
#     # it.
#     number = number // 10
 
# # Here, our number only contain one digit.
# # So, add this number in res variable.
# res += number
 
# # Now, display our output
# print('Addition of first and last digit of number is', res)

# n=input("Enter:")
# for x in n:
#     if x not in 'aeiouAEIOU':
#         print(x)
        
# x={1,2,3,1,2,3}
# for i in x:
#     print(i)
    
# A={1,2,3,4,5}
# B={4,5,6}
# AUB=A.union(B)
# AUB={1,2,3,4,5,6,7,8}
# print(AUB)
# #intersection
# A={1,2,3,4,5}
# B={4,5,6}
# AUB=A.intersection(B)
# AUB={4,5}
# print(AUB)

# a=[1,2,3,5,4]
# print(a[::])

#Lcm and hcf:

# num=int(input("Enter number:"))
# for i in range(1,num+1):
#     if(num%i==0):
#      print("Factor is: ", i)

#Lcm and hcf:
# num1=int(input("Enter num1:"))
# num2=int(input("Enter num2:"))
# num3=int(input("Enter num3:"))

# maxnum=max(num1,num2,num3)
# lcm=maxnum

# while True:
#     if(lcm%num1==0 and lcm%num2==0 and lcm%num3==0):
#         break;
#     else:
#         lcm+=maxnum
# print(lcm)

num1=int(input("Enter num1:"))
num2=int(input("Enter num2:"))
num3=int(input("Enter num3:"))
minnum=min(num1,num2,num3)
hcf=1

for i in range(1,minnum+1):
    if(num1%i==0 and num2%i==0 and num3%i==0):
        hcf=i
print(hcf)

