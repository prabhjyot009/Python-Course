#wap to raise an exception to enter age by user and age>80
# try:
#     age=int(input("Enter age:"))
#     if age<=18:
#         raise ValueError
#     else:
#         print("Eligible")
# except ValueError:
#     print("Not Eligible")
#wap to raise diff type of exceptions in the given prog: use else also along with try and except
# try:
#     age=int(input("Enter age:"))
#     if age<=18:
#         raise ValueError
#     else:
#         print("Eligible")
# except ValueError:
#     print("Not Eligible")

# try:
#     a=int(input())
#     b=int(input())
#     c=a/b
# except ZeroDivisionError:
#     print("Can't divide by zero")
# except ValueError:
#     print("Invalid input")
# else:
#     print("YO")

# 1. Write a Python program to handle a 
# ZeroDivisionError exception when dividing a 
# number by zero.

# exception ZeroDivisionError:
    
# Raised when the second argument of a division 
# or modulo operation is zero. The associated 
# value is a string indicating the type of the 
# operands and the operation.

# def divide(x,y):
#     try:
#         result=x/y
#         print("Result",result)
#     except ZeroDivisionError:
#         print("Can't divide by zero")

# # Usage
# # numerator = 5
# # denominator = 3
# # divide(numerator, denominator)
# x=int(input("x:"))
# y=int(input("y:"))
# call=divide(x,y)

#value error:
def valueerror(prompt):
    try:
        value=int(input())
        return value
    except ValueError:
        print("Error invalid input")
n=valueerror("Input an integer")
print("Input value",n)