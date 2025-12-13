import unittest
from Laba4.src.Book import Book
from Laba4.src.AudioBook import AudioBook
from Laba4.src.TextBook import TextBook
from Laba4.src.BookCollection import BookCollection
from Laba4.src.IndexBookCollection import IndexBookCollection
from Laba4.src.Library import Library


class TestBook(unittest.TestCase):
    """Тестирование книги"""
    def test_book_creation(self):
        book = Book("1984", "Джордж Оруэлл", 1949, "Антиутопия", "1")
        self.assertEqual(book.title, "1984")
        self.assertEqual(book.author, "Джордж Оруэлл")
        self.assertEqual(book.year, 1949)
        self.assertEqual(book.genre, "Антиутопия")
        self.assertEqual(book.isbn, "1")

class TestAudioBook(unittest.TestCase):
    """Тестирование АУдиокниги"""
    def test_audiobook_creation(self):
        audiobook = AudioBook("Мастер и Маргарита", "Михаил Булгаков", 1967,"Роман", "2", "Вячеслав Герасимов", 1320, "русский")
        self.assertEqual(audiobook.narrator, "Вячеслав Герасимов")
        self.assertEqual(audiobook.minutes, 1320)
        self.assertEqual(audiobook.language, "русский")
        self.assertEqual(audiobook.playback_speed, 1.0)

    def test_audiobook_methods(self):
        """Тестирование методов аудиокниги"""
        audiobook = AudioBook("Книга", "Автор", 2023, "Жанр", "3", "Чтец", 100, "рус")
        audiobook.set_playback_position(50)
        self.assertEqual(audiobook.last_position, 50)
        audiobook.set_playback_speed(1.5)
        self.assertEqual(audiobook.playback_speed, 1.5)

class TestTextBook(unittest.TestCase):
    """Тестирование учебника"""
    def test_textbook_creation(self):
        textbook = TextBook("Алгебра", "Виленкин.", 2020, "Учебник", "4","Математика", "10 класс", "Просвещение")
        self.assertEqual(textbook.subject, "Математика")
        self.assertEqual(textbook.grade_level, "10 класс")
        self.assertEqual(textbook.publisher, "Просвещение")

class TestBookCollection(unittest.TestCase):
    """Тестирование BookCollection"""

    def test_add_book(self):
        """Тестирование добавления 1 книги"""
        collection = BookCollection()
        book = Book("книга", "автор", 2023, "жанр", "1")
        collection.add_book(book)
        self.assertEqual(len(collection), 1)

    def test_add_books(self):
        """Тестирование добавления нескольких книг"""
        collection = BookCollection()
        books = [Book("книга 1", "автор 1", 2023, "жанр 1", "1"), Book("книга 2", "автор 2", 2023, "жанр 2", "2")]
        collection.add_books(books)
        self.assertEqual(len(collection), 2)

    def test_remove_book(self):
        """Тестирование удаления 1 книги"""
        collection = BookCollection()
        book = Book("книга", "автор", 2023, "жанр", "1")
        collection.add_book(book)
        collection.remove_book(book)
        self.assertEqual(len(collection), 0)

class TestIndexBookCollection(unittest.TestCase):
    """Тесты IndexBookCollection"""
    def setUp(self):
        """Создание нескольких книг Подготовка"""
        self.book1 = Book("Властелин колец", "Джон Толкин", 1954, "Роман", "1")
        self.book2 = Book("Скотный двор", "Джордж Оруэлл", 1945, "Сатира", "2")
        self.book3 = Book("Война и мир", "Лев Толстой", 1869, "Роман", "3")

    def test_add_book(self):
        """Тест добавления книги"""
        collection = IndexBookCollection([self.book1])
        collection.add_book(self.book2)
        self.assertEqual(len(collection.books), 2)

    def test_remove_book(self):
        """Тест удаления книги"""
        collection = IndexBookCollection([self.book1, self.book2])
        collection.remove_book(self.book1)
        self.assertEqual(len(collection.books), 1)

    def test_creation_with_books(self):
        """Тест создание коллекции с несколькими книгами"""
        collection = IndexBookCollection([self.book1, self.book2])
        self.assertEqual(len(collection.books), 2)

    def test_find_by_isbn(self):
        """Поиск по isbn"""
        collection = IndexBookCollection([self.book1, self.book2])
        found = collection.find_by_isbn("1")
        self.assertEqual(found, self.book1)

    def test_find_fake_by_isbn(self):
        """Поиск несущ книги по isbn"""

        collection = IndexBookCollection([self.book1, self.book2])
        found = collection.find_by_isbn("-1")
        self.assertEqual(False,found)

    def test_find_by_author(self):
        """Поиск по автору"""
        collection = IndexBookCollection([self.book1, self.book2, self.book3])
        books = collection.find_by_author("Джон Толкин")
        self.assertEqual(len(books), 1)

    def test_find_by_fake_author(self):
        """Поиск по несущетсвующему автору"""
        collection = IndexBookCollection([self.book1, self.book2])
        books = collection.find_by_author("Фикалис Антон Павлович")
        self.assertEqual(False, books)

    def test_find_by_year(self):
        """Поиск по году"""
        collection = IndexBookCollection([self.book1, self.book2, self.book3])
        books = collection.find_by_year(1945)
        self.assertEqual(len(books), 1)

class TestLibrary(unittest.TestCase):
    """Тесты библиоткеи"""
    def setUp(self):
        """Подготовка"""
        self.library = Library(BookCollection(), IndexBookCollection())
        self.book1 = Book("1984", "Джордж Оруэлл", 1949, "Антиутопия", "1")
        self.book2 = Book("Властелин колец", "Джон Толкин", 1954, "Роман", "2")
        self.book3 = Book("Война и мир", "Лев Толстой", 1869, "Роман", "3")
        self.audiobook = AudioBook("Аудио", "Автор", 2023, "Жанр", "4", "Чтец", 300, "рус")
        self.textbook = TextBook("Учебник", "Автор", 2023, "Учебник", "5", "Математика", "10 класс", "Издательство")

    def test_add_book(self):
        """Добавление 1 книги"""
        result = self.library.add_book(self.book1)
        self.assertTrue(result)
        self.assertEqual(len(self.library), 1)

    def test_add_books(self):
        """Добавление нескольких книг"""
        self.library.add_books([self.book1, self.book2])
        self.assertEqual(len(self.library), 2)

    def test_find_book_by_isbn(self):
        """Поиск по isbn """
        self.library.add_book(self.book1)
        found = self.library.find_book_by_isbn("1")
        self.assertEqual(found, self.book1)

    def test_find_fake_book_by_isbn(self):
        """Поиск несущ книги по isbn"""
        found = self.library.find_book_by_isbn("-1")
        self.assertEqual(False, found)

    def test_find_books_by_author(self):
        """Поиск по автору"""
        self.library.add_books([self.book1, self.book2])
        books = self.library.find_books_by_author("Джордж Оруэлл")
        self.assertEqual(len(books), 1)

    def test_find_books_by_fake_author(self):
        """Поиск по несущетсвующему автору"""
        books = self.library.find_books_by_author("Шмурдяк")
        self.assertEqual(False, books)

    def test_find_books_by_year(self):
        """Поиск по году"""

        self.library.add_book(self.book1)
        books = self.library.find_books_by_year(1949)
        self.assertEqual(len(books), 1)

    def test_find_books_by_genre(self):
        """Поиск по жанру"""

        self.library.add_book(self.book1)
        books = self.library.find_books_by_genre("Антиутопия")
        self.assertEqual(len(books), 1)

    def test_remove_book(self):
        """Тест удаления книги"""

        self.library.add_book(self.book1)
        self.library.remove_book(self.book1)
        self.assertEqual(len(self.library), 0)

    def test_get_all_books(self):
        """Тест получения всех книг"""
        self.library.add_books([self.book1, self.book2])
        all_books = self.library.get_all_books()
        self.assertEqual(len(all_books), 2)

    def test_add_all_book_types(self):
        """Тест добавления всех типов книг"""

        self.library.add_book(self.book1)
        self.library.add_book(self.audiobook)
        self.library.add_book(self.textbook)
        self.assertEqual(len(self.library), 3)
if __name__ == '__main__':
    unittest.main()