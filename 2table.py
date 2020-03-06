def table():
    a = int(input('Enter number: '))
    for i in range(2, a+1, 1):
        print()
        for j in range(1, 11, 1):
            print(i * j)

table()