'''
year=365 days
leap year=366 days (once in 4 years)

Condition 1:
if(400%year==0) AND (100%year==0) #for century years
Condition 2:
if(4%year==0) AND (100%year!=0) #for non century years

'''

year=int(input("Enter a year: "))
if(year%400==0) and (year%100==0):
    print("Leap year")
elif(year%4==0) and (year%100!=0):
    print("Leap year")
else:
    print("Not a leap year")
    
#using nested if

year=int(input("Enter a year: "))
if(year%4==0):
    if(year%100==0):
        if(year%400==0):
            print("Leap year")
        else:
            print("Not a leap year") 
    else:
        print("Leap year") 
else:
    print("Not a leap year")