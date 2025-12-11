from Laba4.src.Book import Book
from Laba4.src.AudioBook import AudioBook
from Laba4.src.TextBook import TextBook
from Laba4.src.IndexBookCollection import IndexBookCollection
from Laba4.src.BookCollection import BookCollection

class Library:
    def __init__(self, collection, index_dict):
        self.book_collection = BookCollection()
        self.indexed_collection = IndexBookCollection()

    def add_book(self, book):
        if not isinstance(book, (Book, TextBook, AudioBook)):
            return False
        self.book_collection.add_book(book)
        self.indexed_collection.add_book(book)
        return book in self.book_collection and book.isbn in self.indexed_collection.isbn_index

    def add_books(self, books):
        for book in books:
            self.add_book(book)

    def remove_book(self, book):
        if not isinstance(book, (Book, TextBook, AudioBook)):
            return False
        self.book_collection.remove_book(book)
        self.indexed_collection.remove_book(book)
        return True
    def remove_by_isbn(self, isbn: str):
        self.indexed_collection.remove_book_by_isbn_index(isbn)

    def find_book_by_isbn(self,isbn):
        return self.indexed_collection.find_by_isbn(isbn)
    def find_books_by_year(self, year):
        return self.indexed_collection.find_by_year(year)
    def find_books_by_author(self, author):
        return self.indexed_collection.find_by_author(author)
    def find_book_by_title(self, title):
        for book in self.book_collection:
            if title == book.title:
                return book
    def find_books_by_genre(self, genre):
        books_by_genre = []
        for book in self.book_collection:
            if genre == book.genre:
                books_by_genre.append(book)
        return books_by_genre
    def get_all_books(self):
        return self.book_collection.books.copy()
    def __len__(self) -> int:
        return len(self.book_collection)
    def __iter__(self):
        return iter(self.book_collection)