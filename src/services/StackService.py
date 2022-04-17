class StackService:
    """
    A class that handles undo and redo operations for the program
    """
    def __init__(self, rental_repo):
        """
        Initialize the class
        :param rental_repo: the rental_repository
        """
        self.__rental_repo = rental_repo

        self.__undo_stack = []
        self.__redo_stack = []

    def add_to_undo_stack(self, function):
        """
        Adds a function call to the undo stack and clears the redo stack
        because the user cannot redo operations after modifying the stack
        :param function: a function call
        """
        self.__redo_stack.clear()
        self.__undo_stack.append(function)

    def undo_operation(self):
        """
        Undo the previous operation done by the user
        """
        if len(self.__undo_stack) == 0:
            raise IndexError("There are no operations to undo!")

        self.__redo_stack.append(self.__undo_stack[-1])

        self.__undo_stack[-1][1]()
        if len(self.__undo_stack[-1]) == 3:
            for rental in self.__undo_stack[-1][2]:
                self.__rental_repo.get_repo().append(rental)

        self.__undo_stack.pop()

    def redo_operation(self):
        """
        Redo the previous operation that has been undone by the user
        """
        if len(self.__redo_stack) == 0:
            raise IndexError("There are no operations to redo!")

        self.__undo_stack.append(self.__redo_stack[-1])

        self.__redo_stack[-1][0]()
        self.__redo_stack.pop()
