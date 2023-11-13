
class Book:
    def __init__(self, book_ISBN, title, author, category, condition, page_count, copies, location):
        self.book_ISBN = book_ISBN
        self.title = title
        self.author = author
        self.page_count = page_count
        self.condition = condition
        self.category = category
        self.copies = copies
        self.location = location
        self.borrow = 0

    def get_book_details(self):
        return [self.title, self.author, self.category, self.condition, self.page_count, self.copies, self.location, self]

    def __repr__(self):
        print("************ BOOK DETAILS **************")
        print("Title:      ", self.title)
        print("Author:     ", self.author)
        print("ISBN:       ", self.book_ISBN)
        print("Category:   ", self.category)
        print("Condition:  ", self.condition)
        print("Page count: ", self.page_count)
        print("Copies:     ", self.copies)
        print("Location:   ", self.location)

        return ""


class Library:
    def __init__(self, books):
        self.database = {}
        self.borrow_requests = []
        for book in books:
            self.database.setdefault(book.book_ISBN, book.get_book_details())

    def add_book(self, book):
        if self.check_ISBN(book.book_ISBN):
            self.database.setdefault(book.book_ISBN, book.get_book_details())

    def add_new_book(self, book):
        if self.check_ISBN(book.book_ISBN):
            self.database.setdefault(book.book_ISBN, book.get_book_details())
            print("\nBook has been added")
        else:
            print("\nBook already present!")

    def update_book(self, book_ISBN, book_copies):

        book_details = self.database.get(book_ISBN)
        book_details[7].copies += book_copies
        self.database[book_details[7].book_ISBN] = book_details[7].get_book_details()
        print(book_details[7].copies)
        if book_details[7].condition == "Borrowed":
            book_details[7].condition = "Available"
            self.database[book_details[7].book_ISBN] = book_details[7].get_book_details()

    def borrow_book(self, book_ISBN):

        book = self.search_by_ISBN(book_ISBN)

        if type(book) == str:
            return "\nOooops...Book isn't available"

        if book.copies <= 0:
            return f"\nAll copies of '{book.title}' are {book.condition}. Try again later!" \
                   f"\nDo you want to submit a request?(Y/N)"

        if book.copies > 0:
            book.copies -= 1
            book.borrow += 1
            self.database[book.book_ISBN] = book.get_book_details()

        if book.copies == 0:
            book.condition = "Borrowed"
            self.database[book.book_ISBN] = book.get_book_details()

        return f"\n'{book.title}' borrowed. Return in 2 days time"

    def search_by_ISBN(self, book_ISBN):
        book_details = self.database.get(book_ISBN)

        if book_details is None:
            return f"Oooops...Book isn't available"

        return book_details[7]

    def search_by_title_or_author(self, book_detail, choice):
        books = []

        for book_details in self.database.values():
            if choice == 2:
                if book_detail in book_details[0].lower():
                    books.append(book_details[7])
            else:
                if book_detail in book_details[1].lower():
                    books.append(book_details[7])

        if books == []:
            return f"Oooops...Book isn't available"

        return books


    def check_ISBN(self, book_ISBN):
        book_details = self.database.get(book_ISBN)

        if book_details == []:
            return False

        return True

    def display_borrow(self):
        print("-" * 100)
        print("Book ISBN", " " * 27, "Book Title", " " * 18, "Author", " " * 6, "Copies Borrowed")
        print("-" * 100)

        for book_ISBN, book_details in self.database.items():
            print(f"{book_ISBN:>15}", end=" ")
            for book_detail in book_details:
                if book_detail == book_details[2]:
                    print(f"{book_details[7].borrow:>20}")
                    break
                if book_detail == book_details[0]:
                    print(f"{book_detail:>30}", end=" ")
                elif book_detail == book_details[1]:
                    print(f"{book_detail:>25}", end=" ")
                else:
                    print(f"{book_detail:>15}", end=" ")

    def __repr__(self):
        print("-" * 157)
        print("Book ISBN", " " * 27, "Book Title", " " * 18, "Author", " " * 6, "Category", " " * 5,
              "Condition", " " * 4, "Page Count", " " * 8, "Copies", " " * 6, "Location ")
        print("-"*157)
        for book_ISBN, book_details in self.database.items():
            print(f"{book_ISBN:>15}", end=" ")
            for book_detail in book_details:
                if book_detail == book_details[7]:
                    break
                if book_detail == book_details[0]:
                    print(f"{book_detail:>30}", end=" ")
                elif book_detail == book_details[1]:
                    print(f"{book_detail:>25}", end=" ")
                else:
                    print(f"{book_detail:>15}", end=" ")
            print()

        return ""

    def request_book(self, book_isbn):
        self.borrow_requests.append(book_isbn)

    def borrow_request(self):
        if len(self.borrow_requests) == 0:
            print("\nNo borrow requests available")
            return
        print("\n        Book Title")
        for i in range(len(self.borrow_requests)):
            print(f"--<{i+1}>-- {self.database.get(self.borrow_requests[i])[0]}")
