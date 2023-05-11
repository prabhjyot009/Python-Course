#write a python function to check whether no is perfect or not.

def perfect(n):
    sum=0
    for i in range(1,n):
        if n%i==0:
            sum+=i
    if sum==n:
        print("Perfect number")
    else:
        print("Not perfect number")
n=int(input("Enter number:"))
perfect(n)