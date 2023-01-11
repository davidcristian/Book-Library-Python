from random import randint

from domain import Book
from repository import BookRepository
from utils import Generator


class BookService:
    """
    A service for the BookRepository class
    """

    def __init__(self, repository, rental_service) -> None:
        """
        :param repository: the book repository
        :param rental_service: the rental service
        """
        self.__repository = repository
        self.__rental_service = rental_service

        # Only preload data for in-memory repositories
        if type(repository) == BookRepository:
            self.preload()

    def preload(self) -> None:
        """
        Preloads the repository with 20 randomly generated items
        """
        for iterator in range(20):
            self.__repository.get_repo().append(Book(iterator,
                                                     Generator.BOOKS[randint(0, len(Generator.BOOKS) - 1)].title(),
                                                     Generator.NAMES[randint(0, len(Generator.NAMES) - 1)] +
                                                     " " + Generator.NAMES[randint(0, len(Generator.NAMES) - 1)]))

    def create(self, book_id: int, title: str, author: str) -> None:
        """
        Creates a new book
        :param book_id: the id of the book
        :param title: the title of the book
        :param author: the author of the book
        """
        book = Book(book_id, title, author)
        self.__repository.add(book)

    def delete(self, book_id: int) -> None:
        """
        Deletes a book
        :param book_id: the id of the book
        """
        self.__repository.remove(book_id)

        rentals = self.__rental_service.filter_rentals(None, book_id)
        for rental in rentals:
            self.__rental_service.remove_rental(rental.get_rental_id())

    def update(self, book_id: int, title: str, author: str) -> None:
        """
        Updates the title and author of a book
        :param book_id: the id of the book
        :param title: the new title
        :param author: the new author
        """
        self.__repository.update(book_id, title, author)

    def list(self) -> str:
        """
        :return: a string containing the list of books
        """
        return self.__repository.list()

    def search_book_by_id(self, book_id: int) -> Book:
        """
        Searches for a book by its ID
        :param book_id: the ID of the book
        :return: the book with the provided ID
        """
        return self.__repository.search_book_by_id(book_id)

    def search_book_by_title(self, book_title: str) -> list:
        """
        Searches for a book by its title
        :param book_title: the string that should be looked for inside the title of the books
        :return: the list of books matching the given criterion
        """
        return self.__repository.search_book_by_title(book_title)

    def search_book_by_author(self, book_author: str) -> list:
        """
        Searches for a book by its author
        :param book_author: the string that should be looked for inside the author of the books
        :return: the list of books matching the given criterion
        """
        return self.__repository.search_book_by_author(book_author)
