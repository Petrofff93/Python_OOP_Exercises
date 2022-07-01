class User:
    def __init__(self, user_id, username):
        self.user_id = user_id
        self.username = username
        self.books = []

    def info(self):
        books_str = f'{", ".join(sorted(self.books))}'
        return books_str

    def __str__(self):
        user_str = f'{self.user_id}, {self.username}, {self.books}'
        return user_str

