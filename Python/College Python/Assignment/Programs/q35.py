#wap to count number of local variables in a function.
def local():
    count=0
    a=10
    b=20
    c=20
    for i in locals():
        count+=1
    print("Number of local variables:",count)
local()