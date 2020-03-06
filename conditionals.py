Y=input("year:")
x=int(Y)
if x%4==0 and x%100!=0:
    print("this is leap")
elif x%100==0:
    print("this is not leap year")
elif x%400==0:
    print("this is leap year")
else:
    print("This is not a leap year")
