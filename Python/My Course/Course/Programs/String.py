#String in python is immutable
#String is an array
#String is a sequence of characters
#String is a collection of characters
#String is a collection of characters

#String Methods

#capitalize()
a="hello world"
print(a.capitalize())

#center()
print(a.center(13,"*"))

#upper()
print(a.upper())

#lower()
print(a.lower())

#replace()
print(a.replace("world","everyone"))

#split()
print(a.split())

#find()
print(a.find("r"))

#count()
print(a.count("l"))

#isnumeric()
print(a.isnumeric())

#islower()
print(a.islower())

#isupper()
print(a.isupper())

#String Declaration
x="Hello"
y="Sir"
z=x+y
print(z)

#String Array
print(x[1])
print(y[0])

#in reverse
print(x[-1])
print(y[-2])

#String Length
print(len(x))
print(len(y))

# String IN operator:
print("ell" in x)

#String Not IN operator:
print("ell" not in x)

#String Slicing
a="What up biatch"
print(a[1:9])
print(a[2:])
print(a[-2:])
print(a[-6:14])
print(a[-12:-4])

#String Concatination
b="eyo"
c="wasup"
d=b+""+c
print(d)
print("Hello"+" "+"World")
print(b*2)

#String Format
item='Apple'
qty=20
price=30.17
s1="I want {} kg {} for {} dollars"
print(s1.format(qty,item,price))
#or
s2="I want {1} kg {2} for {2} dollars"
print(s1.format(qty,item,price))

#escape sequencing
t1="hey you \"mf\""
print(t1)

