num=int(input("Enter a number:"))
sum=0
temp=num
    while temp>0:
       sum +=digit**3
    if num==sum:
        print("{} is an armstrong".format(num))
    else:
        print("{} is not and armstrong".format(num))