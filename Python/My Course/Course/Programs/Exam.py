# a=[]
# size=int(input("ENter size:"))
# for i in range(size):
#     num=int(input("ENter number:"))
#     a.append(num)
# print(a)
# count=0
# b=[]
# c=[]
# for i in range(size):
#     if a[i]%2!=0 or a[i]==2:
#         count=count+1
#         b.append(a[i])
#     else:
#         c.append(a[i])
# print(count)
# print(b)
# print(c)

# a=[]
# size=int(input("ENter size:"))
# for i in range(size):
#     num=int(input("ENter number:"))
#     a.append(num)
# print(a)
# count=0
# e=[]
# o=[]
# for i in range(size):
#     if a[i]%2==0:
#         count=count+1
#         e.append(a[i])
#     else:
#         o.append(a[i])
# print(count)
# print(e)
# print(o)

# a=[]
# size=int(input("ENter size:"))
# for i in range(size):
#     num=int(input("ENter number:"))
#     a.append(num)
# print(a)
# sum=0
# for i in range(size):
#     sum=sum+a[i]
# print(sum)

# a=[]
# size=int(input("ENter size:"))
# for i in range(size):
#     num=int(input("ENter number:"))
#     a.append(num)
# print(a)
# ele=int(input("Enter search element:"))
# for i in range(size):
#     if a[i]==ele:
#         print("index",i)
#         print("Position",i+1)

# Get the input list from the user
input_list = input("Enter the sorted list of numbers (comma-separated): ").split(",")
input_list = [int(i) for i in input_list]

# Get the number to search from the user
search_num = int(input("Enter the number to search: "))

# Initialize variables
left = 0
right = len(input_list) - 1
found = False

# Perform binary search
while left <= right:
    mid = (left + right) // 2
    if input_list[mid] == search_num:
        found = True
        break
    elif input_list[mid] < search_num:
        left = mid + 1
    else:
        right = mid - 1

# Print the result
if found:
    print(f"{search_num} found at index {mid}.")
else:
    print(f"{search_num} not found in the list.")

