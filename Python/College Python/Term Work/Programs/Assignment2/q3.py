#Write a program to check whether input number is of one digit or two digit or three digit or more than three digit.

num = int(input("Enter a number: "))
if num < 10:
    print("The number is of one digit")
elif num < 100:
    print("The number is of two digits")
elif num < 1000:
    print("The number is of three digits")
else:
    print("The number is of more than three digits")
    