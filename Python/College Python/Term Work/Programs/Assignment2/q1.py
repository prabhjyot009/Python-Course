#Write a program that reads three positive numbers a, b, c and determines whether they can form the three sides of a triangle.

side1 = int(input("Enter the first side of the triangle: "))
side2 = int(input("Enter the second side of the triangle: "))
side3 = int(input("Enter the third side of the triangle: "))
if side1 + side2 > side3 and side2 + side3 > side1 and side1 + side3 > side2:
    print("The given sides can form a triangle")
else:
    print("The given sides cannot form a triangle")