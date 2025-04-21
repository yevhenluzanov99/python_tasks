import unittest
from homework2.library import (
    Library,
    Book,
    Magazine,
    BookModel,
    LibraryContextManager,
)


class TestLibrary(unittest.TestCase):
    """
    Результатом виконання скрипта повинно бути:
        - створення бібліотеки
        - створення інстансу книги та журналу
        - додавання їх у бібліотеку
        - виведення списку книг у бібліотеці
        - виведення списку книг бібліотеки по імені автора
        - збереження списку книг у файл
        - видалення книги з бібліотеки
        - виведення списку книг після видалення
        - додавання книг з файлу в бібліотеку
        - виведення списку книг бібліотеки після додавання
    """

    def setUp(self):
        self.library = Library()
        self.book = Book(BookModel(title="Тестова книга", author="Автор 1", year=2020))
        self.magazine = Magazine(
            BookModel(title="Тестовий журнал", author="Автор 2", year=2021)
        )
        self.library.add_book(self.book)
        self.library.add_book(self.magazine)

    def test_add_books(self):
        self.assertEqual(len(list(self.library)), 2)

    def test_books_by_author(self):
        books = list(self.library.books_by_author("Автор 1"))
        self.assertEqual(len(books), 1)
        self.assertEqual(books[0].title, "Тестова книга")

    def test_remove_book(self):
        self.library.remove_book("Тестова книга")
        titles = [b.title for b in self.library]
        self.assertNotIn("Тестова книга", titles)

    def test_save_and_load_library(self):
        filename = "homework2/test_library.json"

        with LibraryContextManager(filename, self.library):
            loaded_titles = [b.title for b in self.library]

        self.assertIn("Тестова книга", loaded_titles)
        self.assertIn("Тестовий журнал", loaded_titles)
        self.assertIn("Тестова книга3", loaded_titles)
        self.assertIn("Тестовий журнал4", loaded_titles)


if __name__ == "__main__":
    unittest.main()
