'''Python Operators Precedence'''

'''Arithmetic Operators'''

# + Addition
print(10+20)
#user input
num1=int(input("Enter First Number:"))
num2=int(input("Enter Second Number:"))
num3=num1+num2;
print(f"The Sum Of Two Numbers {num1} ,{num2} Is: {num3}")

# - Subtraction
print(10-20)
#user input
num1=int(input("Enter First Number:"))
num2=int(input("Enter Second Number:"))
num3=num1-num2;
print(f"The Subtraction Of Two Numbers {num1} ,{num2} Is: {num3}")

# * Multiplication
print(10*20)
#user input
num1=int(input("Enter First Number:"))
num2=int(input("Enter Second Number:"))
num3=num1*num2;
print(f"The Multiplication Of Two Numbers {num1} ,{num2} Is: {num3}")

# / Division
print(10/20)
#user input
num1=int(input("Enter First Number:"))
num2=int(input("Enter Second Number:"))
num3=num1/num2;
print(f"The Division Of Two Numbers {num1} ,{num2} Is: {num3}")

# % Modulus
print(10%20)
#user input
num1=int(input("Enter First Number:"))
num2=int(input("Enter Second Number:"))
num3=num1%num2;
print(f"The Modulus Of Two Numbers {num1} ,{num2} Is: {num3}")

# ** Exponentiation
print(10**20)
#user input
num1=int(input("Enter First Number:"))
num2=int(input("Enter Second Number:"))
num3=num1**num2;
print(f"The Exponentiation Of Two Numbers {num1} ,{num2} Is: {num3}")

# // Floor Division
print(10//20)
#user input
num1=int(input("Enter First Number:"))
num2=int(input("Enter Second Number:"))
num3=num1//num2;
print(f"The Floor Division Of Two Numbers {num1} ,{num2} Is: {num3}")


'''Comparison Operators'''

# == Equal
print(10==20)
#user input
num1=int(input("Enter First Number:"))
num2=int(input("Enter Second Number:"))
num3=num1==num2;
print(f"The Equal Of Two Numbers {num1} ,{num2} Is: {num3}")

# != Not Equal
print(10!=20)
#user input
num1=int(input("Enter First Number:"))
num2=int(input("Enter Second Number:"))
num3=num1!=num2;
print(f"The Not Equal Of Two Numbers {num1} ,{num2} Is: {num3}")

# > Greater Than
print(10>20)
#user input
num1=int(input("Enter First Number:"))
num2=int(input("Enter Second Number:"))
num3=num1>num2;
print(f"The Greater Than Of Two Numbers {num1} ,{num2} Is: {num3}")

# < Less Than
print(10<20)
#user input
num1=int(input("Enter First Number:"))
num2=int(input("Enter Second Number:"))
num3=num1<num2;
print(f"The Less Than Of Two Numbers {num1} ,{num2} Is: {num3}")

# >= Greater Than or Equal To
print(10>=20)
#user input
num1=int(input("Enter First Number:"))
num2=int(input("Enter Second Number:"))
num3=num1>=num2;
print(f"The Greater Than or Equal To Of Two Numbers {num1} ,{num2} Is: {num3}")

# <= Less Than or Equal To
print(10<=20)
#user input
num1=int(input("Enter First Number:"))
num2=int(input("Enter Second Number:"))
num3=num1<=num2;
print(f"The Less Than or Equal To Of Two Numbers {num1} ,{num2} Is: {num3}")


'''Assignment Operators'''

# += Addition Assignment
a=10
a+=20
print(a)
#OR
a=10
b=20
a+=b
print(a)
#or
a=10
b=20
a=a+b
print(a)


# -= Subtraction Assignment
a=10
a-=20
print(a)
#OR
a=10
b=20
a-=b
print(a)
#or
a=10
b=20
a=a-b
print(a)

# *= Multiplication Assignment
a=10
a*=20
print(a)
#OR
a=10
b=20
a*=b
print(a)
#or
a=10
b=20
a=a*b
print(a)

# /= Division Assignment
a=10
a/=20
print(a)
#OR
a=10
b=20
a/=b
print(a)
#or
a=10
b=20
a=a/b
print(a)

# %= Modulus Assignment
a=10
a%=20
print(a)
#OR
a=10
b=20
a%=b
print(a)
#or
a=10
b=20
a=a%b
print(a)

# **= Exponentiation Assignment
a=2
a**=3
print(a)
#OR
a=2
b=3
a**=b
print(a)
#or
a=2
b=3
a=a**b
print(a)

# //= Floor Division Assignment
a=10.23
a//=20
print(a)
#OR
a=10.23
b=20
a//=b
print(a)
#or
a=10.23
b=20
a=a//b
print(a)

'''Logical Operators'''

# and Logical AND
print(10>20 and 20>10)
#or
a=10
b=20
print(a>b and b>a)
#user input
num1=int(input("Enter First Number:"))
num2=int(input("Enter Second Number:"))
num3=num1>num2 and num2>num1;
print(f"The Logical AND Of Two Numbers {num1} ,{num2} Is: {num3}")

# or Logical OR
print(10>20 or 20>10)
#or
a=10
b=20
print(a>b or b>a)
#user input
num1=int(input("Enter First Number:"))
num2=int(input("Enter Second Number:"))
num3=num1>num2 or num2>num1;
print(f"The Logical OR Of Two Numbers {num1} ,{num2} Is: {num3}")

# not Logical NOT
print(not 10>20)
#or
a=10
b=20
print(not a>b)
#user input
num1=int(input("Enter First Number:"))
num2=int(input("Enter Second Number:"))
num3=not num1>num2;
print(f"The Logical NOT Of Two Numbers {num1} ,{num2} Is: {num3}")

'''Identity Operators'''

# is Identity
a=10
b=20
print(a is b)
#user input
num1=int(input("Enter First Number:"))
num2=int(input("Enter Second Number:"))
num3=num1 is num2;
print(f"The Identity Of Two Numbers {num1} ,{num2} Is: {num3}")

# is not Identity
a=10
b=20
print(a is not b)
#user input
num1=int(input("Enter First Number:"))
num2=int(input("Enter Second Number:"))
num3=num1 is not num2;
print(f"The Identity Of Two Numbers {num1} ,{num2} Is: {num3}")

'''Membership Operators'''

# in Membership
print(10 in [10,20,30])
#or
a=10
b=[10,20,30]
print(a in b)
#user input
num1=int(input("Enter First Number:"))
num2=[10,20,30]
num3=num1 in num2;
print(f"The Membership Of Two Numbers {num1} ,{num2} Is: {num3}")

# not in Membership
print(10 not in [10,20,30])
#or
a=10
b=[10,20,30] #list
print(a not in b)
#user input
num1=int(input("Enter First Number:"))
num2=[10,20,30]
num3=num1 not in num2;
print(f"The Membership Of Two Numbers {num1} ,{num2} Is: {num3}")

'''Bitwise Operators'''

# & Bitwise AND
print(10&20)
#or
a=53
b=23
print(a&b)
#user input
num1=int(input("Enter First Number:"))
num2=int(input("Enter Second Number:"))
num3=num1&num2;
print(f"The Bitwise AND Of Two Numbers {num1} ,{num2} Is: {num3}")

# | Bitwise OR
print(10|20)
#or
a=53
b=23
print(a|b)
#user input
num1=int(input("Enter First Number:"))
num2=int(input("Enter Second Number:"))
num3=num1|num2;
print(f"The Bitwise OR Of Two Numbers {num1} ,{num2} Is: {num3}")

# ^ Bitwise XOR (Exclusive OR) #if both bits are same then 0 else 1
print(10^20)
#or
a=56
b=23
print(a^b)
#user input
num1=int(input("Enter First Number:"))
num2=int(input("Enter Second Number:"))
num3=num1^num2;
print(f"The Bitwise XOR Of Two Numbers {num1} ,{num2} Is: {num3}")

# ~ Bitwise NOT
print(~10)
#or
a=10
print(~a)
#user input
num1=int(input("Enter First Number:"))
num3=~num1;
print(f"The Bitwise NOT Of Two Numbers {num1} Is: {num3}")

# << Bitwise Left Shift
print(10<<2)
#or
a=10
print(a<<2)
#user input
num1=int(input("Enter First Number:"))
num3=num1<<2;
print(f"The Bitwise Left Shift Of Two Numbers {num1} Is: {num3}")

# >> Bitwise Right Shift
print(10>>2)
#or
a=10  # 1010
print(a>>2)  # 0010  2
#user input
num1=int(input("Enter First Number:"))
num3=num1>>2;
print(f"The Bitwise Right Shift Of Two Numbers {num1} Is: {num3}")

