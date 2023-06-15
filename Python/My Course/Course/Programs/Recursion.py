# def sum(n):
#     if n==1:
#         return 1;
#     else:
#         return(n+sum(n-1))
# n=int(input("Enter number"))
# summ=sum(n)
# print(summ)

# def even(n):
#     if n==1:
#         return False;
#     elif n==0:
#         return True
#     else:
#         return even(n-2)
# n=int(input("Enter number"))
# evenn=even(n)
# print(evenn)

# def xyz(S,n):
#     if n==0:
#         print(S[0])
#     else:
#         print(S[n],end='')
#         xyz (S,n-1)
# S=input("Enter String:")
# xyz(S,len(S)-1)

#factorial of a non-negative number:
# def fact(n):
#     if n==1:
#         return 1
#     else:
#         return fact(n-1)*n
# n=int(input("Enter number"))
# factt=fact(n)
# print(factt)

#First 10 natural numbers:
#direct recursion:

# def natural(n):
#     if n<=0:
#         return -1
#     else:
#         natural(n-1)
#         print(n,end=' ')
# natural(10)

#indirect recursion:

# def natural(n):
#     if n<=0:
#         return -1
#     else:
#         natural1(n-1)
#         print(n,end=' ')
# def natural1(n):
#     natural(n-1)
#     print(n,end=' ')

# natural(10)

#Print First uppercase letter in a string Using Recursion

# def first_upper(str,i):  #i is pointer
#     l=len(str)
#     if i>=l:
#         return -1
#     if str[i].isupper():
#         return str[i]
#     if i<l:
#         return first_upper(str,i+1)
# str=input("Enter length of string:")
# index=first_upper(str,0)
# print(index)

#maximum and minimum in a list:

# def largest(a,l,maximum):
#     if l==0:
#         return maximum
#     if l>0:
#         if a[l]>maximum:  #a[8](60)>a[0](1) yeyss
#             maximum=a[l]  #maximum=60
#     return largest(a,l-1,maximum)  #l=
# a=[1,2,3,4,5,90,80,70,60]
# maximum=a[0]
# l=len(a)-1
# print(largest(a,l,maximum))

# def smallest(a,l,minimum):
#     if l==0:
#         return minimum
#     if l>0:
#         if a[l]<minimum:
#             minimum=a[l]
#     return smallest(a,l-1,minimum)
# a=[5,6,7,1,9]
# minimum=a[0]
# l=len(a)-1
# print(smallest(a,l,minimum))

# class Recursion:
#     def __init__(self):
#         self.a=[1,2,3,4,5,90,80,70,60]
#         self.maximum=self.a[0]
#         self.minimum=self.a[0]
#         self.l=len(self.a)-1
#     def largest(self,l):
#         if l==0:
#             return self.maximum
#         if l>0:
#             if self.a[l]>self.maximum:
#                 self.maximum=self.a[l]
#         return self.largest(l-1)
#     def smallest(self,l):
#         if l==0:
#             return self.minimum
#         if l>0:
#             if self.a[l]<self.minimum:
#                 self.minimum=self.a[l]
#         return self.smallest(l-1)
    
# obj=Recursion()
# print(obj.largest(obj.l))
# print(obj.smallest(obj.l))


#factorial of a number:

# def fact(n):
#     if n==1:
#         return 1
#     else:
#         return fact(n-1)*n
# print(fact(5))


#prime number using recursion:
# def prime(num,i): 
#     if i==1:
#         return 1
#     if num%i==0:
#         return 0
#     return prime(num,i-1)
# num=int(input("Enter number"))
# n=prime(num,int(num/2))
# if (n==1):
#     print(num,"It is prime number")
# else:
#     print(num,"It is not a prime number")
    
#sum of digits:
# def sum(n):
#     if n<10:
#         return n
#     else:
#         return (n%10)+sum(int(n/10))
# n=int(input("Enter number:"))
# print(sum(n))

#power of number
# def power(a,b):
#     if b==1:
#         return a
#     else:
#         return a*power(a,b-1)
# a=int(input("Enter number"))
# b=int(input("Enter power"))
# print("Output:",power(a,b))

#count number of digits:
# def count(n):
#     if n<10:
#         return 1
#     else:
#         return 1+count(int(n/10))
# n=int(input())
# print("Count is:",count(n))

#natural number between range:
# def natural(a,b):
#     if a>b:
#         return -1
#     else:
#         print(a," ",end=' ')
#         return natural(a+1,b)# in reverse a-1
# a=int(input("ENter num 1:"))
# b=int(input("Enter 2 num:"))
# natural(a,b)

#armstrong:
# def arm(n):
#     if n<10:
#         return n*n*n
#     else:
#         return (n%10)*(n%10)*(n%10)+arm(int(n/10))
# n=int(input("Enter number:"))
# r=arm(n)
# if r==n:
#     print(n,"is armstrong")
# else:
#     print(n,"not a armstrong")

#palindrome:
# def palin(n,t):
#     if n==0:
#         return t
#     else:
#         t=(t*10)+(n%10)
#         return palin(int(n/10),t)
# n=int(input("Enter number:"))
# t=0
# p=palin(n,t)
# if n==p:
#     print(n,"It is palindrome number")
# else:
#     print(n,"It is not palindrome")

#even number between given range:

# def even(a,b):
#     if a>b:
#         return -1
#     else:
#         print(a)
#         return even(a+2,b)
# a=int(input("ENter num 1:"))
# b=int(input("Enter 2 num:"))
# if a%2==0:
#     a=a
# else:
#     a+=1
# even(a,b)
