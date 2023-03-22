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
    
    
#objective of the program is to check whether the input number is of one digit or two digit or three digit or more than three digit.

#algorithm

#1.	Ask the user to enter a number
#2.	Check whether the number is less than 10
#3.	If the condition is true, print that the number is of one digit
#4.	Else, check whether the number is less than 100
#5.	If the condition is true, print that the number is of two digits
#6.	Else, check whether the number is less than 1000
#7.	If the condition is true, print that the number is of three digits
#8.	Else, print that the number is of more than three digits