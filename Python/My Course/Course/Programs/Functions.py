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


def listadd(a):
    sum=0
    for i in a:
        sum=sum+i;
    print(sum)
l=[]
size=int(input("Enter size:"))
for i in range(size):
    val=int(input("Enter values:"))
    l.append(val)
print(l)
listadd(l)
