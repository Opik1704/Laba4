class Book:
    """
    Класс книга
    книга имеет Название Автора Год выпуска Жанр Isbn
    """
    def __init__(self, title, author, year, genre, isbn):
        """Конструктор книги"""
        self.title = title
        self.author = author
        self.year = year
        self.genre = genre
        self.isbn = isbn
    def __str__(self):
        """
        Строковое предстиавление книги
        :param self: книга
        """
        return f" \n\"{self.title}\" {self.author} ({self.year}) - {self.genre}, ISBN: {self.isbn}"
    def __add__(self, other):
        """Можно сделать собрание книг"""

        if self.author != other.author:
            print("Книги должны быть от 1 автора")
        else:
            new_title = f"Собрание книг : {self.author}"
            author = self.author
            new_isbn = f"-{self.isbn[-5:]}-{other.isbn[-5:]}"
        return Book(title =  new_title, author = author, genre = "Сборник", isbn = new_isbn,year = 2025)

    def __repr__(self):
        """Магический метод __repr__"""
        return f"Book('{self.title}', '{self.author}', {self.year}, '{self.genre}', '{self.isbn}')"