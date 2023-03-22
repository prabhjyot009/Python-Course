#Write a program that reads three positive numbers a, b, c and determines whether they can form the three sides of a triangle.

side1 = int(input("Enter the first side of the triangle: "))
side2 = int(input("Enter the second side of the triangle: "))
side3 = int(input("Enter the third side of the triangle: "))
if side1 + side2 > side3 and side2 + side3 > side1 and side1 + side3 > side2:
    print("The given sides can form a triangle")
else:
    print("The given sides cannot form a triangle")
    
#objective of the program is to check whether the given sides can form a triangle or not

#algorithm

#1.	Ask the user to enter the first side of the triangle
#2.	Ask the user to enter the second side of the triangle
#3.	Ask the user to enter the third side of the triangle
#4.	Check whether the sum of the first two sides is greater than the third side and the sum of the second and third sides is greater than the first side and the sum of the first and third sides is greater than the second side
#5.	If the condition is true, print that the given sides can form a triangle
#6.	Else, print that the given sides cannot form a triangle