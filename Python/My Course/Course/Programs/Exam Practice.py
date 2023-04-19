#even odd
# num=int(input("ENter number:"))
# for i in range(2,num+1):
#     if(num%i==0):
#         print("Even")
#         break;
#     else:
#         print("Odd")
#         break;
    
# # in list:
# a=[]
# size=int(input("ENter size:"))
# for i in range(size):
#     num=int(input("ENter number:"))
#     a.append(num)
#     a.sort()
# print(a)
# even=int(input("Enter frequency you want to count:"))
# for i in range(size):
#     if(a[i]%2==0):
#         print("Even")
#         f=a.count(even)
#         print(f)
#         break;
#     else:
#         print("odd")
#         break;

#prime or not
# a=[]
# size=int(input("ENter size:"))
# for i in range(size):
#     num=int(input("ENter number:"))
#     a.append(num)
# print(a)
# count=0
# for i in range(size):
#     if a[i]%2!=0 or a[i]==2:
#         count=count+1
#         print("Prime")
#     else:
#         print("Not prime")
# print(count)

# num=int(input("Enter number:"))
# og=num
# rev=0
# while num>0:
#     rev=(rev*10)+num%10
#     num=num//10
# if(og==rev):
#     print("No is equal")
# else:
#     print("No is not equal")
    
# i=int(input("Enter Num"))
# og=i
# sum=0
# while i>0:
#     sum=sum+(i%10)*(i%10)*(i%10)
# if og==sum:
#     print("Armstrong")
# else:
#     print("Not Armstrong")
    
# print("Enter the Number: ")
# num = int(input())
# temp = num
# rev = 0
# while num>0:
#     rev =(rev*10)+num%10
#     num=num//10
# if temp==rev:
#     print("\nIt is a Palindrome Number")
# else:
#     print("\nIt is not a Palindrome Number")

# num = int(input("Enter a Number: "))

# rev = 0
# while num>0:
#   rem = num%10
#   rev = rem + (rev*10)
#   num = int(num/10)

# print("\nReverse =", rev)

# num = int(input("Enter a Number: "))
# tot=0
# while num>0:
#     num=num//10
#     tot=tot+1
# print(tot)

# num=int(input("Enter:"))
# sum=0
# while num>0:
#     sum=sum+num%10
#     num=num//10
# print(sum)

# num = input("Enter a Number: ")
# first_digit=int(num[1])
# last_digit=int(num[-2])
# sum=first_digit*last_digit
# print(sum)

# num = input("Enter a number: ")
# middle = num[1:-1]  # slice the middle digits
# product = 1
# for digit in middle:
#     product *= int(digit)
# print("Product of middle digits:", product)


# num = int(input("Enter a number: "))
# sum=0
# while num>0:
#     sum=sum+(num%10)*(num%10)
#     num=num//10
# print(sum)


# num = int(input("Enter a number: "))  # taking input from user

# # converting the number to a string for easier manipulation
# num_str = str(num)

# # interchanging the digits
# new_num_str = num_str[-1] + num_str[1:-1] + num_str[0]

# # converting the string back to an integer
# new_num = int(new_num_str)

# print("The number with digits interchanged is:", new_num)

# n=int(input("Enter no."))
# sum=0
# for i in range(0,n):
#     num=int(input("Enter values:"))
#     sum=sum+num
# print(sum)

# for i in range(256):
#     ch = chr(i)
#     print(i, " ", ch)

# text = input("Enter a String: ")
# for ch in text:
#     asc = ord(ch)
#     print(ch, "\t", asc)

# n = int(input("Enter"))

# fib = list()
# b = 1
# c = 0
# i = 1
# while i <= n:
#     if i == 1:
#         c = 0
#     elif i == 2 or i == 3:
#         c = 1
#     else:
#         a = b
#         b = c
#         c = a+b
#     fib.append(c)
#     i = i+1

# if len(fib) == 0:
#     print("\nOk!")
# else:
#     print("\nFirst", n, "Terms of Fibonacci Series are:")
#     for i in fib:
#         print(i, end=" ")
        
# n = int(input("Enter a number: "))
# fib_series = [0, 1] # Initialize the list with the first two elements of the series
# while fib_series[-1] < n:
#     # While the last element in the list is less than n, add the sum of the last two elements to the list
#     next_fib = fib_series[-1] + fib_series[-2]
#     if next_fib < n:
#         fib_series.append(next_fib)
#     else:
#         break
# fib_list = []
# for i in fib_series:
#     if i < n:
#         fib_list.append(i)
# print(fib_list)

# n = int(input("Enter the number of elements to be inserted: "))
# nums = []

# for i in range(n):
#     num = float(input(f"Enter element {i+1}: "))
#     nums.append(num)

# avg = sum(nums) / n

# print("Average of elements in the list:", avg)

# n=[]
# size=int(input("Enter size:"))
# for i in range(size):
#     val=int(input("Input values"))
#     n.append(val)
# print(n)
# even=0
# odd=0
# for i in range(size):
#     if n[i]%2==0:
#         even=even+1
#     else:
#         odd=odd+1
# print(even)
# print(odd)
        
# n=[]
# size=int(input("Enter size:"))
# for i in range(size):
#     val=int(input("Input values"))
#     n.append(val)
# print(n)
# maxno=0
# minno=0
# sum=0
# for i in range(size):
#     sum=sum+n[i]
#     if n[i]%2==0:
#         maxno=max(n)
#     else:
#         minno=min(n)
# print(maxno)
# print(minno)
# print(sum)

# n=[]
# size=int(input("Enter size:"))
# for i in range(size):
#     val=int(input("Input values"))
#     n.append(val)
# print(n)
# sum=0
# for i in range(size):
#     sum=sum+n[i]
# print(sum)

# n=[]
# size=int(input("Enter size:"))
# for i in range(size):
#     val=int(input("Input values"))
#     n.append(val)
# print(n)
# for i in range(size):
#     if i%2==0:
#         print(n[i])

# n=[]
# size=int(input("Enter size:"))
# for i in range(size):
#     val=int(input("Input values"))
#     n.append(val)
# print(n)
# list2=list(set(n))
# for i in range(size):
#     list2.sort()
# print(list2[1])

# n=[]
# size=int(input("Enter size:"))
# for i in range(size):
#     val=int(input("Input values"))
#     n.append(val)
# print(n)
# ele=int(input("Enter element for insertion:"))
# n.append(ele)
# print(n)

# n=[]
# size=int(input("Enter size:"))
# for i in range(size):
#     val=int(input("Input values"))
#     n.append(val)
# mul=1
# for i in range(size):
#     mul=mul*n[i]
# print(mul)

# n=[]
# size=int(input("Enter size:"))
# for i in range(size):
#     val=int(input("Input values"))
#     n.append(val)
# print(n)
# posOne=int(input())
# posTwo=int(input())
# for i in range(size):
#     n[posOne], n[posTwo] = n[posTwo], n[posOne]
# print(n)

# n=[]
# size=int(input("Enter size:"))
# for i in range(size):
#     val=int(input("Input values"))
#     n.append(val)
# print(n)
# new=[]
# for i in range(size):
#     if n[i] not in new:
#         new.append(n[i])
# print(new)


# print("Enter list 1:")
# n1=[]
# size=int(input("Enter size:"))
# for i in range(size):
#     val=int(input("Input values"))
#     n1.append(val)
# print(n1)
# print("Enter list 2:")
# n2=[]
# size=int(input("Enter size:"))
# for i in range(size):
#     val=int(input("Input values"))
#     n2.append(val)
# print(n2)
# n3=[]
# for i in range(size):
#     n3.append(n1[i])
# for i in range(size):
#     n3.append(n2[i])
# print(n3)

# print("Enter String: ", end="")
# sOne = input()

# sTwo = sOne[:]
# print("\nCopied String =", sTwo)

# n=[]
# size=int(input("Enter size:"))
# for i in range(size):
#     val=int(input("Input values"))
#     n.append(val)
# print(n)

# n=[]
# size=int(input("Enter size:"))
# for i in range(size):
#     val=int(input("Input values"))
#     n.append(val)
# print(n)
# strrev=n[::-1]
# print(strrev)

n=[]
size=int(input("Enter size:"))
for i in range(size):
    val=input("Input values")
    n.append(val)
print(n)
char=input()
sum=0
for i in range(size):
    if char==n[i]:
        sum=sum+1
print(sum)