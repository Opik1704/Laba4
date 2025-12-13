from Laba4.src.Book import Book

class AudioBook(Book):
    """Класс Аудиокнига наследуется от книги, добавляется Чтец Минуты Язык"""
    def __init__(self, title, author, year, genre, isbn, narrator, minutes ,language):
        """Иницализация"""
        super().__init__(title, author, year, genre, isbn)
        self.narrator = narrator
        self.minutes = minutes
        self.language = language

        self.playback_speed: float = 1.0
        self.last_position: int = 0

    def set_playback_position(self, minute):
        """
        Закладка на какой минуте остановилось просулшивание
        :param minute:
        :return:
        """
        if 0 <= minute <= self.minutes:
            self.last_position = minute
            return True
        return False
    def set_playback_speed(self, speed):
        """Изменение скорости воспроизведения"""
        self.playback_speed = speed
    def __str__(self):
        """Строковое представление"""
        base_info = super().__str__()
        return f"{base_info}\n  '{self.narrator}','{self.minutes}','{self.language}'"
