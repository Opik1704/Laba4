from Laba4.src.Book import Book

class TextBook(Book):
    """Класс Учебник наследуется от книги, добавляется Предмет Класс учебника Издательство"""
    def __init__(self, title, author, year, genre, isbn, subject, grade_level, publisher):
        """Инициаилизация с наследованием от Book"""
        super().__init__(title, author, year, genre, isbn)
        self.subject = subject
        self.grade_level = grade_level
        self.publisher = publisher
    def __str__(self):
        """Строковое представление"""
        base_info = super().__str__()
        return f"{base_info}\n  '{self.subject}','{self.grade_level}','{self.publisher}'"
