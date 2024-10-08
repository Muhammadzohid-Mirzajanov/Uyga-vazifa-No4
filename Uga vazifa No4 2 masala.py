from abc import ABC, abstractmethod

class Book(ABC):
    def __init__(self, title, author, isbn, page_count):
        self.__title = title
        self.__author = author
        self.__isbn = isbn
        self.__page_count = page_count
        self.__current_page = 0

    @property
    def title(self):
        return self.__title

    @property
    def author(self):
        return self.__author

    @property
    def isbn(self):
        return self.__isbn

    @property
    def page_count(self):
        return self.__page_count

    def get_info(self):
        return f"{self.title} by {self.author}, ISBN: {self.isbn}, Pages: {self.page_count}"

    def read_page(self):
        if self.__current_page < self.page_count:
            self.__current_page += 1
            return f"Reading page {self.__current_page} of {self.title}."
        else:
            return "You've finished reading the book!"

    def bookmark_page(self):
        return f"Bookmarking page {self.__current_page} of {self.title}."


class EBook(Book):
    def __init__(self, title, author, isbn, page_count, file_size):
        super().__init__(title, author, isbn, page_count)
        self.__file_size = file_size

    def download(self):
        return f"Downloading {self.title} of size {self.__file_size} MB."


class AudioBook(Book):
    def __init__(self, title, author, isbn, page_count, duration):
        super().__init__(title, author, isbn, page_count)
        self.__duration = duration

    def play(self):
        return f"Playing the audiobook {self.title} for {self.__duration} minutes."

ebook = EBook("Python Programming", "John Doe", "1234567890", 300, 5)
audiobook = AudioBook("Learn Python", "Jane Smith", "0987654321", 250, 180)

print(ebook.get_info())
print(ebook.download())
print(ebook.read_page())
print(ebook.bookmark_page())

print()

print(audiobook.get_info())
print(audiobook.play())
print(audiobook.read_page())
print(audiobook.bookmark_page())
