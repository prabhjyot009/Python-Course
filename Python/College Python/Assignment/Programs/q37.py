#wap that count even and odd no. 
def count_no(n):
    even=0
    odd=0
    if n==1:
        return 1;
    elif n==0:
        return 0;
    else:
        even+=count_no(n-1)
        odd=n-even
        return odd
n=int(input("Enter number:"))
print("Even numbers:",count_no(n))
print("Odd numbers:",n-count_no(n))