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
        id_no = id_no + 1
        
        students.append([name,age,address])
        
    elif choice == 2:
        
        del students[0]

    elif choice == 3:
        id = int(input("Enter ID no : "))
        print("\n")
        print("[+] Student ID : {}".format(id))
        print("    Student name : {}".format(students[id][0]))
        print("    Student age : {}".format(students[id][1]))
        print("    Student address : {}".format(students[id][2]))
        
        
    else :
        sys.exit()
