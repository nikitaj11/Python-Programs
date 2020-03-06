import sys

appl_name = "Library Management System"
books = {}
students = {}
sid_no=1
bid_no=1
while 1:
    print("[*] {} [*]".format(appl_name))
    print("1. Add Books \n 2. View Books \n 3. Delete Books \n 4. Books Info \n 5. Add Students \n 6. View students \n 7. Exit ")
    choice = int(input("Enter Your Choice: "))

    if choice == 1:
        Book_name = input("Enter book name: ")
        Books_Author_name = input("Enter author name: ")
        Books_Publication = input("Enter publication's name: ")
        price_of_the_book = int(input("Enter the price: "))
        Books_Quantity = int(input("Available Books: "))
        books[bid_no] = [Book_name,Books_Author_name,Books_Publication,price_of_the_book,Books_Quantity]
        print("books : {}".format(books))
        bid_no = bid_no+1

    if choice == 2:
        for i in books:
            print("[*] Book ID : {}".format(i))
            print(" Book Name : {}".format(books[i][0]))
            print(" Book Author Name : {}".format(books[i][1]))
            print(" Books Publication : {}".format(books[i][2]))
            print(" Price of the book : {}".format(books[i][3]))
            print(" Books Quantity : {}".format(books[i][4]))

    if choice == 3:
        bid_no = int(input("Enter Book ID:"))
        del books[bid_no]

    if choice == 4:
        id = int(input("Enter Book ID:"))
        print("[*] Book ID : {}".format(id))
        print(" Book Name : {}".format(books[id][0]))
        print(" Book Author Name : {}".format(books[id][1]))
        print(" Books Publication : {}".format(books[id][2]))
        print(" Price of the book : {}".format(books[id][3]))
        print(" Books Quantity : {}".format(books[id][4]))
       
        
    if choice == 5:
        student_name = input("Enter Your name: ")
        student_course = input("Enter your course: ")
        student_admission_yr = input("Enter your admission year: ")
        Student_dept = input("Enter your dept: ")
        student_contact = input("Enter your contact no.: ")
        student_semester = input("Enter sem: ")
        students[sid_no] = [student_name,student_course,student_admission_yr,Student_dept,student_contact,student_semester]
        sid_no = sid_no + 1
        print("students : {}".format(students))

    if choice == 6:
        for i in books:
            print("[*] Student ID : {}".format(i))
            print(" Student Course : {}".format(students[i][0]))
            print(" Student Adm yr : {}".format(students[i][1]))
            print(" Student Dept : {}".format(students[i][2]))
            print(" student contact : {}".format(students[i][3]))
            print(" student semseter: {}".format(students[i][4]))

    if choice == 7:
        break

print("Thank You..!")
sys.exit()



        
        

