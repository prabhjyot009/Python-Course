# def oddeven(a):
#     if a%2==0:
#         print(a,"even");
#     else:
#         print(a,"odd");
#     return a
# a=int(input("Enter number:"))
# x=oddeven(a)


# def reverse(i):
#     rev=0;
#     while i>0:
#         rev=(rev*10)+i%10
#         i=i//10
#     print(rev)
#     return rev
# i=int(input("Enter number:"))
# x=reverse(i)

# def listadd(a):
#     sum=0
#     for i in a:
#         sum=sum+i;
#     print(sum)
# # l=[]
# # size=int(input("Enter size:"))
# # for i in range(size):
# #     val=int(input("Enter values:"))
# #     l.append(val)
# # print(l)
# a=int(input("Enter elemnt to add:"))
# listadd(a)


# def listadd(a):
#     sum=0
#     for i in a:
#         sum=sum+i;
#     print(sum)
# l=[]
# size=int(input("Enter size:"))
# for i in range(size):
#     val=int(input("Enter values:"))
#     l.append(val)
#
# print(l)
# listadd(l)

# def calc(a,b):
#     global z
#     z=a+b
#     return z
# print(calc(10,20))
# z="hello"
# print(z)

# def disp(int_x,str):
#     print(int_x)
#     print(str)
# disp(int_x=5,str="hello")
# disp(str="hello",int_x=5)

# def calc(a,b=10,c=10):
#     global z
#     z=a+b+c
#     return z
# print(calc(10,20,10))
# z="hello"
# print(z)

# Q1.create a function which takes n number of inputs from tuple and return the sum of all the elements in the list and print the list.
def listadd(*a):
    sum=0
    for i in a:
        sum=sum+i;
    return sum
l=[1,2,3,4]
# size=int(input("Enter size:"))
# for i in range(size):
#     val=int(input("Enter values:"))
#     l.append(val)
# ll=
print(listadd(*l))

# lambda functions are anoynymous functions that is fucntion eithout name these fucntionsa have only single line they can have any number of arguments
# they cannnot access global varuable and donot have explicit return statement

# sum=lambda x,y:x+y
# print(sum(10,20))

# No argument with No return:

# def add():
#     a=10
#     b=20
#     c=a+b
#     print("Addition is",c)
# add()

# def add():
#     a=int(input("Enter a:"))
#     b=int(input("Enter b:"))
#     c=a+b
#     print(c)
# add()

# Argument with no return:

# def add(a,b):
#     c=a+b
#     print(c)
# a=int(input("ENter a:"))
# b=int(input("ENter b:"))
# add(a,b)

# No argument with return:

# def add():
#     a=int(input("Enter a:"))
#     b=int(input("Enter b:"))
#     c=a+b
#     return c
# sum=add()
# print(sum)

# argument with return:

# def add(a,b):
#     c=a+b
#     return c
# a=int(input("Enter a:"))
# b=int(input("Enter b:"))
# sum=add(a,b)
# print(sum)

# questions:

# maximum of 3 numbers in a list:

# def max(a,b,c):
#     if a>b and a>c:
#         print("A is greater")
#     elif b>a and b>c:
#         print("B is greater")
#     else:
#         print("C is greater")
# a=int(input("Enter a:"))
# b=int(input("Enter b:"))
# c=int(input("Enter c:"))
# output=max(a,b,c)

# 2. Write a Python function to sum all the numbers in a list.
# Sample List : (8, 2, 3, 0, 7)
# Expected Output : 20

# def sumlist(l):
#     sum = 0
#     for i in l:
#         sum = sum+i
#     return sum


# l = [8, 2, 3, 0, 7]
# s = sumlist(l)
# print(s)

# 4. Write a Python program to reverse a string.
# Sample String : "1234abcd"
# Expected Output : "dcba4321"

# def s(string):
#     rev=None
#     for i in range(len(string)):
#         rev=string[::-1]
#     print(rev)
#     return rev
# string=input("Enter string:")
# call=s(string)

#check if palindrome or not:
# def s(string):
#     rev=None
#     for i in range(len(string)):
#         rev=string[::-1]
#     print(rev)
#     return rev
# string=input("Enter string:")
# call=s(string)
# if string==call:
#     print("Palindrome")
# else:
#     print("Not palindrome")
    
# 5. Write a Python function to calculate the 
# factorial of a number (a non-negative integer).
# The function accepts the number as an argument.
# Click me to see the sample solution

# def factorial(a):
#     fact=1
#     while a>0:
#         fact=fact*(a%10)
#         a=a//10
#     print(fact)
# a=int(input("ENter number"))
# f=factorial(a)

# 6. Write a Python function to check whether a number falls within a given range.

# def rangee(n):
#     if n in range(3,9):
#         print("yesss")
#     else:
#         print("NOOOO")
#     return n
# n=8
# call=rangee(n)

# 7. Write a Python function that accepts a 
# string and counts the number of upper and
# lower case letters.
# Sample String : 'The quick Brow Fox'
# Expected Output :
# No. of Upper case characters : 3
# No. of Lower case Characters : 12

# def string(s):
#     countupper=0
#     countlower=0
#     for i in s:
#         if i.isupper():
#             countupper+=1
#         elif i.islower():
#             countlower+=1
#         else:
#             pass
#     print("Orignal:",s)
#     print("No of uppercase:",countupper)
#     print("No of lowercase:",countlower)
# s=input("ENter string:")
# call=string(s)

# 8. Write a Python function that takes a 
# list and returns a new list with distinct 
# elements from the first list.
# Sample List : [1,2,3,3,3,3,4,5]
# Unique List : [1, 2, 3, 4, 5]

# def samplelist(l):
#     uniquelist=[]
#     for i in l:
#         if i not in uniquelist:
#             uniquelist.append(i)
#     print("Unique List",uniquelist)
#     return uniquelist
# l=[]
# size=int(input("Enter size:"))
# for i in range(size):
#     val=int(input("ENter elements:"))
#     l.append(val)
# print("Orignal List",l)
# call=samplelist(l)

# 9. Write a Python function that takes a number 
# as a parameter and checks whether the number is
# prime or not.

# def prime(n):
#     if n==1:
#         return False
#     elif n==2:
#         return True
#     else:
#         for i in range(2,n):
#             if n%i==0:
#                 return False
#         return True
# n=int(input("Enter number:"))
# call=prime(n)
# print(call)

# 10. Write a Python program to print the even 
# numbers from a given list.
# Sample List : [1, 2, 3, 4, 5, 6, 7, 8, 9]
# Expected Result : [2, 4, 6, 8]

# def even(l):
#     x=[]
#     for i in l:
#         if i%2==0:
#             x.append(i)
#         else:
#             pass
#     return x
# print(even([1,2,3,4,5,6]))


#function inside function
# def test(a):
#     def add(b):
#         nonlocal a
#         a+=1
#         return a+b
#     return add
# func=test(4)
# print(func(4))

#local variable:
# def abc():
#     x=1
#     y=2
#     str1='hello'
#     z=4
#     print("yo")
# print(abc.__code__.co_nlocals)

