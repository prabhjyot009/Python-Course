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

#String Format
name='Singh'
age='18'
s1="Hi my name is {} and i am {} years old"
print(s1.format(name,age))