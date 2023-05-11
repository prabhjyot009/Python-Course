#write a program that accepts a string and counts the number of uppercase and lowercase letters in it.
def count(str):
    upper=0
    lower=0
    for i in str:
        if i.isupper():
            upper+=1
        elif i.islower():
            lower+=1
    print("Upper case letters:",upper)
    print("Lower case letters:",lower)
str=input("Enter string:")
count(str)