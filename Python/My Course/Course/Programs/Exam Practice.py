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

num = input("Enter a number: ")
middle = num[1:-1]  # slice the middle digits
product = 1
for digit in middle:
    product *= int(digit)
print("Product of middle digits:", product)

