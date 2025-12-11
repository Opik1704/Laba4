from Laba4.src.Book import Book
from Laba4.src.TextBook import TextBook
from Laba4.src.AudioBook import AudioBook

class BookCollection:
    def __init__(self, books_:list[Book] = None):
        if books_ is not None:
            self.books = books_
        else:
            self.books = []
    def __getitem__(self, item):
        if isinstance(item, slice):
            return BookCollection(self.books[item])
        return self.books[item]
    def __len__(self):
        return len(self.books)
    def __iter__(self):
        return iter(self.books)
    def __str__(self):
        if len(self.books) == 0:
            return "Коллекция книг пустая"
        books_str = "".join([f"{book}" for i, book in enumerate(self.books)])
        return f"Книги({len(self.books)}):\n{books_str}"

    def __contains__(self, item) -> bool:
        """
        Проверка наличия в коллекции.
        Поддерживает:
        - Проверку наличия книги (Book object)
        - Проверку наличия книги по ISBN (string)
        - Проверку наличия книг автора (string)
        """
        if isinstance(item, Book):
            return item in self.books
        elif isinstance(item, str):
            if any(book.isbn == item for book in self.books):
                return True
            return any(item.lower() in book.author.lower() for book in self.books)
        return False

    def __call__(self, filter_func=None, **kwargs):
        """
        Фильтрация коллекции по функции или критериям
        """
        if filter_func and callable(filter_func):
            return BookCollection([book for book in self.books if filter_func(book)])
        elif kwargs:
            filtered_books = []
            for book in self.books:
                match = True
                for key, value in kwargs.items():
                    if hasattr(book, key):
                        attr_value = getattr(book, key)
                        if isinstance(attr_value, str):
                            if value.lower() not in attr_value.lower():
                                match = False
                                break
                        elif attr_value != value:
                            match = False
                            break
                    else:
                        match = False
                        break
                if match:
                    filtered_books.append(book)
            return BookCollection(filtered_books)
        return BookCollection(self._books.copy())
    def __repr__(self) :
        """Cтроковое представление"""
        book_reprs = [repr(book) for book in self.books]
        return f"BookCollection([{', '.join(book_reprs)}])"
    def add_book(self, book):
        if book not in self.books:
            self.books.append(book)
        else:
            print(f"Такая книга с ISBN {book.isbn} уже есть в коллекции")
    def add_books(self, books:list[Book]):
        for book in books:
            self.add_book(book)
    def remove_book(self, book):
        if book in self.books:
            self.books.remove(book)
        else:
            print(f"Такой книги с ISBN {book.isbn} нет в коллекции")
    def remove_books_by_isbn(self, isbn: str):
        for book in self.books:
            if book.isbn == isbn:
                self.books.remove(book)
                return True
        print(f"Такой книги с ISBN {book.isbn} нет в коллекции")
        return False


