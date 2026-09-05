from reading_tracker import ReadingTracker


def main():
    tracker = ReadingTracker()
    print("Reading Tracker\n")

    while True:
        print("1. Add a book\n" +
              "2. List books\n" +
              "3. Update a book's status\n" +
              "4. Quit")
        
        option = input("Choose an option: ")

        if option == "1":
            title = input("Book title: ")
            tracker.add_book(title)
            print(f'Added "{title}" with status: to read.\n')

        elif option == "2":
            if tracker.is_empty():
                print("No books in the list.\n")
            else:
                print("\nReading list")
                for i, book in enumerate(tracker.books, start=1):
                    print(f'{i}. {book.title} — {book.status}')
                print()

                counts = tracker.get_status_counts()
                print("Status summary")
                print(f"to read: {counts['to read']}")
                print(f"reading: {counts['reading']}")
                print(f"finished: {counts['finished']}\n")

        elif option == "3":
            user_input = input("Book number: ")
            if user_input.isnumeric():
                index = int(user_input) - 1
                if 0 <= index < len(tracker.books):
                    new_status = input("New status (to read, reading, finished): ").strip().lower()
                    updated_book = tracker.update_book_status(index, new_status)
                    print(f'Updated "{updated_book.title}" to {new_status}.\n')
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