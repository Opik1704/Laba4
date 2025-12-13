# Лабораторная работа номер 3

## Алгоритмы и структуры данных
Ввод бесконечный пока не введешь break
## Структура проекта
 <pre>
  ├── src/ # Исходный код
  │ ├── init.py # Инициализация 
  │ ├── AudioBook.py # Аудиокнига наследует книгу
  │ ├── Book.py # Книга
  │ ├── Library.py # Библиотека
  │ ├── TextBook.py # Учебник наследует книгу
  │ ├── main.py # Основной класс в нем происходит симуляция
  │ ├── BookCollection.py Коллекция книг
  │ └── IndexBookCollection.py Словарная коллекция для индексов
  ├── tests/ # Тесты
  │ ├── init.py # Инициализация тестов
  │ └── test.py # Тесты 
  ├── requirements.txt
  ├── .gitignore
  ├── .pre-commit-config.yaml
  └── README.md
  </pre>
## Реализована Библиотека Library
Класс Book от которой наследуются Audiobook и TextBook
BookCollection и IndexBookCollection поддерживают __iter__ , __len__ , __getitem__
Добавлены все магические методы по смыслу 
Реализована симуляция со взятием книг возвращением, поиском книг по разным параметрам и выбиранием книг по жанру

## Установка 
 ```bash
 $ python -m venv venv
 $ source venv/bin/activate
 
 $ pip install requirements.txt
 $ python -m src.main
```
