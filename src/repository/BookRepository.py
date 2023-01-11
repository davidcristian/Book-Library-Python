import os
import pickle

from utils import Iterable
from exceptions import RepositoryException
from domain import Book


class BookRepository(Iterable):
    """
    A class that represents a book repository
    """
    def __init__(self) -> None:
        """
        Constructor for the BookRepository class
        """
        super(BookRepository, self).__init__()
        self._repo = Iterable()

    def get_repo(self) -> Iterable:
        """
        :return: the internal list
        """
        return self._repo

    def add(self, new_book: Book) -> None:
        """
        Adds a new book to the repository
        :param new_book: the new book
        """
        for book in self._repo:
            if book.get_book_id() == new_book.get_book_id():
                raise RepositoryException("Duplicate book ID!")

        self._repo.append(new_book)

    def remove(self, book_id: int) -> None:
        """
        Removes a book from the repository
        :param book_id: the ID of the book
        """
        for book in self._repo:
            if book.get_book_id() == book_id:
                self._repo.remove(book)
                return None

        raise RepositoryException("There is no book with the given ID!")

    def update(self, book_id: int, new_title: str, new_author: str) -> None:
        """
        Updates a book
        :param book_id: the ID of the book that should be updated
        :param new_title: the new title of the book
        :param new_author: the new author of the book
        """
        for book in self._repo:
            if book.get_book_id() == book_id:
                book.set_title(new_title)
                book.set_author(new_author)
                return None

        raise RepositoryException("There is no book with the given ID!")

    def list(self) -> str:
        """
        :return: a string representation of the repository
        """
        value = "" if len(self._repo) > 0 else "The list of books is empty."
        self._repo = Iterable.sort(self._repo, lambda x, y: x.get_book_id() > y.get_book_id())

        for book in self._repo:
            value += (str(book) + "\n")

        return value.rstrip()

    def search_book_by_id(self, book_id: int) -> Book:
        """
        Searches for a book by its ID
        :param book_id: the ID of the book
        :return: the book with the provided ID
        """
        books = Iterable.filter(self._repo, lambda x: x.get_book_id() == book_id)
        if len(books) == 0:
            raise RepositoryException("There is no book with the given ID!")

        return books[0]

    def search_book_by_title(self, book_title: str) -> list:
        """
        Searches for a book by its title
        :param book_title: the string that should be looked for inside the title of the books
        :return: the list of books matching the given criterion
        """
        books = Iterable.filter(self._repo, lambda x: book_title.strip().lower() in x.get_title().strip().lower())
        if len(books) == 0:
            raise RepositoryException("There are no books with the given title!")

        return books

    def search_book_by_author(self, book_author: str) -> list:
        """
        Searches for a book by its author
        :param book_author: the string that should be looked for inside the author of the books
        :return: the list of books matching the given criterion
        """
        books = Iterable.filter(self._repo, lambda x: book_author.strip().lower() in x.get_author().strip().lower())
        if len(books) == 0:
            raise RepositoryException("There are no books with the given author!")

        return books


class BookRepositoryText(BookRepository):
    """
    A class that represents a book repository using text files for storage
    """
    def __init__(self, file_path: str = "") -> None:
        """
        Constructor for the BookRepository class
        :param file_path: the path to the storage file
        """
        super(BookRepositoryText, self).__init__()
        self.__file_path = file_path

        with open(file_path, "r") as input_file:
            if os.stat(file_path).st_size > 0:
                for line in input_file:
                    line = line.strip()
                    if len(line) > 0:
                        object_string = line.split(",")
                        self._repo.append(Book(int(object_string[0]), object_string[1], object_string[2]))

    def save_data(self) -> None:
        """
        Save the data according to the currently used data type
        """
        with open(self.__file_path, "w") as output_file:
            output_file.truncate(0)
            for book in self._repo:
                object_string = str(book.get_book_id()) + "," + book.get_title() + "," +\
                                book.get_author()
                output_file.write(object_string + "\n")

    def add(self, new_book: Book) -> None:
        """
        Adds a new book to the repository
        :param new_book: the new book
        """
        super(BookRepositoryText, self).add(new_book)
        self.save_data()

    def remove(self, book_id: int) -> None:
        """
        Removes a book from the repository
        :param book_id: the ID of the book
        """
        super(BookRepositoryText, self).remove(book_id)
        self.save_data()

    def update(self, book_id: int, new_title: str, new_author: str) -> None:
        """
        Updates a book
        :param book_id: the ID of the book that should be updated
        :param new_title: the new title of the book
        :param new_author: the new author of the book
        """
        super(BookRepositoryText, self).update(book_id, new_title, new_author)
        self.save_data()


class BookRepositoryBinary(BookRepository):
    """
    A class that represents a book repository using binary files for storage
    """
    def __init__(self, file_path: str = "") -> None:
        """
        Constructor for the BookRepository class
        :param file_path: the path to the storage file
        """
        super(BookRepositoryBinary, self).__init__()
        self.__file_path = file_path

        with open(file_path, "rb") as input_file:
            if os.stat(file_path).st_size > 0:
                self.__repo = pickle.load(input_file)

    def save_data(self) -> None:
        """
        Save the data according to the currently used data type
        """
        with open(self.__file_path, "wb") as output_file:
            output_file.truncate(0)
            pickle.dump(self.__repo, output_file)

    def add(self, new_book: Book) -> None:
        """
        Adds a new book to the repository
        :param new_book: the new book
        """
        super(BookRepositoryBinary, self).add(new_book)
        self.save_data()

    def remove(self, book_id: int) -> None:
        """
        Removes a book from the repository
        :param book_id: the ID of the book
        """
        super(BookRepositoryBinary, self).remove(book_id)
        self.save_data()

    def update(self, book_id: int, new_title: str, new_author: str) -> None:
        """
        Updates a book
        :param book_id: the ID of the book that should be updated
        :param new_title: the new title of the book
        :param new_author: the new author of the book
        """
        super(BookRepositoryBinary, self).update(book_id, new_title, new_author)
        self.save_data()
