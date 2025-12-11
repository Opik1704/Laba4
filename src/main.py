import random
import time

from Laba4.src.Book import Book
from Laba4.src.TextBook import TextBook
from Laba4.src.AudioBook import AudioBook
from Laba4.src.BookCollection import BookCollection
from Laba4.src.IndexBookCollection import IndexBookCollection
from Laba4.src.Library import Library


def run_simulation(steps=15, seed=None):
    if seed is not None:
        random.seed(seed)
    else:
        random.seed(int(time.time()))
    print(seed, steps)

    library = Library(BookCollection(), IndexBookCollection())

    books = [
        Book("1984", "Джордж Оруэлл", 1949, "Антиутопия", "1"),
        Book("Скотный двор", "Джордж Оруэлл", 1945, "Сатира", "2"),
        Book("Убить пересмешника", "Харпер Ли", 1960, "Роман", "3"),
        AudioBook("Мастер и Маргарита", "Михаил Булгаков", 1967, "Роман",
                  "4", "Вячеслав Герасимов", 1320, "русский"),
        TextBook("Алгебра", "Иванов И.И.", 2020, "Учебник", "5",
                 "Математика", "10 класс", "Просвещение"),
    ]

    for book in books:
        library.add_book(book)

    print(f"Всего книг: {len(library)}")

    for step in range(steps):
        print(f"\nШаг {step + 1}:")

        action = random.choice([
            "add_book",
            "add_books",
            "remove_book",
            "remove_by_isbn",
            "find_by_isbn",
            "find_by_year",
            "find_by_author",
            "find_by_title",
            "find_by_genre",
            "get_all_books",
        ])
        if action == "add_book":
            add_book_action(library, step)
        elif action == "add_books":
            add_books_action(library, step)
        elif action == "remove_book":
            remove_book_action(library)
        elif action == "remove_by_isbn":
            remove_by_isbn_action(library)
        elif action == "find_by_isbn":
            find_by_isbn_action(library)
        elif action == "find_by_year":
            find_by_year_action(library)
        elif action == "find_by_author":
            find_by_author_action(library)
        elif action == "find_by_title":
            find_by_title_action(library)
        elif action == "find_by_genre":
            find_by_genre_action(library)
        elif action == "get_all_books":
            get_all_books_action(library,)
        time.sleep(0.9)
    libraly_stats(library)

def add_book_action(library, step):
    book_type = random.choice(["book", "audiobook", "textbook"])
    if book_type == "book":
        new_book = Book(
            f"Книга {step} ",
            f"Автор{random.randint(1, 10)}", 2000 + random.randint(0, 20),
            random.choice(["Роман", "Детектив"]),
            f"ISBN{random.randint(100, 999)}"
        )
    elif book_type == "audiobook":
        new_book = AudioBook(
            f"Аудиокнига{step}",
            f"Автор{random.randint(1, 5)}",
            2010 + random.randint(0, 10),
            "Фантастика",
            f"AUDIO{random.randint(100, 999)}",
            f"Чтец{random.randint(1, 3)}",random.randint(300, 600),
            "русский"
        )
    else:
        new_book = TextBook(
            f"Учебник{step}",
            f"Автор{random.randint(1, 5)}",
            2015 + random.randint(0, 5),
            "Учебник",
            f"TEXT{random.randint(100, 999)}",
            random.choice(["Математика", "Физика"]),
            f"{random.randint(5, 11)} класс",
            "Просвещение"
        )

    result = library.add_book(new_book)
    print(f"Добавление книги: {new_book.title}, тип книги: {book_type}")


def add_books_action(library, step):
    new_books = [
        Book(f"Добавленная{step} 1", "Автор1", 2023, "Роман", f"ADD{step}1"),
        Book(f"Добавленная{step} 2", "Автор2", 2023, "Детектив", f"ADD{step}2")
    ]

    library.add_books(new_books)
    print(f"Добавление {len(new_books)} книг")
    print(f"Теперь книг: {len(library)}")


def remove_book_action(library):
    all_books = library.get_all_books()
    if not all_books:
        print("Нет книг для удаления")
        return
    book = random.choice(all_books)
    library.remove_book(book)
    print(f"Удаление книги: {book.title}")
    print(f"Осталось книг: {len(library)}")

def remove_by_isbn_action(library):
    all_books = library.get_all_books()
    if not all_books:
        print("Нет книг для удаления")
        return
    book = random.choice(all_books)
    library.remove_by_isbn(book.isbn)
    print(f"Удаление по ISBN: {book.isbn}")
    print(f"Название: {book.title}")

def find_by_isbn_action(library):
    all_books = library.get_all_books()
    if not all_books:
        print("Нет книг для поиска")
        return
    book = random.choice(all_books)
    found = library.find_book_by_isbn(book.isbn)
    if found:
        print(f"Поиск по ISBN: {book.isbn}")
        print(f"Найдено: {found.title}")
    else:
        print(f"Поиск по ISBN: {book.isbn}")
        print("Не найдено")

def find_by_year_action(library):
    years = [1949, 1945, 1960, 1967, 2020]
    year = random.choice(years)

    books = library.find_books_by_year(year)
    print(f"Поиск книг {year} года")
    print(f"Найдено: {len(books)} книг")
    for book in books[:2]:
        print(f"- {book.title}")

def find_by_author_action(library):
    authors = ["George Orwell", "Harper Lee", "Михаил Булгаков"]
    author = random.choice(authors)

    books = library.find_books_by_author(author)
    print(f"Поиск книг автора: {author}")
    print(f"Найдено: {len(books)} книг")
    for book in books[:2]:
        print(f"- {book.title}")

def find_by_title_action(library):
    all_books = library.get_all_books()
    if not all_books:
        print("Нет книг для поиска")
        return

    book = random.choice(all_books)
    found = library.find_book_by_title(book.title)
    if found:
        print(f"Поиск по названию: {book.title}")
        print(f"Найдено: {found.title}")
    else:
        print(f"Поиск по названию: {book.title}")
        print("Не найдено")


def find_by_genre_action(library):
    genres = ["Антиутопия", "Сатира", "Роман", "Учебник"]
    genre = random.choice(genres)

    books = library.find_books_by_genre(genre)
    print(f"Поиск книг по жанру: {genre}")
    print(f"Нашлось {len(books)} книг")
    for book in books:
        print(f" {book.title}")

def get_all_books_action(library):
    all_books = library.get_all_books()
    print(f"Всего: {len(all_books)} книг c типами")
    book_types = {}
    for book in all_books:
        book_type = type(book).__name__
        book_types[book_type] = book_types.get(book_type, 0) + 1
    for book_type, count in book_types.items():
        print(f"{book_type}: {count}")

def libraly_stats(library):
    print("\nСтатистика библиотеки ")
    print(f"Всего книг {library.__len__()}")
    all_books = library.get_all_books()
    book_types = {}
    for book in all_books:
        book_type = type(book).__name__
        book_types[book_type] = book_types.get(book_type, 0) + 1
    print("Типы книг:")
    for book_type, count in book_types.items():
        print(f"{book_type} {count}")
    print("\nВсе книги:")
    for i, book in enumerate(all_books, 1):
        print(f"{i}. {book.title} - {book.author}")

if __name__ == "__main__":
    run_simulation(steps=15, seed=42)