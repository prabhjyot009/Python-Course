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
def fact(n):
    if n==1 and n==2:
        return 1
    else:
        return (fact(n-1)+fact(n-2))
n=int(input("Enter number"))
factt=fact(n)
print(factt)