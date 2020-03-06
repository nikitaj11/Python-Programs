def add(a,b):
    return a+b
def sub(a,b):
    return a-b


import sys
while 1:
    print(" 1.Addition \n 2. subtraction ")
    choice = int(input("Enter vhoice: "))
    a = int(input("Enter 1st no: "))
    b = int(input("Enter 2nd no: "))
    if choice == 1:
        c = add(a,b)
        print(c)
    elif choice == 2:
        c = sub(a,b)
        print(c)
    else:
        sys.exit()
