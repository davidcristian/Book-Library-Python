from random import randint
from datetime import datetime, timedelta

from domain import Rental
from repository import RentalRepository
from exceptions import RepositoryException


class RentalService:
    """
    Service for rental operations
    """
    def __init__(self, rental_repo, book_repo, client_repo) -> None:
        """
        Creates a RentalService instance
        :param rental_repo: the rental repo
        :param book_repo: the book repo
        :param client_repo: the client repo
        """
        self.__bookRepo = book_repo
        self.__clientRepo = client_repo
        self.__rental_repo = rental_repo

        # Only preload data for in-memory repositories
        if type(rental_repo) == RentalRepository:
            self.preload()

    def preload(self) -> None:
        """
        Preloads the repository with 20 randomly generated items
        """
        current_rental = 0
        available_books = list(range(20))
        available_clients = list(range(20))

        for iterator in range(20):
            if randint(0, 1) == 0:
                book = randint(0, len(available_books) - 1)
                client = randint(0, len(available_books) - 1)
                start = (datetime.today() - timedelta(randint(300, 600))).strftime("%Y/%m/%d")
                end = (datetime.today() - timedelta(randint(0, 299))).strftime("%Y/%m/%d")

                self.__rental_repo.get_repo().append(Rental(current_rental, available_books[book],
                                                            available_clients[client], start,
                                                            end if randint(0, 1) == 0 else "-1"))

                available_books.pop(book)
                available_clients.pop(client)
                current_rental += 1

    def filter_rentals(self, client, book) -> list:
        """
        Filters the rentals by client and book
        :param client: the id of a client (None = all)
        :param book: the id of a book (None = all)
        :return: a list of rentals performed by the provided client for the provided book
        """
        result = list()
        for rental in self.__rental_repo.get_repo():
            if client is not None and rental.get_client_id() != client:
                continue
            if book is not None and rental.get_book_id() != book:
                continue
            result.append(rental)

        return result

    def get_most_rented_books(self) -> str:
        """
        :return: the most rented books sorted in descending order by number of rentals
        """
        times_rented = dict()

        for rental in self.__rental_repo.get_repo():
            if rental.get_book_id() in times_rented:
                times_rented[rental.get_book_id()] += 1
            else:
                times_rented[rental.get_book_id()] = 1

        combined_list = sorted(zip(list(times_rented.values()), list(times_rented.keys())), reverse=True)
        sorted_list = [element for _, element in combined_list]

        result = ""
        for book in sorted_list:
            result += (str(self.__bookRepo.search_book_by_id(book)) + ". Rented " + str(times_rented[book]) +
                       " time" + ("s" if times_rented[book] > 1 else "") + ".\n")

        return result.rstrip()

    def get_most_active_clients(self) -> str:
        """
        :return: the most active clients sorted in descending order by number of rentals
        """
        days_rented = dict()
        date_format = "%Y/%m/%d"

        for rental in self.__rental_repo.get_repo():
            start = datetime.strptime(rental.get_rented_date(), date_format)
            end = datetime.strptime(rental.get_returned_date(), date_format) if rental.get_returned_date() != "-1"\
                else datetime.today()

            if rental.get_client_id() in days_rented:
                days_rented[rental.get_client_id()] += ((end - start).days + 1)
            else:
                days_rented[rental.get_client_id()] = (end - start).days + 1

        combined_list = sorted(zip(list(days_rented.values()), list(days_rented.keys())), reverse=True)
        sorted_list = [element for _, element in combined_list]

        result = ""
        for client in sorted_list:
            result += (str(self.__clientRepo.search_client_by_id(client)) + ". Rented for " + str(days_rented[client]) +
                       " day" + ("s" if days_rented[client] > 1 else "") + ".\n")

        return result.rstrip()

    def get_most_rented_authors(self) -> str:
        """
        :return: the most rented authors sorted in descending order by number of rentals
        """
        times_rented = dict()

        for rental in self.__rental_repo.get_repo():
            book = self.__bookRepo.search_book_by_id(rental.get_book_id())
            if book.get_author() in times_rented:
                times_rented[book.get_author()] += 1
            else:
                times_rented[book.get_author()] = 1

        combined_list = sorted(zip(list(times_rented.values()), list(times_rented.keys())), reverse=True)
        sorted_list = [element for _, element in combined_list]

        result = ""
        for author in sorted_list:
            result += (author + " rented " + str(times_rented[author]) +
                       " time" + ("s" if times_rented[author] > 1 else "") + ".\n")

        return result.rstrip()

    def create_rental(self, rental_id: int, book_id: int, client_id: int,
                      start: str = datetime.today().strftime("%Y/%m/%d")) -> None:
        """
        Creates a rental
        :param rental_id: the rental ID
        :param book_id: the ID of the book
        :param client_id: the ID of the client
        :param start: the rental start date
        """
        rental = Rental(rental_id, book_id, client_id, start, "-1")

        rentals = self.filter_rentals(None, book_id)
        for rent in rentals:
            if start < rent.get_rented_date() or\
                    (rent.get_returned_date() != "-1" and start > rent.get_returned_date()):
                continue

            raise RepositoryException("The book is not available at the current time!")

        self.__rental_repo.rent(rental)

    def return_rental(self, rental_id: int, end: str = datetime.today().strftime("%Y/%m/%d")) -> None:
        """
        Returns a rental
        :param rental_id: the ID of the rental
        :param end: the end date of the rental
        """
        self.__rental_repo.unrent(rental_id, end)

    def remove_rental(self, rental_id: int) -> None:
        """
        Removes a rental
        :param rental_id: the ID of the rental
        """
        self.__rental_repo.remove(rental_id)

    def search_rental_by_id(self, rental_id: int) -> Rental:
        """
        Searches a rental by ID
        :param rental_id: the ID of the rental
        :return: the rental with the provided ID
        """
        return self.__rental_repo.search_rental_by_id(rental_id)

    def list(self) -> str:
        """
        :return: a string containing the list of rentals
        """
        return self.__rental_repo.list()
