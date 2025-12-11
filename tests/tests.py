import unittest
from Laba4.src.Library import Library
from Laba4.src.Book import Book
from Laba4.src.AudioBook import AudioBook
from Laba4.src.TextBook import TextBook
from Laba4.src.IndexBookCollection import IndexBookCollection
from Laba4.src.BookCollection import BookCollection


class TestBook(unittest.TestCase):
    def setUp(self):
        self.book1 = Book("Война и мир", "Лев Толстой", 1869, "Роман", "978-5-699-12014-7")
        self.book2 = Book("Преступление и наказание", "Фёдор Достоевский", 1866, "Роман", "978-5-17-090539-9")

    def test_book_creation(self):
        self.assertEqual(self.book1.title, "Война и мир")
        self.assertEqual(self.book1.author, "Лев Толстой")
        self.assertEqual(self.book1.year, 1869)
        self.assertEqual(self.book1.genre, "Роман")
        self.assertEqual(self.book1.isbn, "978-5-699-12014-7")

    def test_book_str(self):
        result = str(self.book1)
        self.assertIn("Война и мир", result)
        self.assertIn("Лев Толстой", result)
        self.assertIn("1869", result)
        self.assertIn("978-5-699-12014-7", result)

    def test_book_repr(self):
        result = repr(self.book1)
        self.assertIn("Book(", result)
        self.assertIn("'Война и мир'", result)

    def test_book_addition_same_author(self):
        book3 = Book("Анна Каренина", "Лев Толстой", 1877, "Роман", "978-5-389-12345-6")
        collection = self.book1 + book3
        self.assertEqual(collection.author, "Лев Толстой")
        self.assertEqual(collection.genre, "Сборник")


class TestAudioBook(unittest.TestCase):
    def setUp(self):
        self.audiobook = AudioBook(
            "1984", "Джордж Оруэлл", 1949, "Антиутопия",
            "978-5-17-090987-8", "Иван Петров", 720, "русский"
        )

    def test_audiobook_creation(self):
        self.assertEqual(self.audiobook.title, "1984")
        self.assertEqual(self.audiobook.narrator, "Иван Петров")
        self.assertEqual(self.audiobook.minutes, 720)
        self.assertEqual(self.audiobook.language, "русский")

    def test_audiobook_str(self):
        result = str(self.audiobook)
        self.assertIn("1984", result)
        self.assertIn("Джордж Оруэлл", result)
        self.assertIn("Читает: Иван Петров", result)

    def test_set_playback_position(self):
        self.assertTrue(self.audiobook.set_playback_position(100))
        self.assertEqual(self.audiobook.last_position, 100)

        # За пределами допустимого диапазона
        self.assertFalse(self.audiobook.set_playback_position(800))
        self.assertFalse(self.audiobook.set_playback_position(-10))

    def test_set_playback_speed(self):
        self.audiobook.set_playback_speed(1.5)
        self.assertEqual(self.audiobook.playback_speed, 1.5)


class TestTextBook(unittest.TestCase):
    def setUp(self):
        self.textbook = TextBook(
            "Алгебра", "Иванов И.И.", 2020, "Учебник",
            "978-5-09-071234-5", "Математика", 9, "Просвещение"
        )

    def test_textbook_creation(self):
        self.assertEqual(self.textbook.title, "Алгебра")
        self.assertEqual(self.textbook.subject, "Математика")
        self.assertEqual(self.textbook.grade_level, 9)
        self.assertEqual(self.textbook.publisher, "Просвещение")

    def test_textbook_str(self):
        result = str(self.textbook)
        self.assertIn("Алгебра", result)
        self.assertIn("Предмет: Математика", result)
        self.assertIn("Класс: 9", result)
        self.assertIn("Издaтельство: Просвещение", result)


class TestBookCollection(unittest.TestCase):
    def setUp(self):
        self.book1 = Book("Книга 1", "Автор 1", 2000, "Фантастика", "111")
        self.book2 = Book("Книга 2", "Автор 2", 2001, "Детектив", "222")
        self.collection = BookCollection([self.book1, self.book2])

    def test_collection_creation(self):
        self.assertEqual(len(self.collection), 2)

    def test_add_book(self):
        book3 = Book("Книга 3", "Автор 3", 2002, "Роман", "333")
        self.collection.add_book(book3)
        self.assertEqual(len(self.collection), 3)
        self.assertIn(book3, self.collection.books)

    def test_remove_book(self):
        self.collection.remove_book(self.book1)
        self.assertEqual(len(self.collection), 1)
        self.assertNotIn(self.book1, self.collection.books)

    def test_remove_book_by_isbn(self):
        self.collection.remove_books_by_isbn("111")
        self.assertEqual(len(self.collection), 1)
        self.assertNotIn(self.book1, self.collection.books)

    def test_contains_by_isbn(self):
        self.assertIn("111", self.collection)
        self.assertNotIn("999", self.collection)

    def test_contains_by_book(self):
        self.assertIn(self.book1, self.collection)

        book3 = Book("Другая книга", "Автор", 2000, "Жанр", "999")
        self.assertNotIn(book3, self.collection)

    def test_getitem(self):
        self.assertEqual(self.collection[0], self.book1)

        # Тестирование среза
        slice_result = self.collection[0:1]
        self.assertIsInstance(slice_result, BookCollection)
        self.assertEqual(len(slice_result), 1)

    def test_iteration(self):
        books = []
        for book in self.collection:
            books.append(book)
        self.assertEqual(len(books), 2)
        self.assertIn(self.book1, books)

    def test_call_with_filter(self):
        filtered = self.collection(author="Автор 1")
        self.assertEqual(len(filtered), 1)
        self.assertEqual(filtered[0], self.book1)


class TestIndexBookCollection(unittest.TestCase):
    def setUp(self):
        self.book1 = Book("Книга A", "Автор A", 2000, "Фантастика", "111")
        self.book2 = Book("Книга B", "Автор B", 2000, "Детектив", "222")
        self.book3 = Book("Книга C", "Автор A", 2001, "Роман", "333")
        self.indexed = IndexBookCollection([self.book1, self.book2, self.book3])

    def test_index_creation(self):
        self.assertEqual(len(self.indexed.books), 3)
        self.assertEqual(len(self.indexed.isbn_index), 3)
        self.assertEqual(len(self.indexed.author_index), 2)  # 2 уникальных автора
        self.assertEqual(len(self.indexed.year_index), 2)  # 2 уникальных года

    def test_find_by_isbn(self):
        result = self.indexed.find_by_isbn("111")
        self.assertEqual(result, self.book1)

        result = self.indexed.find_by_isbn("999")
        self.assertIsNone(result)

    def test_find_by_author(self):
        result = self.indexed.find_by_author("Автор A")
        self.assertEqual(len(result), 2)
        self.assertIn(self.book1, result)
        self.assertIn(self.book3, result)

    def test_find_by_year(self):
        result = self.indexed.find_by_year(2000)
        self.assertEqual(len(result), 2)
        self.assertIn(self.book1, result)
        self.assertIn(self.book2, result)

    def test_contains_by_isbn(self):
        self.assertIn("111", self.indexed)
        self.assertIn(self.book1, self.indexed)
        self.assertNotIn("999", self.indexed)

    def test_add_book(self):
        book4 = Book("Книга D", "Автор C", 2002, "Фантастика", "444")
        self.indexed.add_book(book4)

        self.assertEqual(len(self.indexed.books), 4)
        self.assertIn("444", self.indexed.isbn_index)
        self.assertIn("Автор C", self.indexed.author_index)
        self.assertIn(2002, self.indexed.year_index)

    def test_remove_book(self):
        self.indexed.remove_book(self.book1)

        self.assertEqual(len(self.indexed.books), 2)
        self.assertNotIn("111", self.indexed.isbn_index)
        self.assertNotIn(self.book1, self.indexed.author_index.get("Автор A", []))

    def test_call_method(self):
        result = self.indexed(author="Автор A")
        self.assertEqual(len(result.books), 2)
        result = self.indexed(year=2000)
        self.assertEqual(len(result.books), 2)
        result = self.indexed(sort_by='title')
        self.assertEqual(result.books[0].title, "Книга A")


class TestLibrary(unittest.TestCase):
    def setUp(self):
        self.library = Library(collection=None, index_dict=None)
        self.book1 = Book("Книга 1", "Автор 1", 2000, "Фантастика", "111")
        self.book2 = Book("Книга 2", "Автор 2", 2001, "Детектив", "222")
        self.audiobook = AudioBook(
            "Аудиокнига", "Автор 3", 2020, "Роман",
            "333", "Чтец", 300, "русский"
        )

    def test_add_book(self):
        result = self.library.add_book(self.book1)
        self.assertTrue(result)
        self.assertEqual(len(self.library), 1)

        # Проверяем, что книга есть в обеих коллекциях
        self.assertIn(self.book1, self.library.book_collection)
        self.assertIn("111", self.library.indexed_collection.isbn_index)

    def test_add_multiple_books(self):
        books = [self.book1, self.book2]
        self.library.add_books(books)
        self.assertEqual(len(self.library), 2)

    def test_add_invalid_book(self):
        result = self.library.add_book("не книга")
        self.assertFalse(result)
        self.assertEqual(len(self.library), 0)

    def test_add_audiobook(self):
        result = self.library.add_book(self.audiobook)
        self.assertTrue(result)
        self.assertEqual(len(self.library), 1)

    def test_remove_book(self):
        self.library.add_book(self.book1)
        result = self.library.remove_book(self.book1)
        self.assertTrue(result)
        self.assertEqual(len(self.library), 0)

    def test_find_book_by_isbn(self):
        self.library.add_book(self.book1)
        result = self.library.find_book_by_isbn("111")
        self.assertEqual(result, self.book1)

        result = self.library.find_book_by_isbn("999")
        self.assertIsNone(result)

    def test_find_books_by_author(self):
        self.library.add_books([self.book1, self.book2])
        result = self.library.find_books_by_author("Автор 1")
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0], self.book1)

    def test_find_books_by_year(self):
        self.library.add_books([self.book1, self.book2])
        result = self.library.find_books_by_year(2000)
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0], self.book1)

    def test_find_book_by_title(self):
        self.library.add_book(self.book1)
        result = self.library.find_book_by_title("Книга 1")
        self.assertEqual(result, self.book1)

        result = self.library.find_book_by_title("Несуществующая")
        self.assertIsNone(result)

    def test_find_books_by_genre(self):
        self.library.add_books([self.book1, self.book2])
        result = self.library.find_books_by_genre("Фантастика")
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0], self.book1)

    def test_get_all_books(self):
        self.library.add_books([self.book1, self.book2])
        all_books = self.library.get_all_books()
        self.assertEqual(len(all_books), 2)
        self.assertIn(self.book1, all_books)
        self.assertIn(self.book2, all_books)

    def test_iteration(self):
        self.library.add_books([self.book1, self.book2])
        books = []
        for book in self.library:
            books.append(book)
        self.assertEqual(len(books), 2)

    def test_remove_by_isbn(self):
        self.library.add_book(self.book1)
        self.library.remove_by_isbn("111")
        self.assertEqual(len(self.library), 0)
        self.assertIsNone(self.library.find_book_by_isbn("111"))


def run_tests():
    # Создаем тестовый набор
    test_suite = unittest.TestSuite()

    # Добавляем тесты
    test_suite.addTest(unittest.makeSuite(TestBook))
    test_suite.addTest(unittest.makeSuite(TestAudioBook))
    test_suite.addTest(unittest.makeSuite(TestTextBook))
    test_suite.addTest(unittest.makeSuite(TestBookCollection))
    test_suite.addTest(unittest.makeSuite(TestIndexBookCollection))
    test_suite.addTest(unittest.makeSuite(TestLibrary))

    # Запускаем тесты
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(test_suite)

    return result


if __name__ == "__main__":
    run_tests()