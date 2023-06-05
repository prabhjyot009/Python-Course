#wap to raise diff type of exceptions in the given prog: use else also

try:
    age=int(input("Enter age:"))
    if age<=18:
        raise ValueError
    else:
        print("Eligible")
except ValueError:
    print("Not Eligible")
else:
    print("No exception raised")