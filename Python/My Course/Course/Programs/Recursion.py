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

#factorial:
# def fact(n):
#     if n==1 and n==2:
#         return 1
#     else:
#         return (fact(n-1)+fact(n-2))
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
def prime(num,i): 
    if i==1:
        return 1
    if num%i==0:
        return 0
    return prime(num,i-1)
num=int(input("Enter number"))
n=prime(num,int(num/2))
if (n==1):
    print(num,"It is prime number")
else:
    print(num,"It is not a prime number")
    
