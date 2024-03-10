import unittest

from domain import Client
from repository import ClientRepository


class ClientRepositoryTest(unittest.TestCase):
    """
    A class that tests the ClientRepository class
    """
    def test_add(self) -> None:
        """
        Tests the add() function
        """
        client_repository = ClientRepository()

        client1 = Client(0, "test")
        client2 = Client(1, "test")
        client3 = Client(2, "test")

        client_repository.add(client1)
        self.assertEqual(client_repository.get_repo(), [client1])

        client_repository.add(client2)
        self.assertEqual(client_repository.get_repo(), [client1, client2])

        client_repository.add(client3)
        self.assertEqual(client_repository.get_repo(), [client1, client2, client3])

    def test_remove(self) -> None:
        """
        Tests the remove() function
        """
        client_repository = ClientRepository()

        client1 = Client(0, "test")
        client2 = Client(1, "test")
        client3 = Client(2, "test")

        client_repository.add(client1)
        client_repository.add(client2)
        client_repository.add(client3)

        self.assertEqual(client_repository.get_repo(), [client1, client2, client3])

        client_repository.remove(1)
        self.assertEqual(client_repository.get_repo(), [client1, client3])

        client_repository.remove(0)
        self.assertEqual(client_repository.get_repo(), [client3])

        client_repository.remove(2)
        self.assertEqual(client_repository.get_repo(), [])

    def test_update(self) -> None:
        """
        Tests the update() function
        """
        client_repository = ClientRepository()

        client1 = Client(0, "test")
        client2 = Client(1, "test")
        client3 = Client(2, "test")

        client_repository.add(client1)
        client_repository.add(client2)
        client_repository.add(client3)

        client_repository.update(1, "test2")
        self.assertEqual(client_repository.get_repo()[1].get_name(), "test2")

        client_repository.update(0, "test4")
        self.assertEqual(client_repository.get_repo()[0].get_name(), "test4")

        client_repository.update(2, "test6")
        self.assertEqual(client_repository.get_repo()[2].get_name(), "test6")

    def test_search_client_by_id(self) -> None:
        """
        Tests the search_client_by_id() function
        """
        client_repository = ClientRepository()

        client1 = Client(0, "test1")
        client2 = Client(1, "test2")
        client3 = Client(2, "test3")

        client_repository.add(client1)
        client_repository.add(client2)
        client_repository.add(client3)

        self.assertEqual(client_repository.search_client_by_id(0), client1)
        self.assertEqual(client_repository.search_client_by_id(1), client2)
        self.assertEqual(client_repository.search_client_by_id(2), client3)

    def test_search_client_by_name(self) -> None:
        """
        Tests the search_client_by_name() function
        """
        client_repository = ClientRepository()

        client1 = Client(0, "test1")
        client2 = Client(1, "test2")
        client3 = Client(2, "test3")

        client_repository.add(client1)
        client_repository.add(client2)
        client_repository.add(client3)

        self.assertEqual(client_repository.search_client_by_name("st1"), [client1])
        self.assertEqual(client_repository.search_client_by_name("st2"), [client2])
        self.assertEqual(client_repository.search_client_by_name("est"), [client1, client2, client3])
