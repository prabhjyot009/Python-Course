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

#algorithm
# step 1:start
# step 2:define a function count(str)
# step 3:initialize upper=0,lower=0
# step 4:for i in str
# step 5:if i.isupper()
# step 6:upper+=1
# step 7:elif i.islower()
# step 8:lower+=1
# step 9:print("Upper case letters:",upper)
# step 10:print("Lower case letters:",lower)
# step 11:stop

#objective:
# to count the number of uppercase and lowercase letters in a string