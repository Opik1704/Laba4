class Book:
    def __init__(self, title, author, year, genre, isbn):
            self.title = title
            self.author = author
            self.year = year
            self.genre = genre
            self.isbn = isbn
    def __str__(self):
        """Cтроковое представление книги"""
        return f" \n\"{self.title}\" {self.author} ({self.year}) - {self.genre}, ISBN: {self.isbn}"
    def __add__(self, other):
        """
        Создание сборника книг от одного автора
        Возвращает новую книгу-сборник
        Использование: book1 + book2
        """
        if self.author != other.author:
            print("Книги должны быть от 1 автора")
        else:
            new_title = f"Собрание книг : {self.author}"
            author = self.author
            new_isbn = f"-{self.isbn[-5:]}-{other.isbn[-5:]}"
        return Book(title =  new_title, author = author, genre = "Сборник", isbn = new_isbn,year = 2025)

    def __repr__(self) -> str:
        """строковое представление объекта для воссоздания объекта"""
        return f"Book('{self.title}', '{self.author}', {self.year}, '{self.genre}', '{self.isbn}')"