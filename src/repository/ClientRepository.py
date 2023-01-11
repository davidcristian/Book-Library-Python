import os
import pickle

from utils import Iterable
from domain import Client
from exceptions import RepositoryException


class ClientRepository(Iterable):
    """
    A class that represents a client repository
    """
    def __init__(self) -> None:
        """
        Constructor for the ClientRepository class
        """
        super(ClientRepository, self).__init__()
        self._repo = Iterable()

    def get_repo(self) -> Iterable:
        """
        :return: the internal list
        """
        return self._repo

    def add(self, new_client: Client) -> None:
        """
        Adds a new client to the repository
        :param new_client: the new client
        """
        for client in self._repo:
            if client.get_client_id() == new_client.get_client_id():
                raise RepositoryException("Duplicate client ID!")

        self._repo.append(new_client)

    def remove(self, client_id: int) -> None:
        """
        Removes a client from the repository
        :param client_id: the ID of the client
        """
        for client in self._repo:
            if client.get_client_id() == client_id:
                self._repo.remove(client)
                return None

        raise RepositoryException("There is no client with the given ID!")

    def update(self, client_id: int, new_name: str) -> None:
        """
        Updates a client
        :param client_id: the ID of the client that should be updated
        :param new_name: the new name of the client
        """
        for client in self._repo:
            if client.get_client_id() == client_id:
                client.set_name(new_name)
                return None

        raise RepositoryException("There is no client with the given ID!")

    def list(self) -> str:
        """
        :return: a string representation of the repository
        """
        value = "" if len(self._repo) > 0 else "The list of clients is empty."
        self._repo = Iterable.sort(self._repo, lambda x, y: x.get_client_id() > y.get_client_id())

        for client in self._repo:
            value += (str(client) + "\n")

        return value.rstrip()

    def search_client_by_id(self, client_id: int) -> Client:
        """
        Searches for a client by ID
        :param client_id: the ID of the client
        :return: the client with the provided ID
        """
        clients = Iterable.filter(self._repo, lambda x: x.get_client_id() == client_id)
        if len(clients) == 0:
            raise RepositoryException("There is no client with the given ID!")

        return clients[0]

    def search_client_by_name(self, client_name: str) -> list:
        """
        Searches for a client by name
        :param client_name: the string that should be looked for inside the name of the clients
        :return: the list of clients matching the given criterion
        """
        clients = Iterable.filter(self._repo, lambda x: client_name.strip().lower() in x.get_name().strip().lower())
        if len(clients) == 0:
            raise RepositoryException("There are no clients with the given name!")

        return clients


class ClientRepositoryText(ClientRepository):
    """
    A class that represents a client repository using text files for storage
    """
    def __init__(self, file_path: str = "") -> None:
        """
        Constructor for the ClientRepository class
        :param file_path: the path to the storage file
        """
        super(ClientRepositoryText, self).__init__()
        self.__file_path = file_path

        with open(file_path, "r") as input_file:
            if os.stat(file_path).st_size > 0:
                for line in input_file:
                    line = line.strip()
                    if len(line) > 0:
                        object_string = line.split(",")
                        self._repo.append(Client(int(object_string[0]), object_string[1]))

    def save_data(self) -> None:
        """
        Save the data according to the currently used data type
        """
        with open(self.__file_path, "w") as output_file:
            output_file.truncate(0)
            for client in self._repo:
                object_string = str(client.get_client_id()) + "," + client.get_name()
                output_file.write(object_string + "\n")

    def add(self, new_client: Client) -> None:
        """
        Adds a new client to the repository
        :param new_client: the new client
        """
        super(ClientRepositoryText, self).add(new_client)
        self.save_data()

    def remove(self, client_id: int) -> None:
        """
        Removes a client from the repository
        :param client_id: the ID of the client
        """
        super(ClientRepositoryText, self).remove(client_id)
        self.save_data()

    def update(self, client_id: int, new_name: str) -> None:
        """
        Updates a client
        :param client_id: the ID of the client that should be updated
        :param new_name: the new name of the client
        """
        super(ClientRepositoryText, self).update(client_id, new_name)
        self.save_data()


class ClientRepositoryBinary(ClientRepository):
    """
    A class that represents a client repository using binary files for storage
    """
    def __init__(self, file_path: str = "") -> None:
        """
        Constructor for the ClientRepository class
        :param file_path: the path to the storage file
        """
        super(ClientRepositoryBinary, self).__init__()
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

    def add(self, new_client: Client) -> None:
        """
        Adds a new client to the repository
        :param new_client: the new client
        """
        super(ClientRepositoryBinary, self).add(new_client)
        self.save_data()

    def remove(self, client_id: int) -> None:
        """
        Removes a client from the repository
        :param client_id: the ID of the client
        """
        super(ClientRepositoryBinary, self).remove(client_id)
        self.save_data()

    def update(self, client_id: int, new_name: str) -> None:
        """
        Updates a client
        :param client_id: the ID of the client that should be updated
        :param new_name: the new name of the client
        """
        super(ClientRepositoryBinary, self).update(client_id, new_name)
        self.save_data()
