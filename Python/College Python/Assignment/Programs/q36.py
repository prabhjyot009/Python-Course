#wap to display fibonacci sequence using recursion.
def fibo(n):
    if n<=1:
        return n
    else:
        return fibo(n-1)+fibo(n-2)
n=int(input("Enter number:"))
for i in range(n):
    print(fibo(i),end=" ")
print()

#algorithm
# step 1:start
# step 2:define a function fibo(n)
# step 3:if n<=1
# step 4:return n
# step 5:else
# step 6:return fibo(n-1)+fibo(n-2)
# step 7:for i in range(n)
# step 8:print(fibo(i),end=" ")
# step 9:stop

#objective:
# to display fibonacci sequence using recursion.