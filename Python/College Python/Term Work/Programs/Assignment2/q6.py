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