import unittest
from domain import Book


class BookTest(unittest.TestCase):
    """
    A class that handles the testing of the Book class
    """
    def test_get_book_id(self) -> None:
        """
        Tests the get_book_id() function
        """
        book1 = Book(0, "test", "test")
        book2 = Book(1, "test", "test")
        book3 = Book(2, "test", "test")

        self.assertEqual(book1.get_book_id(), 0)
        self.assertEqual(book2.get_book_id(), 1)
        self.assertEqual(book3.get_book_id(), 2)

    def test_set_book_id(self) -> None:
        """
        Tests the set_book_id() function
        """
        book1 = Book(0, "test", "test")
        book2 = Book(1, "test", "test")
        book3 = Book(2, "test", "test")

        book1.set_book_id(3)
        book2.set_book_id(4)
        book3.set_book_id(5)

        self.assertEqual(book1.get_book_id(), 3)
        self.assertEqual(book2.get_book_id(), 4)
        self.assertEqual(book3.get_book_id(), 5)

    def test_get_title(self) -> None:
        """
        Tests the get_title() function
        """
        book1 = Book(0, "test1", "test")
        book2 = Book(1, "test2", "test")
        book3 = Book(2, "test3", "test")

        self.assertEqual(book1.get_title(), "test1")
        self.assertEqual(book2.get_title(), "test2")
        self.assertEqual(book3.get_title(), "test3")

    def test_set_title(self) -> None:
        """
        Tests the set_title() function
        """
        book1 = Book(0, "test1", "test")
        book2 = Book(1, "test2", "test")
        book3 = Book(2, "test3", "test")

        book1.set_title("test4")
        book2.set_title("test5")
        book3.set_title("test6")

        self.assertEqual(book1.get_title(), "test4")
        self.assertEqual(book2.get_title(), "test5")
        self.assertEqual(book3.get_title(), "test6")

    def test_get_author(self) -> None:
        """
        Tests the get_author() function
        """
        book1 = Book(0, "test", "test1")
        book2 = Book(1, "test", "test2")
        book3 = Book(2, "test", "test3")

        self.assertEqual(book1.get_author(), "test1")
        self.assertEqual(book2.get_author(), "test2")
        self.assertEqual(book3.get_author(), "test3")

    def test_set_author(self) -> None:
        """
        Tests the set_author() function
        """
        book1 = Book(0, "test", "test1")
        book2 = Book(1, "test", "test2")
        book3 = Book(2, "test", "test3")

        book1.set_author("test4")
        book2.set_author("test5")
        book3.set_author("test6")

        self.assertEqual(book1.get_author(), "test4")
        self.assertEqual(book2.get_author(), "test5")
        self.assertEqual(book3.get_author(), "test6")
