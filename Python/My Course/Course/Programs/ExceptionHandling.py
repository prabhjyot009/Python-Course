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
try:
    age=int(input("Enter age:"))
    if age<=18:
        raise ValueError
    else:
        print("Eligible")
except ValueError:
    print("Not Eligible")