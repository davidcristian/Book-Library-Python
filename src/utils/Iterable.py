

class Iterable:
    """
    A class that implements an iterable data structure
    """

    def __init__(self) -> None:
        """
        Initialize the class
        """
        self.__data = list()

    @staticmethod
    def sort(data, comparison_function) -> list:
        """
        Sorts the data using comb sort (basically bubble sort but initially with a gap
        that is higher than 1 to eliminate small values near the end of the list. The
        gap grows smaller at a scale of 1.3 every iteration)
        :param data: the data to be sorted
        :param comparison_function: the function used to compare two values
        :return: sorted data
        """
        data_copy = data[:]

        gap = len(data_copy)
        swap = True
        while gap > 1 or swap:
            gap = max(1, int(gap / 1.3))
            swap = False

            for i in range(len(data_copy) - gap):
                j = i + gap
                if comparison_function(data_copy[i], data_copy[j]):
                    data_copy[i], data_copy[j] = data_copy[j], data_copy[i]
                    swap = True

        return data_copy

    @staticmethod
    def filter(data, filter_function) -> list:
        """
        Filters the data
        :param data: the data to be filtered
        :param filter_function: the function used to decide if a value passes the filter
        :return: the filtered data
        """
        filtered = list()
        for value in data:
            if filter_function(value):
                filtered.append(value)

        return filtered

    def append(self, value: object) -> None:
        """
        Appends a value at the end of the list
        :param value: the value
        """
        self.__setitem__(len(self.__data), value)

    def remove(self, key: int) -> None:
        """
        Deletes an item at the given index
        :param key: the given index
        """
        self.__delitem__(key)

    def __setitem__(self, key: int, value: object) -> None:
        """
        Sets the item at the given key to the given value
        :param key: the index
        :param value: the value
        """
        if key < len(self.__data):
            self.__data[key] = value
        elif key == len(self.__data):
            self.__data.append(value)
        else:
            raise IndexError

    def __getitem__(self, item: int) -> object:
        """
        Returns an item at an index
        :param item: the given index
        :return: the item at the given index
        """
        return self.__data[item]

    def __delitem__(self, key: int) -> None:
        """
        Deletes an item at the given index
        :param key: the given index
        """
        self.__data.remove(key)

    def __next__(self) -> object:
        """
        :return: the next element during an iteration
        """
        if self.__iterator < len(self.__data) - 1:
            self.__iterator += 1
            return self.__data[self.__iterator]
        else:
            raise StopIteration

    def __iter__(self) -> object:
        """
        Initializes the iterator
        :return: the object to be iterated (self)
        """
        self.__iterator = -1
        return self

    def __len__(self) -> int:
        """
        :return: the length of the data
        """
        return len(self.__data)

    def __eq__(self, other) -> bool:
        """
        :return: whether 2 sets of data are equal
        """
        return self.__data == other
