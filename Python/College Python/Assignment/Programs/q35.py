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

#algorithm
# step 1:start
# step 2:define a function local()
# step 3:initialize count=0,a=10,b=20,c=20
# step 4:for i in locals()
# step 5:count+=1
# step 6:print("Number of local variables:",count)
# step 7:stop

#objective:
# to count number of local variables in a function.