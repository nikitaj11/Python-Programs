students = []
students = ["nikita","22","cs"]
try:
    del students[4]
except:
    print("List out of index")
finally:
    print("Bydefault")