import unittest

from domain import Rental
from repository import RentalRepository


class RentalRepositoryTest(unittest.TestCase):
    """
    A class that tests the RentalRepository class
    """
    def test_rent(self) -> None:
        """
        Tests the rent() function
        """
        rental_repository = RentalRepository()

        rental1 = Rental(0, 5, 10, "2021/11/14", "-1")
        rental2 = Rental(1, 10, 15, "2021/11/15", "-1")
        rental3 = Rental(2, 15, 20, "2021/11/16", "-1")

        rental_repository.rent(rental1)
        self.assertEqual(rental_repository.get_repo(), [rental1])

        rental_repository.rent(rental2)
        self.assertEqual(rental_repository.get_repo(), [rental1, rental2])

        rental_repository.rent(rental3)
        self.assertEqual(rental_repository.get_repo(), [rental1, rental2, rental3])

    def test_unrent(self) -> None:
        """
        Tests the unrent() function
        """
        rental_repository = RentalRepository()

        rental1 = Rental(0, 5, 10, "2021/11/11", "-1")
        rental2 = Rental(1, 10, 15, "2021/11/12", "-1")
        rental3 = Rental(2, 15, 20, "2021/11/13", "-1")

        rental_repository.rent(rental1)
        rental_repository.rent(rental2)
        rental_repository.rent(rental3)

        rental_repository.unrent(1, "2021/11/14")
        self.assertEqual(rental_repository.get_repo()[1].get_returned_date(), "2021/11/14")

        rental_repository.unrent(0, "2021/11/15")
        self.assertEqual(rental_repository.get_repo()[0].get_returned_date(), "2021/11/15")

        rental_repository.unrent(2, "2021/11/16")
        self.assertEqual(rental_repository.get_repo()[2].get_returned_date(), "2021/11/16")

    def test_remove(self) -> None:
        """
        Tests the remove() function
        """
        rental_repository = RentalRepository()

        rental1 = Rental(0, 5, 10, "2021/11/14", "-1")
        rental2 = Rental(1, 10, 15, "2021/11/15", "-1")
        rental3 = Rental(2, 15, 20, "2021/11/16", "-1")

        rental_repository.rent(rental1)
        rental_repository.rent(rental2)
        rental_repository.rent(rental3)

        self.assertEqual(rental_repository.get_repo(), [rental1, rental2, rental3])

        rental_repository.remove(1)
        self.assertEqual(rental_repository.get_repo(), [rental1, rental3])

        rental_repository.remove(0)
        self.assertEqual(rental_repository.get_repo(), [rental3])

        rental_repository.remove(2)
        self.assertEqual(rental_repository.get_repo(), [])
