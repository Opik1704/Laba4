from Laba4.src import Book
from typing import Dict, List
from Laba4.src.TextBook import TextBook
from Laba4.src.AudioBook import AudioBook

class IndexBookCollection:
    def __init__(self, books_:list[Book] = None):
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
            if author in self._author_index and year in self._year_index:
                author_books = set(self._author_index[author])
                year_books = set(self._year_index[year])
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
    def add_book_to_isbn_index(self, book):
        self.isbn_index[book.isbn] = book
    def add_book_to_author_index(self, book):
        self.author_index[book.author].append(book)
    def add_book_to_year_index(self, book):
        self.year_index[book.year].append(book)
    def add_book(self, book):
        self.books.append(book)
    def _add_to_indices(self, book):
        self.add_book_to_isbn_index(book)
        self.add_book_to_author_index(book)
        self.add_book_to_year_index(book)
    def remove_book(self, book):
        self.books.remove(book)
    def remove_author_index(self, book):
        for book.author in self.author_index:
            self.author_index[book.author].remove(book)
    def remove_year_index(self, book):
        for book.year in self.year_index:
            self.year_index[book.year].remove(book)
    def remove_book_by_isbn_index(self, book):
        for book.isbn in self.isbn_index:
            self.isbn_index[book.isbn].remove(book)
    def find_by_isbn(self, isbn):
        return self.isbn_index.get(isbn)
    def find_by_author(self, author):
        return self.author_index.get(author, []).copy()
    def find_by_year(self, year):
        return self.year_index.get(year, []).copy()
