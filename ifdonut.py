price=int(input("Enter the price of the donut:Rs."))
quantity=int(input("Enter the number of donuts:"))
amount=price*quantity
if amount>1000:
    print("yess discount is applicable..!")
else:
    print('5% discount is available')
print("Your total amount is..",amount)
