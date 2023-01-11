from random import randint

from domain import Client
from repository import ClientRepository
from utils import Generator


class ClientService:
    def __init__(self, repository, rental_service) -> None:
        """
        :param repository: the client repository
        :param rental_service: the rental service
        """
        self.__repository = repository
        self.__rental_service = rental_service

        # Only preload data for in-memory repositories
        if type(repository) == ClientRepository:
            self.preload()

    def preload(self) -> None:
        """
        Preloads the repository with 20 randomly generated items
        """
        for iterator in range(20):
            self.__repository.get_repo().append(Client(iterator, Generator.NAMES[randint(0, len(Generator.NAMES) - 1)]
                                                       + " " + Generator.NAMES[randint(0, len(Generator.NAMES) - 1)]))

    def create(self, client_id: int, name: str) -> None:
        """
        Creates a new client
        :param client_id: the ID of the client
        :param name: the name of the client
        """
        client = Client(client_id, name)
        self.__repository.add(client)

    def delete(self, client_id: int) -> None:
        """
        :param client_id: the client ID
        """
        self.__repository.remove(client_id)

        rentals = self.__rental_service.filter_rentals(client_id, None)
        for rental in rentals:
            self.__rental_service.remove_rental(rental.get_rental_id())

    def update(self, client_id: int, name: str) -> None:
        """
        Updates the name of a client
        :param client_id: the ID of the client
        :param name: the new name
        """
        self.__repository.update(client_id, name)

    def list(self) -> str:
        """
        :return: a string containing the list of clients
        """
        return self.__repository.list()

    def search_client_by_id(self, client_id: int) -> Client:
        """
        Searches for a client by ID
        :param client_id: the ID of the client
        :return: the client with the provided ID
        """
        return self.__repository.search_client_by_id(client_id)

    def search_client_by_name(self, client_name: str) -> list:
        """
        Searches for a client by name
        :param client_name: the string that should be looked for inside the name of the clients
        :return: the list of clients matching the given criterion
        """
        return self.__repository.search_client_by_name(client_name)
