from typing import List, Generator, Union
from abc import ABC, abstractmethod
from pydantic import BaseModel
import json
import os
from homework2.decorators import log_action, check_exists


class BookModel(BaseModel):
    """
    Для класу “Книга” створіть модель pydantic BookModel з атрибутами книги: назва, автор, рік видання.
    """

    title: str
    author: str
    year: int


class Publication(ABC):
    """
    Додайте абстрактний клас або метод, який вимагає реалізації у дочірніх класах.
    """

    @abstractmethod
    def get_info(self) -> str:
        pass


class Book(Publication):
    """
    Клас "Книга":
    Книга повинна приймати аргументом інстанс BookModel.
    Метод, що повертає стрічку з інформацією про книгу.
    Використовуйте інкапсуляцію, роблячи деякі атрибути приватними.
    """

    def __init__(self, data: BookModel) -> None:
        self._title: str = data.title
        self._author: str = data.author
        self._year: int = data.year

    def get_info(self) -> str:
        return f"Книга: '{self._title}' автор: {self._author}, рік: {self._year}"

    def to_dict(self) -> dict:
        return {
            "type": "Book",
            "title": self._title,
            "author": self._author,
            "year": self._year,
        }

    @property
    def title(self) -> str:
        return self._title

    @property
    def author(self) -> str:
        return self._author


class Magazine(Book):
    """
    Застосуйте спадкування, створивши, наприклад, клас "Журнал", який наслідується від "Книги".
    """

    def get_info(self) -> str:
        return f"Журнал: '{self._title}' автор: {self._author}, рік: {self._year}"

    def to_dict(self) -> dict:
        return {
            "type": "Magazine",
            "title": self._title,
            "author": self._author,
            "year": self._year,
        }


class LibraryContextManager:
    """
    Контекстний менеджер для роботи з файлами:
    збереження списку книг до файлу та завантаження списку книг з файлу.
    """

    def __init__(self, filename: str, library: "Library") -> None:
        self.filename: str = filename
        self.library: Library = library

    def __enter__(self) -> "Library":
        if os.path.exists(self.filename):
            with open(self.filename, "r", encoding="utf-8") as file:
                data = json.load(file)
                for entry in data:
                    model = BookModel(
                        title=entry["title"], author=entry["author"], year=entry["year"]
                    )
                    item: Union[Book, Magazine] = (
                        Book(model) if entry["type"] == "Book" else Magazine(model)
                    )
                    self.library.add_book(item)
        return self.library

    def __exit__(self, exc_type: type, exc_val: BaseException, exc_tb: object) -> None:
        existing: List[dict] = []
        if os.path.exists(self.filename):
            with open(self.filename, "r", encoding="utf-8") as file:
                existing = json.load(file)

        existing_books = {(e["title"], e["author"], e["year"]) for e in existing}

        all_books = self.library._books.copy()
        for b in all_books:
            key = (b._title, b._author, b._year)
            if key not in existing_books:
                existing.append(
                    {
                        "title": b._title,
                        "author": b._author,
                        "year": b._year,
                        "type": "Book" if isinstance(b, Book) else "Magazine",
                    }
                )
                existing_books.add(key)

        with open(self.filename, "w", encoding="utf-8") as file:
            json.dump(existing, file, ensure_ascii=False, indent=2)


class Library:
    """
    Клас "Бібліотека":
    Атрибути: список книг.
    Ітератор, який дозволяє проходитися по всіх книгах у бібліотеці.
    Генератор, який повертає книги за імʼям одного автора.
    """

    def __init__(self) -> None:
        self._books: List[Publication] = []

    @log_action
    def add_book(self, item: Publication) -> None:
        self._books.append(item)

    @check_exists
    def remove_book(self, title: str) -> None:
        self._books = [book for book in self._books if book.title != title]
        print(f"Книга '{title}' видалена.")

    def __iter__(self) -> Generator[Publication, None, None]:
        return iter(self._books)

    def books_by_author(self, author: str) -> Generator[Publication, None, None]:
        return (book for book in self._books if book.author == author)
