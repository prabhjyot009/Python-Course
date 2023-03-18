'''Seprator is used to seperate the output'''

# x=10
# y=20
# z=30
# print(x,y,z,sep=",")
# print("Hello","World",sep=",")

'''End is used to end the output with a character'''

# #normal print
# print("Hello Python 1")
# print("Hello Python 2")
# print("Hello Python 3\n")

# #use of end
# print("Hello Python 1",end=" = ")
# print("Hello Python 2",end=" = ")
# print("Hello Python 3")

# name="Singh"
# age=19 #age is integer type variable so we can't use it in string concatenation
# age=str(age) #convert integer to string
# country="India"

# print("My name is",name,"and I am",age,"years old. I am from",country,".")

# #Concatenation
# print("My name is "+name+" and I am "+str(age)+" years old. I am from "+country+".")
# #or
# print("My name is "+name+" and I am "+age+" years old. I am from "+country+".")
# #format method
# print("My name is {} and I am {} years old. I am from {}.".format(name,age,country))
# #f-string
# print(f"My name is {name} and I am {age} years old. I am from {country}.")

# #input function
# name=input("Enter your name: ")
# print("Your name is:",name)
# #f-string
# print(f"Your name is: {name}")
# print(type(name))

Num1=int(input("Enter First Number:"))
Num2=int(input("Enter Second Number:"))
Num3=Num1+Num2;
print(f"The Sum Of Two Numbers {Num1} ,{Num2} Is: {Num3}")