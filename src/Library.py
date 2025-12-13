from Laba4.src.Book import Book
from Laba4.src.AudioBook import AudioBook
from Laba4.src.TextBook import TextBook
from Laba4.src.IndexBookCollection import IndexBookCollection
from Laba4.src.BookCollection import BookCollection

class Library:
    """
    Класс библиотека
    Есть магиечские методы __init__,__len__,__iter__
    Вприницпе все отлично самочитается
    """
    def __init__(self, collection, index_dict):
        self.book_collection = BookCollection()
        self.indexed_collection = IndexBookCollection()
    def __len__(self) -> int:
        return len(self.book_collection)
    def __iter__(self):
        return iter(self.book_collection)
    def add_book(self, book):
        """
        Добавляет книжку
        :param book: книжка
        :return: False или True
        """
        if not isinstance(book, (Book, TextBook, AudioBook)):
            return False
        self.book_collection.add_book(book)
        self.indexed_collection.add_book(book)
        return book in self.book_collection and book.isbn in self.indexed_collection.isbn_index
    def add_books(self, books):
        """
        Добавление списка книжек
        :param books: список книжник
        :return:
        """
        for book in books:
            self.add_book(book)
    def remove_book(self, book):
        """
        удаление книжнки
        :param book: книжка
        :return: False или True
        """
        if not isinstance(book, (Book, TextBook, AudioBook)):
            print("Такой книги нет",book)
            return False
        self.book_collection.remove_book(book)
        self.indexed_collection.remove_book(book)
        return True
    def get_all_authors(self):
        """
        Получение всех авторов доступных в бидлиотеке
        :return: спиксок авторов
        """
        return list(self.indexed_collection.author_index.keys())
    def get_all_year(self):
        """
        Получение всех годов выпуска книжек доступных в бидлиотеке
        :return: спиксок годов
        """
        return list(self.indexed_collection.year_index.keys())
    def find_book_by_isbn(self,isbn):
        """
        Поиск по isbn
        :param isbn:
        """
        return self.indexed_collection.find_by_isbn(isbn)
    def find_books_by_year(self, year):
        """
        Поиск по году
        :param год:
        """
        return self.indexed_collection.find_by_year(year)
    def find_books_by_author(self, author):
        """
        Поиск по автору
        :param: автор
        """
        return self.indexed_collection.find_by_author(author)
    def find_book_by_title(self, title):
        """
        Поиск по заголовку
        :param: заголовок
        """
        for book in self.book_collection:
            if title == book.title:
                return book
        print("Такой книги нет")
        return False
    def find_books_by_genre(self, genre):
        """
        Поиск по жанру
        :param: жанр
        """
        books_by_genre = []
        for book in self.book_collection:
            if genre == book.genre:
                books_by_genre.append(book)
        return books_by_genre
    def get_all_books(self):
        """
        Получение всех книг
        :return: все книги
        """
        return self.book_collection.books.copy()
