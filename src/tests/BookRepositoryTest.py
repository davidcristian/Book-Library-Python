import unittest

from domain import Book
from repository import BookRepository


class BookRepositoryTest(unittest.TestCase):
    """
    A class that tests the BookRepository class
    """
    def test_add(self) -> None:
        """
        Tests the add() function
        """
        book_repository = BookRepository()

        book1 = Book(0, "test", "test")
        book2 = Book(1, "test", "test")
        book3 = Book(2, "test", "test")

        book_repository.add(book1)
        self.assertEqual(book_repository.get_repo(), [book1])

        book_repository.add(book2)
        self.assertEqual(book_repository.get_repo(), [book1, book2])

        book_repository.add(book3)
        self.assertEqual(book_repository.get_repo(), [book1, book2, book3])

    def test_remove(self) -> None:
        """
        Tests the remove() function
        """
        book_repository = BookRepository()

        book1 = Book(0, "test", "test")
        book2 = Book(1, "test", "test")
        book3 = Book(2, "test", "test")

        book_repository.add(book1)
        book_repository.add(book2)
        book_repository.add(book3)

        self.assertEqual(book_repository.get_repo(), [book1, book2, book3])

        book_repository.remove(1)
        self.assertEqual(book_repository.get_repo(), [book1, book3])

        book_repository.remove(0)
        self.assertEqual(book_repository.get_repo(), [book3])

        book_repository.remove(2)
        self.assertEqual(book_repository.get_repo(), [])

    def test_update(self) -> None:
        """
        Tests the update() function
        """
        book_repository = BookRepository()

        book1 = Book(0, "test", "test")
        book2 = Book(1, "test", "test")
        book3 = Book(2, "test", "test")

        book_repository.add(book1)
        book_repository.add(book2)
        book_repository.add(book3)

        book_repository.update(1, "test2", "test3")
        self.assertEqual(book_repository.get_repo()[1].get_title(), "test2")
        self.assertEqual(book_repository.get_repo()[1].get_author(), "test3")

        book_repository.update(0, "test4", "test5")
        self.assertEqual(book_repository.get_repo()[0].get_title(), "test4")
        self.assertEqual(book_repository.get_repo()[0].get_author(), "test5")

        book_repository.update(2, "test6", "test7")
        self.assertEqual(book_repository.get_repo()[2].get_title(), "test6")
        self.assertEqual(book_repository.get_repo()[2].get_author(), "test7")

    def test_search_book_by_id(self) -> None:
        """
        Tests the search_book_by_id() function
        """
        book_repository = BookRepository()

        book1 = Book(0, "test1", "test1")
        book2 = Book(1, "test2", "test2")
        book3 = Book(2, "test3", "test3")

        book_repository.add(book1)
        book_repository.add(book2)
        book_repository.add(book3)

        self.assertEqual(book_repository.search_book_by_id(0), [book1])
        self.assertEqual(book_repository.search_book_by_id(1), [book2])
        self.assertEqual(book_repository.search_book_by_id(2), [book3])

    def test_search_book_by_title(self) -> None:
        """
        Tests the search_book_by_title() function
        """
        book_repository = BookRepository()

        book1 = Book(0, "test1", "test1")
        book2 = Book(1, "test2", "test2")
        book3 = Book(2, "test3", "test3")

        book_repository.add(book1)
        book_repository.add(book2)
        book_repository.add(book3)

        self.assertEqual(book_repository.search_book_by_title("st1"), [book1])
        self.assertEqual(book_repository.search_book_by_title("st2"), [book2])
        self.assertEqual(book_repository.search_book_by_title("est"), [book1, book2, book3])

    def test_search_book_by_author(self) -> None:
        """
        Tests the search_book_by_author() function
        """
        book_repository = BookRepository()

        book1 = Book(0, "test1", "test1")
        book2 = Book(1, "test2", "test2")
        book3 = Book(2, "test3", "test3")

        book_repository.add(book1)
        book_repository.add(book2)
        book_repository.add(book3)

        self.assertEqual(book_repository.search_book_by_author("st1"), [book1])
        self.assertEqual(book_repository.search_book_by_author("st2"), [book2])
        self.assertEqual(book_repository.search_book_by_author("est"), [book1, book2, book3])
