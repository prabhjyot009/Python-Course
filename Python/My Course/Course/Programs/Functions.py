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

#Q1.create a function which takes n number of inputs from tuple and return the sum of all the elements in the list and print the list.
# def listadd(*a):
#     sum=0
#     for i in a:
#         sum=sum+i;
#     return sum
# l=[]
# size=int(input("Enter size:"))
# for i in range(size):
#     val=int(input("Enter values:"))
#     l.append(val)
# ll=
# print(listadd(*l))

#lambda functions are anoynymous functions that is fucntion eithout name these fucntionsa have only single line they can have any number of arguments
#they cannnot access global varuable and donot have explicit return statement

# sum=lambda x,y:x+y
# print(sum(10,20))

