try:
    age
except NameError as e:
    print("NameError")
    print(e)
finally:
    print("nikita")