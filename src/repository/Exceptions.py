class RepositoryException(Exception):
    """
    Custom exceptions for the repositories
    """
    def __init__(self, message):
        """
        :param message: the error message
        """
        self.__message = message

    @property
    def message(self):
        """
        :return: the error message
        """
        return self.__message

    def __str__(self):
        """
        :return: the string representation of the error
        """
        return self.__message
