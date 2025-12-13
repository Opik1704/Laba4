import random
import time

from Laba4.src.Book import Book
from Laba4.src.TextBook import TextBook
from Laba4.src.AudioBook import AudioBook
from Laba4.src.BookCollection import BookCollection
from Laba4.src.IndexBookCollection import IndexBookCollection
from Laba4.src.Library import Library


def run_simulation(steps=15, seed=None):
    """
    Симуляция работы библиотеки
    :param steps: количество шагов
    :param seed: при заданном seed генерирует идентичную последовательность событий
    """
    if seed is not None:
        random.seed(seed)
    else:
        random.seed(int(time.time()))
    print(seed, steps)
    library = Library(BookCollection(), IndexBookCollection())
    books = [
        Book("1984", "Джордж Оруэлл", 1949, "Антиутопия", "1"),
        Book("Скотный двор", "Джордж Оруэлл", 1945, "Сатира", "2"),
        Book("Война и мир", "Лев Толстой", 1869, "Роман", "3"),
        AudioBook("Мастер и Маргарита", "Михаил Булгаков", 1967, "Роман",
                  "4", "Вячеслав Герасимов", 1320, "русский"),
        TextBook("Алгебра", "Иванов И.И.", 2020, "Учебник", "5",
                 "Математика", "10 класс", "Просвещение"),
    ]
    for book in books:
        library.add_book(book)
    print("Всего книг", len(library))
    for step in range(steps):
        print("\nШаг",step + 1)
        action = random.choice([
            "add_book",
            "add_books",
            "remove_book",
            "find_by_isbn",
            "find_by_year",
            "find_by_author",
            "find_by_title",
            "find_by_genre",
            "get_all_books",
            "find_fake_isbn",
            "remove_fake_isbn",
        ])
        if action == "add_book":
            add_book(library, step)
        elif action == "add_books":
            add_books(library, step)
        elif action == "remove_book":
            remove_book(library)
        elif action == "find_by_isbn":
            find_by_isbn(library)
        elif action == "find_by_year":
            find_by_year(library)
        elif action == "find_by_author":
            find_by_author(library)
        elif action == "find_by_title":
            find_by_title(library)
        elif action == "find_by_genre":
            find_by_genre(library)
        elif action == "get_all_books":
            get_all_books(library)
        elif action == "find_fake_isbn":
            find_fake_isbn(library)
        elif action == "remove_fake_isbn":
            remove_fake_book_by_isbn(library)
        time.sleep(0.7)
    libraly_stats(library)

def add_book(library, step):
    """
    Добавление 1 книги в библиотеку
    Получает библиотеку в которуб надо добавить и шаг
    """
    book_type = random.choice(["book", "audiobook", "textbook"])
    if book_type == "book":
        new_book = Book(f"Книга {step} ",f"Автор {random.randint(1, 20)}", 2000 + random.randint(0, 25),
            random.choice(["Роман", "Детектив","Фантастика"]),f"isbn{random.randint(100, 999)}")
    elif book_type == "audiobook":
        new_book = AudioBook(f"Аудиокнига {step}",f"Автор{random.randint(1, 20)}", 2000 + random.randint(0, 25),
            random.choice(["Роман", "Детектив","Фантастика"]),f"audio{random.randint(100, 999)}",
            f"Чтец{random.randint(1, 20)}",random.randint(300, 600),"Русский" )
    else:
        new_book = TextBook(f"Учебник{step}",f"Автор{random.randint(1, 20)}",2010 + random.randint(0, 15),"Учебник",
            f"textbook{random.randint(100, 999)}",random.choice(["Математика", "Физика","Русский язык"]),
            f"{random.randint(5, 11)} класс","Просвещение")
    result = library.add_book(new_book)
    print(f"Добавлена книга {new_book.title} с типом книги: {book_type}")

def add_books(library, step):
    """
    Добавляет несколько книг в библиотеку
    :param library: библиотека
    :param step: шаг
    :return: Ничего
    """
    new_books = [
        Book(f"Добавленная {step} ", f"Автор {step}", random.randint(2000,2025), "Роман", f"addbook{step} 1"),
        Book(f"Добавленная {step + 1} ", f"Автор {step + 1}", random.randint(2000,2025), "Детектив", f"addbook{step} 2")
    ]
    library.add_books(new_books)
    print(f"Добавлено {len(new_books)} книг")
    print("Количество книг", len(library))

def remove_book(library):
    """
    Удаляет книгу
    :param library: из библиотеки данной
    :return:
    """
    all_books = library.get_all_books()
    if not all_books:
        print("Нет книг для удаления")
        return False
    book = random.choice(all_books)
    library.remove_book(book)
    print("Удаление книги",book.title)
    print("Осталось книг",len(library))
    return True

def remove_fake_book_by_isbn(library):
    """
    Пытается удалить несуществующую книгу
    :param library: из библиотеки
    """
    fake_book = Book("ЖмышенкоВалерий", "Пенис Детров", 1954, "Комедия", "1448228"),
    library.remove_book(fake_book)

def find_by_isbn(library):
    """
    Поиск книг по isbn
    :param library: в библиотеки
    :return: True если нашли и False если нет
    """
    all_books = library.get_all_books()
    if not all_books:
        print("Нет книг для поиска")
        return False
    book = random.choice(all_books)
    found = library.find_book_by_isbn(book.isbn)
    print(f"Книга по ISBN найдена", found.title,book.isbn)
    return True

def find_fake_isbn(library):
    """
    Поиск несуществующей  книге по isbn
    :param library: в библиотеки
    :return: True если нашли и False если нет
    """
    fake_isbn = -1000
    print("fake_isbn", fake_isbn)
    all_books = library.get_all_books()
    found = library.find_book_by_isbn(fake_isbn)
def find_by_year(library):
    """
    Поиск книг по году
    :param library: в библиотеке
    """
    years = library.get_all_year()
    year = random.choice(years)

    books = library.find_books_by_year(year)
    print("Поиск книг вышедших года ", year)
    print("Книг найдено", len(books))
    for book in books:
        print(book.title)

def find_by_author(library):
    """
    Поиск книг по автору
    :param library: в библиотеке
    """
    authors = library.get_all_authors()
    author = random.choice(authors)

    books = library.find_books_by_author(author)
    print("Поиск книг автора", author)
    print("Книг найдено", len(books))
    for book in books:
        print(book.title)

def find_by_title(library):
    """
    Поиск книг по названию
    :param library: в библиотеке
    """
    all_books = library.get_all_books()
    if not all_books:
        print("Нет книг для поиска")
        return
    book = random.choice(all_books)
    found = library.find_book_by_title(book.title)
    if found:
        print("Поиск книг с названием", book.title)
        print("Найдено")
    else:
        print("Поиск книг с названием", book.title)
        print("Не найдено")

def find_by_genre(library):
    """
    Поиск книг по жанру
    :param library: в библиотеке
    """
    genres = ["Антиутопия", "Сатира", "Роман", "Учебник"]
    genre = random.choice(genres)

    books = library.find_books_by_genre(genre)
    print("Поиск книг по жанру", genre)
    print("Книг найдено", len(books))
    for book in books:
        print(book.title)
def get_all_books(library):
    """
    Получение всех книг
    :param library: в библиотеке
    :return:
    """
    all_books = library.get_all_books()
    print(f"Всего в библиотеке {len(all_books)} книг c типами")
    book_types = {}
    for book in all_books:
        book_type = type(book).__name__
        book_types[book_type] = book_types.get(book_type, 0) + 1
    for book_type, count in book_types.items():
        print(f"{book_type}: {count}")

def libraly_stats(library):
    """
    Статистика
    :param library: библиотеки
    :return:
    """
    print("\nСтатистика библиотеки ")
    print("Всего книг",library.__len__())
    all_books = library.get_all_books()
    book_types = {}
    for book in all_books:
        book_type = type(book).__name__
        book_types[book_type] = book_types.get(book_type, 0) + 1
    print("\nТипы книг:")
    for book_type, count in book_types.items():
        print(f"{book_type} {count}")
    print("\nВсе книги:")
    for i, book in enumerate(all_books, 1):
        print(f"{i}. {book.title} - {book.author}")

if __name__ == "__main__":
    """
    Начинает симуляцию точка входа
    """
    run_simulation(steps=15, seed=42)