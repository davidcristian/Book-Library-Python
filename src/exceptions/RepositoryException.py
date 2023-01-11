

class RepositoryException(Exception):
    """
    Custom exception for the Repository class
    """
    def __init__(self, message: str) -> None:
        """
        Creates a RepositoryException instance
        :param message: the error message
        """
        self.__message = message

    @property
    def message(self) -> str:
        """
        :return: the error message
        """
        return self.__message

    def __str__(self) -> str:
        """
        :return: the string representation of the error
        """
        return self.__message
