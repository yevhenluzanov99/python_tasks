import os
from functools import wraps


def log_action(func):
    """
    Декоратор для логування (запись події у файл .txt або .log )при додаванні нової книги до бібліотеки.
    """

    @wraps(func)
    def wrapper(self, item, *args, **kwargs):
        file_path = os.path.join(os.getcwd(), "homework2/library.log")
        result = func(self, item, *args, **kwargs)
        with open(file_path, "a", encoding="utf-8") as log_file:
            log_file.write(f"Дія: додано '{item.title}' автор: {item.author}\n")
        return result

    return wrapper


def check_exists(func):
    """
    Декоратор, який перевіряє наявність книги в бібліотеці перед її видаленням.
    """

    @wraps(func)
    def wrapper(self, title, *args, **kwargs):
        if any(book.title == title for book in self._books):
            return func(self, title, *args, **kwargs)
        else:
            print(f"Книга '{title}' не знайдена у бібліотеці.")

    return wrapper
