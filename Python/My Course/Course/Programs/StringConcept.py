name="Singh"
for i in name:
    print(i,end='')#i zero se lehke name ke last index tak chalega 0 se lehke 4 tak.

    
#replication operator *:
name ="Singh"
print(2*name)

print(3*"singh")

#membership operator
name="Singh"
print("S" in name) #will give ouput true

#String Slicing: Syntax: string[start:end]

name="Singh"
print(name[1:-1])  #-1 se last karna hai

name="Singhs"
print(name[1:5])  #4 tak karna hai

name="Singh Brar"
print(name[6:],name[:5])

name="Hello World"
print(name[3:-2])
