from typing import Dict, List
from Laba4.src.Book import Book
from Laba4.src.TextBook import TextBook
from Laba4.src.AudioBook import AudioBook

class IndexBookCollection:
    """Класс IndexBookCollection """
    def __init__(self, books_:list[Book] = None):
        """Инициализция"""
        self.books: List[Book] = []
        self.isbn_index: Dict[str, Book] = {}
        self.author_index: Dict[str, List[Book]] = {}
        self.year_index: Dict[int, List[Book]] = {}
        if books_ is not None:
            for book in books_:
                self.add_book(book)
    def __contains__(self, item) :
        """
        Проверка наличия с использованием индексов
        """
        if isinstance(item, Book):
            return item.isbn in self.isbn_index
        elif isinstance(item, str):
            return item in self.isbn_index
        elif isinstance(item, tuple) and len(item) == 2:
            author, year = item
            if author in self.author_index and year in self.year_index:
                author_books = set(self.author_index[author])
                year_books = set(self.year_index[year])
                return bool(author_books.intersection(year_books))
        return False
    def __call__(self, **params):
        """
        Поиск книги по параметру
        """
        result = self.books.copy()
        if 'author' in params:
            author_books = self.author_index.get(params['author'], [])
            result = [book for book in result if book in author_books]
        if 'year' in params:
            year_books = self.year_index.get(params['year'], [])
            result = [book for book in result if book in year_books]
        if 'genre' in params:
            genre = params['genre'].lower()
            result = [book for book in result if genre in book.genre.lower()]
        if 'title' in params:
            title_part = params['title'].lower()
            result = [book for book in result if title_part in book.title.lower()]
        if 'sort_by' in params:
            sort_field = params['sort_by']
            reverse = params.get('reverse', False)
            if sort_field == 'year':
                result.sort(key=lambda x: x.year, reverse=reverse)
            elif sort_field == 'title':
                result.sort(key=lambda x: x.title.lower(), reverse=reverse)
            elif sort_field == 'author':
                result.sort(key=lambda x: x.author.lower(), reverse=reverse)
        return IndexBookCollection(result)
    def __repr__(self):
        """Cтроковое представление"""
        stats = f"books={len(self.books)}, authors={len(self.author_index)}, years={len(self.year_index)}"
        return f"IndexedBookCollection({stats})"
    def get_all_authors(self):
        """Получение всех авторов"""
        return list(self.author_index.keys())
    def get_years(self):
        """Получение всех годов"""
        return list(self.year_index.keys())
    def add_book_to_isbn_index(self, book):
        """Добавление книги в isbn index"""
        self.isbn_index[book.isbn] = book
    def add_book_to_author_index(self, book):
        """Добавление книги в авторский index"""
        if book.author not in self.author_index:
            self.author_index[book.author] = []
        self.author_index[book.author].append(book)
    def add_book_to_year_index(self, book):
        """Добавление книги в year index"""
        if book.year not in self.year_index:
            self.year_index[book.year] = []
        self.year_index[book.year].append(book)
    def add_book(self, book):
        """Добавление книги book"""
        if book.isbn in self.isbn_index:
            print(f"Книга с ISBN {book.isbn} уже существует")
            return False
        self.books.append(book)
        self.add_to_indices(book)
        return True
    def add_to_indices(self, book):
        """Добавление во всез индексы"""
        self.add_book_to_isbn_index(book)
        self.add_book_to_author_index(book)
        self.add_book_to_year_index(book)
    def remove_from_indices(self, book):
        """Добавление из всех индексов"""
        if book.isbn in self.isbn_index:
            del self.isbn_index[book.isbn]
        if book.author in self.author_index:
            author_books = self.author_index[book.author]
            if book in author_books:
                author_books.remove(book)
            if not author_books:
                del self.author_index[book.author]
        if book.year in self.year_index:
            year_books = self.year_index[book.year]
            if book in year_books:
                year_books.remove(book)
            if not year_books:
                del self.year_index[book.year]
    def remove_book(self, book):
        """Удаление книши"""
        if book in self.books:
            self.books.remove(book)
            self.remove_from_indices(book)
            return True
        return False
    def find_by_isbn(self, isbn):
        """Поиск по isbn"""
        if self.isbn_index.get(isbn):
            return self.isbn_index.get(isbn)
        else:
            print("Такой книги нет")
            return False
    def find_by_author(self, author):
        """Поиск по автору"""
        if self.author_index.get(author):
            return self.author_index.get(author, []).copy()
        else:
            print("Такого автора нет")
            return False
    def find_by_year(self, year):
        """Поиск по году"""
        if self.year_index.get(year):
            return self.year_index.get(year, []).copy()
        else:
            print("Книг такого года нет")
            return False
