import sys

students = []
id_no = 1
while 1:
    choice=int(input("Enter Your choice: "))
    print("1.add students ")
    if choice == 1:
        name = input("Enter ur name: ")
        age = input("Enter ur age: ")
        address = input("Enter ur address: ")
        
        students.append(name)
        students.append(age)
        students.append(address)
    
    print("Students : {}".format(students))