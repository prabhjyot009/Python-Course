marks=int(input("Enter your makrs:"))
if marks>80:
    print("Grade A")
    age=int(input("Enter your age:"))
    if age>=20:
        print("You are eligible for admission")
    else:
        print("You are not eligible for admission")
elif marks>60:
    print("Grade B")
elif marks>40:
    print("Grade C")
else:
    print("Fail")
    