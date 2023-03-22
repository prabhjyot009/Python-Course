#Write a program to display all prime numbers within a range using while loop.

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
i = num1
while i <= num2:
    j = 2
    while j < i:
        if i % j == 0:
            break
        j += 1
    if j == i:
        print(i)
    i += 1
    
#objective of the program is to display all prime numbers within a range using while loop.

#algorithm

#1.	Ask the user to enter the first number
#2.	Ask the user to enter the second number
#3.	Declare a variable i and assign it the value of num1
#4.	While i is less than or equal to num2
#5.	Declare a variable j and assign it the value 2
#6.	While j is less than i
#7.	If i is divisible by j
#8.	Break
#9.	Increment j by 1
#10.	If j is equal to i
#11.	Print i
#12.	Increment i by 1