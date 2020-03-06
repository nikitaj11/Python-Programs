def stringReverse():
    str = input('Enter String to reverse: ')
    for i in  range(len(str), 0, -1):
        print(str[i-1], end='')



stringReverse()