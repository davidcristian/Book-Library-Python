from exceptions import BookException


class Book:
    """
    A class that represents a Book through an ID, a title, and an author
    """

    def __init__(self, book_id: int, title: str, author: str) -> None:
        """
        Creates a Book instance
        :param book_id: the ID of the book
        :param title: the title of the book
        :param author: the author of the book
        """
        self.__book_id = -1
        self.set_book_id(book_id)

        self.__title = ""
        self.set_title(title)

        self.__author = ""
        self.set_author(author)

    def __str__(self) -> str:
        """
        :return: the string representation of a book
        """
        return str(self.__book_id) + " | " + self.__title + " - " + self.__author

    def __eq__(self, other) -> bool:
        """
        Checks if two books are equal
        :param other: other book
        :return: true if the books are the same, false otherwise
        """
        return isinstance(other, Book) and self.__book_id == other.get_book_id()

    def get_book_id(self) -> int:
        """
        :return: the book id
        """
        return self.__book_id

    def set_book_id(self, value: int) -> None:
        """
        Sets the book_id property to the given value
        :param value: the new value
        """
        if value < 0:
            raise BookException("Invalid book ID! The book ID cannot be less than 0.")

        self.__book_id = value

    def get_title(self) -> str:
        """
        :return: the book title
        """
        return self.__title

    def set_title(self, value: str) -> None:
        """
        Sets the title property to the given value
        :param value: the new value
        """
        if len(value) == 0:
            raise BookException("Invalid book title! The book title cannot be empty.")

        self.__title = value

    def get_author(self) -> str:
        """
        :return: the author
        """
        return self.__author

    def set_author(self, value: str) -> None:
        """
        Sets the author property to the given value
        :param value: the new value
        """
        if len(value) == 0:
            raise BookException("Invalid book author! The book author cannot be empty.")

        self.__author = value
