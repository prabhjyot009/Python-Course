#write a python program to check the type of input using if else statement

num = input("Enter a number: ")
if num.isdigit():
    print("Integer")
    
elif num.isalpha():
    print("String")
    
elif num.isalnum():
    print("Alphanumeric")

elif num.isspace():
    print("Space")
    
else:
    print("Special character")