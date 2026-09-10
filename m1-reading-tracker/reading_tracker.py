class Book:
    def __init__(self, title, finished=False):
        self.title = title
        self.finished = finished

    def mark_finished(self):
        self.finished = True

class ReadingTracker:
    def __init__(self):
        self.books = []

    def add_book(self, title):
        book = Book(title)
        self.books.append(book)
        return book

    def is_empty(self):
        return len(self.books) == 0
    def mark_book_finished(self, index):
        if 0 <= index < len(self.books):
            self.books[index].mark_finished()
            return self.books[index]
        return None

# For the main program, start with this code: 

# print("Reading Tracker\n")
# books = []
# while True:
    
#     print("1. Add a book\n" +
#       "2. List books\n" +
#       "3. Mark a book as finished\n" +
#       "4. Quit")
#     option = input("Choose an option: ")
#     if option == "1":
#         enterBook = input("Book title: ")
#         books.append({"title": enterBook, "finished": False})
#         print(f'Added "{enterBook}".\n')
#     elif option == "2":
#         if not books:
#             print("No books in the list.")
#         else:
#             print("\nReading list")
#             for i, book in enumerate(books, start=1):
#                 status = "finished" if book["finished"] else "not finished"
#                 print(f'{i}. {book["title"]} — {status}')
#             print()
#     elif option == "3":
#         bookNumber = input("Book number: ")
#         bookNumber = int(bookNumber) - 1
#         if 0 <= bookNumber < len(books):
#             books[bookNumber]["finished"] = True
#             print(f'Marked "{books[bookNumber]["title"]}" as finished.')
#     elif option == "4":
#         print("Goodbye.")
#         break
#     else:
#         print("Invalid option. Select 1-3 or 4 to quit.\n")
