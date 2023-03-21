#wap to swap first and last number.

string=input("Enter a string: ")
result=string[-1]+string[1:-1]+string[0]
print(result)

#using while loop
string=input("Enter a string: ")
i=0
result=""
while i<len(string):
    if i==0:
        result+=string[-1]
    elif i==len(string)-1:
        result+=string[0]
    else:
        result+=string[i]
    i+=1
print(result)