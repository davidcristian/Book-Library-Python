from src.domain.Exceptions import ClientException


class Client:
    """
    A class that represents a client through an ID and a name
    """
    def __init__(self, client_id, name):
        """
        :param client_id: the ID of the client
        :param name: the name of the client
        """
        self.__client_id = -1
        self.set_client_id(client_id)

        self.__name = ""
        self.set_name(name)

    def __str__(self):
        """
        :return: the string representation of a client
        """
        return str(self.__client_id) + " | " + self.__name

    def __eq__(self, other):
        """
        :param other: other client
        :return: true if the clients are the same, false otherwise
        """
        return isinstance(other, Client) and self.__client_id == other.get_client_id()

    def get_client_id(self):
        """
        :return: the client id
        """
        return self.__client_id

    def set_client_id(self, value):
        """
        Sets the client_id property to the given value
        :param value: the new value
        """
        if value < 0:
            raise ClientException("Invalid client ID! The client ID cannot be less than 0.")

        self.__client_id = value

    def get_name(self):
        """
        :return: the name
        """
        return self.__name

    def set_name(self, value):
        """
        Sets the name property to the given value
        :param value: the new value
        """
        if len(value) == 0:
            raise ClientException("Invalid author name! The author name cannot be empty.")

        self.__name = value
