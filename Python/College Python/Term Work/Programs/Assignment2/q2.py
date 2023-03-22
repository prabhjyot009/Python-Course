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
    
    
#objective of the program is to check whether the input character is an uppercase letter or a lowercase letter or a digit or a special character.

#algorithm

#1.	Ask the user to enter a character
#2.	Check whether the character is an uppercase letter
#3.	If the condition is true, print that the character is an uppercase letter
#4.	Else, check whether the character is a lowercase letter
#5.	If the condition is true, print that the character is a lowercase letter
#6.	Else, check whether the character is a digit
#7.	If the condition is true, print that the character is a digit
#8.	Else, print that the character is a special character
