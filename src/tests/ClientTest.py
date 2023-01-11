import unittest
from domain import Client


class ClientTest(unittest.TestCase):
    """
    A class that handles the testing of the Client class
    """
    def test_get_client_id(self) -> None:
        """
        Tests the get_client_id() function
        """
        client1 = Client(0, "test1")
        client2 = Client(1, "test2")
        client3 = Client(2, "test3")

        self.assertEqual(client1.get_client_id(), 0)
        self.assertEqual(client2.get_client_id(), 1)
        self.assertEqual(client3.get_client_id(), 2)

    def test_set_client_id(self) -> None:
        """
        Tests the set_client_id() function
        """
        client1 = Client(0, "test1")
        client2 = Client(1, "test2")
        client3 = Client(2, "test3")

        client1.set_client_id(3)
        client2.set_client_id(4)
        client3.set_client_id(5)

        self.assertEqual(client1.get_client_id(), 3)
        self.assertEqual(client2.get_client_id(), 4)
        self.assertEqual(client3.get_client_id(), 5)

    def test_get_name(self) -> None:
        """
        Tests the get_name() function
        """
        client1 = Client(0, "test1")
        client2 = Client(1, "test2")
        client3 = Client(2, "test3")

        self.assertEqual(client1.get_name(), "test1")
        self.assertEqual(client2.get_name(), "test2")
        self.assertEqual(client3.get_name(), "test3")

    def test_set_name(self) -> None:
        """
        Tests the set_name() function
        """
        client1 = Client(0, "test1")
        client2 = Client(1, "test2")
        client3 = Client(2, "test3")

        client1.set_name("test4")
        client2.set_name("test5")
        client3.set_name("test6")

        self.assertEqual(client1.get_name(), "test4")
        self.assertEqual(client2.get_name(), "test5")
        self.assertEqual(client3.get_name(), "test6")
