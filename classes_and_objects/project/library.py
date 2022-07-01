from project.user import User


class Library:
    def __init__(self):
        self.user_records = []  # empty list that stores the user objects for the library
        self.books_available = {}  # dict that stores authors(keys) and available books as a list of strings
        self.rented_books = {}  # nested dict that stores usernames(keys) and book names: days to return

    def get_book(self, author, book_name, days_to_return, user: User):
        for auth, books in self.books_available.items():
            if book_name in books:
                user.books.append(book_name)
                self.rented_books[user.username] = {book_name: days_to_return}
                self.books_available[author].remove(book_name)
                return f"{book_name} successfully rented for the next {days_to_return} days!"

        for user_name, book in self.rented_books.items():
            if book_name in book:
                return f'The book "{book_name}" is already rented and will be available in {self.rented_books[user_name][book_name]} days!'

    def return_book(self, author, book_name, user: User):
        if book_name in user.books:
            self.books_available[author].append(book_name)
            del self.rented_books[user.username][book_name]
            user.books.remove(book_name)
        else:
            return f"{user.username} doesn't have this book in his/her records!"




