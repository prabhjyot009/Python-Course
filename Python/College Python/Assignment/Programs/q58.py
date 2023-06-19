def valueerror(prompt):
    try:
        value=int(input())
        return value
    except ValueError:
        print("Error invalid input")
n=valueerror("Enter an integer")
print(n)

x=5
y="hello"
try:
    z=x+y
except TypeError:
    print("Error")
finally:
    print("FUck")
    
