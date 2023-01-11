

class StackException(Exception):
    """
    Custom exception for the Undo/Redo Stack class
    """
    def __init__(self, message: str) -> None:
        """
        Creates a StackException instance
        :param message: the error message
        """
        self.__message = message

    def __str__(self) -> str:
        """
        :return: the error message
        """
        return self.__message


class UndoException(StackException):
    def __init__(self, message: str) -> None:
        super().__init__(message)


class RedoException(StackException):
    def __init__(self, message: str) -> None:
        super().__init__(message)
