def valueerror(prompt):
    try:
        value=int(input())
        return value
    except ValueError:
        print("Error invalid input")
n=valueerror("Enter an integer")
print(n)