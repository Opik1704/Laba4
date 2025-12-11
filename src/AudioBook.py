from Laba4.src.Book import Book

class AudioBook(Book):
    def __init__(self, title, author, year, genre, isbn, narrator, minutes ,language):
        super().__init__(title, author, year, genre, isbn)
        self.narrator = narrator
        self.minutes = minutes
        self.language = language

        self.playback_speed: float = 1.0
        self.last_position: int = 0

    def set_playback_position(self, minute):
        if 0 <= minute <= self.minutes:
            self.last_position = minute
            return True
        return False
    def set_playback_speed(self, speed):
        self.playback_speed = speed
    def __str__(self) -> str:
        base_info = super().__str__()
        audio_info = [f"Читает: {self.narrator}",f"Длительность в минутах: {self.minutes}",f"Язык: {self.language}",]
        return f"{base_info}\n" + "\n".join([f"  • {info}" for info in audio_info])
