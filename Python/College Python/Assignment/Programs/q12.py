# wap to reverse a string and check if it is palindrome or not using while loop.
string = input("Enter a string: ")
reverse_string = ""
i = len(string) - 1
while (i >= 0):
    reverse_string = reverse_string + string[i]
    i =i-1
if (string == reverse_string):
    print(string, "is a palindrome")
else:
    print(string, "is not a palindrome")
