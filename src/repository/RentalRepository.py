import os
import pickle

from utils import Iterable
from domain import Rental
from exceptions import RepositoryException


class RentalRepository(Iterable):
    """
    A class that represents a rental repository
    """
    def __init__(self) -> None:
        """
        Constructor for the RentalRepository class
        """
        super(RentalRepository, self).__init__()
        self._repo = Iterable()

    def get_repo(self) -> Iterable:
        """
        :return: the internal list
        """
        return self._repo

    def rent(self, new_rental: Rental) -> None:
        """
        Adds a new rental to the repository
        :param new_rental: the new rental
        """
        for rental in self._repo:
            if rental.get_rental_id() == new_rental.get_rental_id():
                raise RepositoryException("Duplicate rental ID!")

        self._repo.append(new_rental)

    def unrent(self, rental_id: int, end: str) -> None:
        """
        Unrents a book
        :param rental_id: the rental ID
        :param end: the end date of the rental
        """
        for rental in self._repo:
            if rental.get_rental_id() == rental_id:
                rental.set_returned_date(end)
                return None

        raise RepositoryException("There is no rental with the given ID!")

    def remove(self, rental_id: int) -> None:
        """
        Removes a rental from the repository
        :param rental_id: the rental ID
        """
        for rental in self._repo:
            if rental.get_rental_id() == rental_id:
                self._repo.remove(rental)
                return None

        raise RepositoryException("There is no rental with the given ID!")

    def search_rental_by_id(self, rental_id) -> Rental:
        """
        Searches for a rental by ID
        :param rental_id: the ID of the rental
        :return: the rental with the provided ID
        """
        rentals = Iterable.filter(self._repo, lambda x: x.get_rental_id() == rental_id)
        if len(rentals) == 0:
            raise RepositoryException("There is no rental with the given ID!")

        return rentals[0]

    def list(self) -> str:
        """
        :return: a string representation of the repository
        """
        value = "" if len(self._repo) > 0 else "The list of rentals is empty."
        self._repo = Iterable.sort(self._repo, lambda x, y: x.get_rental_id() > y.get_rental_id())

        for client in self._repo:
            value += (str(client) + "\n")

        return value.rstrip()


class RentalRepositoryText(RentalRepository):
    """
    A class that represents a rental repository using text files for storage
    """
    def __init__(self, file_path: str = "") -> None:
        """
        Constructor for the RentalRepository class
        :param file_path: the path to the storage file
        """
        super(RentalRepositoryText, self).__init__()
        self.__file_path = file_path

        with open(file_path, "r") as input_file:
            if os.stat(file_path).st_size > 0:
                for line in input_file:
                    line = line.strip()
                    if len(line) > 0:
                        object_string = line.split(",")
                        self._repo.append(Rental(int(object_string[0]), int(object_string[1]),
                                                 int(object_string[2]), object_string[3], object_string[4]))

    def save_data(self) -> None:
        """
        Save the data according to the currently used data type
        """
        with open(self.__file_path, "w") as output_file:
            output_file.truncate(0)
            for rental in self._repo:
                object_string = str(rental.get_rental_id()) + "," + str(rental.get_book_id()) + "," +\
                                str(rental.get_client_id()) + "," + rental.get_rented_date() + "," +\
                                rental.get_returned_date()
                output_file.write(object_string + "\n")

    def rent(self, new_rental: Rental) -> None:
        """
        Adds a new rental to the repository
        :param new_rental: the new rental
        """
        super(RentalRepositoryText, self).rent(new_rental)
        self.save_data()

    def unrent(self, rental_id: int, end: str) -> None:
        """
        Unrents a book
        :param rental_id: the rental ID
        :param end: the end date of the rental
        """
        super(RentalRepositoryText, self).unrent(rental_id, end)
        self.save_data()

    def remove(self, rental_id: int) -> None:
        """
        Removes a rental from the repository
        :param rental_id: the rental ID
        """
        super(RentalRepositoryText, self).remove(rental_id)
        self.save_data()


class RentalRepositoryBinary(RentalRepository):
    """
    A class that represents a rental repository using text files for storage
    """
    def __init__(self, file_path: str = "") -> None:
        """
        Constructor for the RentalRepository class
        :param file_path: the path to the storage file
        """
        super(RentalRepositoryBinary, self).__init__()
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

    def rent(self, new_rental: Rental) -> None:
        """
        Adds a new rental to the repository
        :param new_rental: the new rental
        """
        super(RentalRepositoryBinary, self).rent(new_rental)
        self.save_data()

    def unrent(self, rental_id: int, end: str) -> None:
        """
        Unrents a book
        :param rental_id: the rental ID
        :param end: the end date of the rental
        """
        super(RentalRepositoryBinary, self).unrent(rental_id, end)
        self.save_data()

    def remove(self, rental_id: int) -> None:
        """
        Removes a rental from the repository
        :param rental_id: the rental ID
        """
        super(RentalRepositoryBinary, self).remove(rental_id)
        self.save_data()
