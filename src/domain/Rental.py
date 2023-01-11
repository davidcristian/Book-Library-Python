from exceptions import RentalException


class Rental:
    """
    A class that represents a rental through a rental ID, a book ID, a client ID, a rented date, and a returned date
    """
    def __init__(self, rental_id: int, book_id: int, client_id: int, rented_date: str, returned_date: str) -> None:
        """
        Creates a Rental instance
        :param rental_id: the ID of the rental
        :param book_id: the ID of the book that was rented
        :param client_id: the ID of the client that rented
        :param rented_date: the start date of the rental
        :param returned_date: the end date of the rental
        """
        self.__rental_id = -1
        self.set_rental_id(rental_id)

        self.__book_id = -1
        self.set_book_id(book_id)

        self.__client_id = -1
        self.set_client_id(client_id)

        self.__rented_date = "-1"
        self.set_rented_date(rented_date)

        self.__returned_date = "-1"
        self.set_returned_date(returned_date)

    def __str__(self) -> str:
        """
        :return: the string representation of a rental
        """
        return str(self.__rental_id) + " | Book with ID " + str(self.__book_id) +\
            " rented by client with ID " + str(self.__client_id) + " at date " + self.__rented_date +\
            ("; Not returned yet" if self.__returned_date == "-1" else ("; Returned at date " + self.__returned_date))

    def __eq__(self, other) -> bool:
        """
        Checks if two rentals are equal
        :param other: other rental
        :return: true if the rentals are the same, false otherwise
        """
        return isinstance(other, Rental) and self.__rental_id == other.get_rental_id()

    def get_rental_id(self) -> int:
        """
        :return: the rental id
        """
        return self.__rental_id

    def set_rental_id(self, value: int) -> None:
        """
        Sets the rental_id property to the given value
        :param value: the new value
        """
        if value < 0:
            raise RentalException("Invalid rental ID! The rental ID cannot be less than 0.")

        self.__rental_id = value

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
            raise RentalException("Invalid book ID! The book ID cannot be less than 0.")

        self.__book_id = value

    def get_client_id(self) -> int:
        """
        :return: the client id
        """
        return self.__client_id

    def set_client_id(self, value: int) -> None:
        """
        Sets the client_id property to the given value
        :param value: the new value
        """
        if value < 0:
            raise RentalException("Invalid client ID! The client ID cannot be less than 0.")

        self.__client_id = value

    def get_rented_date(self) -> str:
        """
        :return: the rented date
        """
        return self.__rented_date

    def set_rented_date(self, value: str) -> None:
        """
        Sets the get_rented_date property to the given value
        :param value: the new value
        """
        if len(value) != 10 and value[2] != "/" and value[5] != "/":
            raise RentalException("Invalid rented date! Please use the following format: dd/mm/yyyy")

        self.__rented_date = value

    def get_returned_date(self) -> str:
        """
        :return: the returned date
        """
        return self.__returned_date

    def set_returned_date(self, value: str) -> None:
        """
        Sets the returned_date property to the given value
        :param value: the new value
        """
        if value == "-1":
            self.__returned_date = "-1"
            return None

        if len(value) != 10 and value[2] != "/" and value[5] != "/":
            raise RentalException("Invalid returned date! Please use the following format: dd/mm/yyyy")

        self.__returned_date = value
