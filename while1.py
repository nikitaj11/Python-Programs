a = int(input("Enter a number: "))
sum = 0
for i in range(a):
    sum = sum + i
    print("Nikita + {}".format(sum))
    if sum%2 == 0:
        print("even {}".format(sum))
    else:
        print("Odd {}".format(i))
    