from reading_tracker import ReadingTracker


def main():
    tracker = ReadingTracker()
    print("Reading Tracker\n")

    while True:
        print("1. Add a book\n" +
              "2. List books\n" +
              "3. Mark a book as finished\n" +
              "4. Quit")
        
        option = input("Choose an option: ")

        if option == "1":
            title = input("Book title: ")
            tracker.add_book(title)
            print(f'Added "{title}".\n')

        elif option == "2":
            if tracker.is_empty():
                print("No books in the list.\n")
            else:
                print("\nReading list")
                for i, book in enumerate(tracker.books, start=1):
                    status = "finished" if book.finished else "not finished"
                    print(f'{i}. {book.title} — {status}')
                print()

        elif option == "3":
            user_input = input("Book number: ")
            if user_input.isnumeric():
                index = int(user_input) - 1
                updated_book = tracker.mark_book_finished(index)
                if updated_book:
                    print(f'Marked "{updated_book.title}" as finished.\n')
                else:
                    print("Invalid book number.\n")
            else:
                print("Please enter a valid number.\n")

        elif option == "4":
            print("Goodbye.")
            break

        else:
            print("Invalid option. Select 1-3 or 4 to quit.\n")


if __name__ == "__main__":
    main()