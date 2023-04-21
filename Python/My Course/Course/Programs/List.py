# a=["ram",1,"shyam",12.5]
# print(a)
# print(a[0][-1::-1]) #revrse of 1st element
# print(a[-1])
# a[1]=100
# print(a[1])



# l=[]
# a=int(input("Enter"))
# for i in range(0,a):
#     a=int(input("Enter next:"))
#     if(a%5==0 and a!=100):
#         l.append(a);
#     else:
#         break;
# print(l)

# a=[]
# size=int(input("Enter size:"))
# for i in range(size):
#     num=int(input("Enter elements"))
#     a.append(num)
# print("The elements in list are:",a)
# sum=0
# for i in range(size):
#     sum=sum+a[i]
# print(sum)
# print(max(a))

'''
a=[]
size=int(input("Enter size:"))
for i in range(size):
    num=int(input("Enter values:"))
    a.append(num)
print(a)
odd=0
even=0
for i in range(size):
    if a[i]%2==0:
        even=even+1
    else:
        odd=odd+1
print("Total number of odd nos. are:",even)
print("Total number of odd nos. are:",odd)'''

'''
a=[]
size=int(input("Enter size:"))
for i in range(size):
    num=int(input("Enter values:"))
    a.append(num)
print(a)
sum=0
pro=1
for i in range(size):
    if a[i]%2==0:
        sum=sum+a[i]
    else:
        pro=pro*a[i]
print("sum of even nos. are:",sum)
print("pro of odd nos. are:",pro)'''

'''a=[]
size=int(input("Enter size:"))
for i in range(size):
    num=int(input("Enter values:"))
    a.append(num)
key=int(input("Enter the elemnt you want to search:"))
flag=0
pos=0
for i in range(size):
    if a[i]==key:
        flag=1
        pos=i+1
        break;
if(flag==1):
    print("element found at position,",pos)
else:
    print("Element not found")'''
    
#program to count frequency of a number:
'''a=[]
size=int(input("Enter size:"))
for i in range(size):
    num=int(input("Enter values:"))
    a.append(num)
val=int(input("Enter number:"))
f=a.count(val)
print(f)'''

'''a=[]
size=int(input("Enter size:"))
for i in range(size):
    num=int(input("Enter values:"))
    a.append(num)
key=int(input("Enter elemnt:"))
count=0
for i in range(size):
    if a[i]==key:
        count=count+1
    else:
        break
print(count)'''

#prog to find max and min in a list:
'''a=[]
size=int(input("Enter size:"))
for i in range(size):
    num=int(input("Enter elements:"))
    a.append(num)
print(a)
x=max(a)
y=min(a)
print(x)
print(y)'''

#or
'''a=[]
size=int(input("Enter size:"))
for i in range(size):
    num=int(input("Enter elements:"))
    a.append(num)
max=a[0]
for i in range(size):
    if a[i]>max:
        max=a[i]
    if a[i]<max:
        min=a[i]
print(max)
print(min)'''

'''a=[]  #initializing list
size=int(input("Enter size:"))  #getting size from user
for i in range(size):  #looping through the list
    num=int(input("Enter elements:"))  #getting the elements from the user
    a.append(num)  #appending the elements to the list
i=0
j=size-1
t=a[i]
a[i]=a[j]
a[j]=t
i=i+1
j=j-1
print("List after reverse:")
for i in range(size):
    print(a[i],end=' ')'''


# a=[]
# size=int(input("enter size: "))
# for i in range(size):
#     value=int(input("enter value: "))
#     a.append(value)
# print("Orignal list is: ",a)
# a.sort()
# print("2nd Min value in list is: ",a[1])
# print("2nd Max value in list is: ",a[-2])

#Write a program to to take a string from user and find total no of words 
# in a string and reverse each word and store into a new string.

# a=input("Enter a string: ") # Enter a string
# b=a.split() # Split the string and create a list
# print("Total no of words in a string is: ",len(b)) # Print the length of list
# print("Total no of letters in a string is: ",len(a))
# c=[]
# for i in b:
#     c.append(i[::-1]) # Append the reverse of each word to list c
# print("Reverse of each word is: ",c)

#14.Write a program to find count of vowels,consonants and special characters.

# a=input("Enter a string: ")
# vowels=0
# consonants=0
# special=0
# for i in a:
#     if i in 'aeiouAEIOU':
#         vowels=vowels+1
#     elif i in 'bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ':
#         consonants=consonants+1
#     else:
#         special=special+1
# print("Total no of vowels in a string is: ",vowels)
# print("Total no of consonants in a string is: ",consonants)
# print("Total no of special characters in a string is: ",special)

#14.Write a program to find count of vowels,consonants and special characters using list.

# a=input("Enter a string: ")
# vowels=0
# consonants=0
# special=0
# v=['a','e','i','o','u','A','E','I','O','U']
# c=['b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','y','z','B','C','D','F','G','H','J','K','L','M','N','P','Q','R','S','T','V','W','X','Y','Z']
# for i in a:
#     if i in v:
#         vowels=vowels+1
#     elif i in c:
#         consonants=consonants+1
#     else:
#         special=special+1
# print("Total no of vowels in a string is: ",vowels)
# print("Total no of consonants in a string is: ",consonants)
# print("Total no of special characters in a string is: ",special)

#lcm of two numbers using factors:
# a=int(input("Enter a number: "))
# b=int(input("Enter a number: "))
# c=[]
# d=[]
# for i in range(1,a+1):
#     if a%i==0:
#         c.append(i)
# print("Factors of a: ",c)
# for j in range(1,b+1):
#     if b%j==0:
#         d.append(j)
# print("Factors of b: ",d)
# e=[]
# for i in c:
#     for j in d:
#         if i==j:
#             e.append(i)
# print("Common factors: ",e)
# print("LCM of two numbers is: ",max(e))
# print("HCF of two numbers is: ",min(e))

#binary search:

# Binary Search Algorithm
a = [] # Empty list
size = int(input("Enter size: ")) # 5
# Input the array
for i in range(size): # 0,1,2,3,4
    value = int(input("Enter value: ")) # 5,7,2,9,1
    a.append(value) # a[0]=5, a[1]=7, a[2]=2, a[3]=9, a[4]=1
print("Orignal list is: ", a) # [5,7,2,9,1]
# Sort the array
a.sort() # [1,2,5,7,9]
print("Sorted list is: ", a) # [1,2,5,7,9]
# Input the key to be searched
key = int(input("Enter key: ")) # 5
low = 0 # 0
high = size-1 # 4
# Search the key using for loop
for i in range(size): # 0,1,2,3,4
    mid = (low+high)//2 # 2
    if key == a[mid]: # 5==5
        print("Element found at: ", mid) # 2
        break
    elif key < a[mid]: # 5<5
        high = mid-1 # 1
    elif key > a[mid]: # 5>5
        low = mid+1 # 3
else:
    print("Element not found")
    
    #output:
    
# Enter size: 5
# Enter value: 5
# Enter value: 7
# Enter value: 2
# Enter value: 9
# Enter value: 1
# Orignal list is:  [5, 7, 2, 9, 1]
# Sorted list is:  [1, 2, 5, 7, 9]
# Enter key: 5
# Element found at:  2