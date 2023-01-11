

class BookException(Exception):
    """
    Custom exception for the Book class
    """
    def __init__(self, message: str) -> None:
        """
        Creates a BookException instance
        :param message: the error message
        """
        self.__message = message

    def __str__(self) -> str:
        """
        :return: the error message
        """
        return self.__message


class ClientException(Exception):
    """
    Custom exception for the Client class
    """
    def __init__(self, message: str) -> None:
        """
        Creates a ClientException instance
        :param message: the error message
        """
        self.__message = message

    def __str__(self) -> str:
        """
        :return: the error message
        """
        return self.__message


class RentalException(Exception):
    """
    Custom exception for the Rental class
    """
    def __init__(self, message: str) -> None:
        """
        Creates a RentalException instance
        :param message: the error message
        """
        self.__message = message

    def __str__(self) -> str:
        """
        :return: the error message
        """
        return self.__message
