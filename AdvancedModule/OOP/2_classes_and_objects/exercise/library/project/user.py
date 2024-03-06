class User:

    def __init__(self, user_id, username):
        self.user_id = user_id
        self.username = username
        self.books = []

    def info(self):
        return ', '.join(book for book in sorted(self.books)) or '[]'

    def __str__(self):
        return f"{self.user_id}, {self.username}, {self.info()}"
