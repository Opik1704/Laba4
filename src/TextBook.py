from Laba4.src.Book import Book

class TextBook(Book):
    def __init__(self, title, author, year, genre, isbn, subject, grade_level, publisher):
        super().__init__(title, author, year, genre, isbn)
        self.subject = subject
        self.grade_level = grade_level
        self.publisher = publisher
    def __str__(self):
        base_info = super().__str__()
        return f"{base_info}\n  Предмет: {self.subject}, Класс: {self.grade_level}, Издaтельство: {self.publisher}"
