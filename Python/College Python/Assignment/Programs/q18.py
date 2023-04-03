n = int(input("Enter:"))
a = []
for i in range(0, n+1):
    temp = i
    rev = 0
    while temp:
        rev = (rev*10)+temp % 10
        temp = temp//10
    if i != rev:
        a.append(i)
    else:
        continue
print(a)