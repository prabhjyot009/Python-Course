#2.	Write a program to check whether input character is an uppercase letter or lowercase letter or a digit or a special character.

x = input("Enter a character: ")
if x.isupper():
    print("The character is an uppercase letter")
elif x.islower():
    print("The character is a lowercase letter")
elif x.isdigit():
    print("The character is a digit")
else:
    print("The character is a special character")
    