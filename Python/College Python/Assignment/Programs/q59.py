def indexerror(list):
    try:
        print(list[5])
    except IndexError:
        print("Index out of range")
list=[1,2,3,4,5]
indexerror(list)