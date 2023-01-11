import unittest
from utils import Iterable


class IterableTest(unittest.TestCase):
    """
    A class that handles the testing of the Iterable class
    """
    def test_class(self) -> None:
        iterable = Iterable()
        iterable.append(1)
        self.assertEqual(iterable, [1])

        iterable[1] = 1
        self.assertEqual(iterable, [1, 1])

        iterable[0] = 0
        self.assertEqual(iterable, [0, 1])

        del iterable[1]
        self.assertEqual(iterable, [0])
        iterable.remove(0)

        try:
            iterable[1] = 1
        except IndexError:
            pass

        iterable.append(0)
        self.assertEqual(len(iterable), 1)
        iterable.append(1)
        iterable.append(2)
        iterable.append(3)
        iterable.append(4)
        iterable.append(5)

        sorted_iterable = Iterable.sort(iterable, lambda x, y: x >= y)
        self.assertEqual(sorted_iterable, [0, 1, 2, 3, 4, 5])

        sorted_iterable = Iterable.sort(iterable, lambda x, y: x < y)
        self.assertEqual(sorted_iterable, [5, 4, 3, 2, 1, 0])

        filtered_iterable = Iterable.filter(iterable, lambda x: x % 2 == 0)
        self.assertEqual(filtered_iterable, [0, 2, 4])

        filtered_iterable = Iterable.filter(iterable, lambda x: x % 2 == 1)
        self.assertEqual(filtered_iterable, [1, 3, 5])
