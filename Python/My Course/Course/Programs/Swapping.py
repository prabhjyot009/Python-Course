x=int(input("The value of x is:"));
y=int(input("The value of y is:"));

#using third variable:
temp=x;  #temp=10
x=y;     #x=20;
y=temp;  #y=10;

s1="The Final answer after swapping is {}{}"
print(s1.format(x,y))

#without using third variable
x,y=y,x
s1="The Final answer after swapping is {}{}"
print(s1.format(y,x))