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

#algorithm
# step 1:start
# step 2:define a function perfect(n)
# step 3:initialize sum=0
# step 4:for i in range(1,n)
# step 5:if n%i==0
# step 6:sum+=i
# step 7:if sum==n
# step 8:print("Perfect number")
# step 9:else
# step 10:print("Not perfect number")

#objective:
# to check whether no is perfect or not.