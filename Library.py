from Classes import Book, Library

isaac = Book("978-0-460-89012-2", "From Grass To Grace", "Federal Sedinam", "Motivational", "Available", 50, 30, "1A")
derry = Book("978-0-826-48565-2", "Life Means Hope", "Katherine Flux", "Motivational", "Borrowed", 70, 0, "4E")
george = Book("978-0-685-28789-9", "No Sweetness Here", "Charlie Chaplin", "Fiction", "Borrowed", 89, 0, "3A")
sedinam = Book("978-0-460-15812-2", "God Is Love", "Federal Sedinam", "History", "Available", 50, 2, "1A")
kevin = Book("978-0-685-25489-9", "Gifted Hands", "Ben Carson", "Motivational", "Available", 79, 25, "3A")
peter = Book("978-0-685-55907-9", "Data structure and Algorithm", "Dr. Theresa Adjaidoo", "Programming", "Available", 54, 4, "2B")
marvin= Book("978-0-333-87654-7", "Evangelism by fire", "Reinhard Bonke", "Christian", "Available", 150, 50, "4E")
kwame = Book("978-0-567-98145-8", "Born to run", "Christopher McDougall", "Sport", "Available", 200, 15, "3A")
gideon = Book("978-0-465-81345-5", "Silver Spoon", "Peggy Oppong", "Fiction", "Available", 100, 24, "1A")

library = Library([isaac, derry, george, sedinam, kevin, peter, marvin, kwame, gideon])
admin_password = "algorithm"


def print_books(books):
    if type(books) != str:
        if len(books) == 1:
            print(books[0])
            return books[0].book_ISBN
        else:
            print("\nSelect a book:")
            for i in range(len(books)):
                print(f"\t{i + 1}. {books[i].title}")
            book_choice = int(input(">>Enter choice: "))
            print()
            print(books[book_choice - 1])
            return books[0].book_ISBN
    else:
        print()
        print(books)


def book_operation(operation):
    while True:
        print("\nSelect an option: ")
        print("\t1. Enter ISBN")
        print("\t2. Enter Title")
        if operation == 2:
            print("\t3. Enter Author")
            print("\t4. Exit")
        else:
            print("\t3. Exit")
        choice = int(input(">>> "))

        if choice == 1:
            book_isbn = input("\n>>Enter Book ISBN: ").strip()
            if operation == 1:
                print(library.borrow_book(book_isbn))
                borrow_request = input(">>> ")

                if borrow_request.title() == "Y":
                    print("\nBorrow Request has been submitted")
                    library.request_book(book_isbn)
                else:
                    print("\nThanks...See you some other time")
            else:
                print()
                print(library.search_by_ISBN(book_isbn))
        elif choice == 2:
            book_title = input("\n>>Enter Book Title: ").lower().strip()
            books = library.search_by_title_or_author(book_title, choice)

            if operation == 1:
                book_isbn = print_books(books)
                print(library.borrow_book(book_isbn))
                borrow_request = input(">>> ")

                if borrow_request.title() == "Y":
                    print("\nBorrow Request has been submitted")
                    library.request_book(book_isbn)
                else:
                    print("\nThanks...See you some other time")
            else:
                print_books(books)

        elif choice == 3:
            print()
            if operation == 1:
                break
            else:
                book_author = input(">>Enter Book Author: ").lower().strip()
                books = library.search_by_title_or_author(book_author, choice)
                print_books(books)

        elif choice == 4:
            if operation == 2:
                break
        else:
            print("Invalid input")


def add_new_book():

    print("\nEnter Book Details: ")
    book_title = input("Title: ").title().strip()
    book_isbn = input("ISBN: ")
    book_author = input("Author: ").title().strip()
    book_category = input("Category: ").title().strip()
    book_copies = int(input("Copies: "))
    book_page_count = int(input("Page Count: "))
    book_location = input("Location: ").title().strip()

    new_book = Book(book_isbn, book_title, book_author, book_category, "Available", book_page_count, book_copies, book_location)
    library.add_new_book(new_book)


def update_book():
    book_isbn = input("\nEnter Book ISBN: ")

    if library.check_ISBN(book_isbn):
        book_copies = int(input("Enter no. of copies: "))
        library.update_book(book_isbn, book_copies)
        print("\nBooks have been added")
    else:
        print("\nBook does not exist... Kindly add book")


def admin_login():
    global admin_password
    password_count = 0
    password = input("\nEnter password: ")

    while True:
        if password_count == 2:
            print("\nYou have attempted 3 times.")
            password = input("Enter new password: ")
            admin_password = password
            password_count = 0

        if password == admin_password:
            print("\nWelcome...Librarian")
            print("Select an option: ")
            print("\t1. Add New Book")
            print("\t2. Update Existing Book")
            print("\t3. View Borrowed Books")
            print("\t4. View Borrow Requests")
            print("\t5. Log Out")
            choice = int(input("Enter choice: "))

            if choice == 1:
                add_new_book()
            elif choice == 2:
                update_book()
                print(library)
            elif choice == 3:
                library.display_borrow()
            elif choice == 4:
                library.borrow_request()
            elif choice == 5:
                print()
                break
            else:
                print("\nInvalid option")
        else:
            print(f"Incorrect Password. Try again. You have {2 - password_count} attempt(s) left")
            password_count += 1
            password = input("\nEnter password: ")


while True:
    print("BOLD STEP! KNOWLEDGE IS POWER...WELCOME")
    print("At Your Service, select an option,")
    print("\t1. Borrow Book")
    print("\t2. Find Book")
    print("\t3. View Books")
    print("\t4. Admin Login")
    choice = int(input("Enter choice: "))

    if choice == 1:
        book_operation(choice)
    elif choice == 2:
        book_operation(choice)
    elif choice == 3:
        print(library)
    elif choice == 4:
        admin_login()

