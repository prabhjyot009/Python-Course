num = int(input("Enter the number:"))
if num == 1:
    print("It is not prime")
if num > 1:
    for i in range(2,num):
        if num % i == 0:
            print(num,"it is not prime")
            break
    else:
        print(num,"it is prime")