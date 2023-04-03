a=[]
for n in range(1500,3000):
    if (n % 7 == 0 and n % 5 == 0):
        a.append(n)
    else:
        continue
print(a)