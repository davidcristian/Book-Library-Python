from functools import partial
from exceptions import *


class Menu:
    """
    A class that represents the console user interface that is displayed to the user
    """

    def __init__(self, rental_service, book_service, client_service, stack_service) -> None:
        """
        Initializes the Menu class
        :param rental_service: the rental service
        :param book_service: the book service
        :param client_service: the client service
        :param stack_service: the stack service
        """
        self.__rental_service = rental_service
        self.__book_service = book_service
        self.__client_service = client_service
        self.__stack_service = stack_service

        self.__menu_options = ["Exit", "Add a book", "Remove a book", "Update a book", "List books",
                               "Add a client", "Remove a client", "Update a client", "List clients",
                               "Rent a book", "Return a book", "List rentals", "Search book by id",
                               "Search book by title", "Search book by author", "Search client by id",
                               "Search client by name", "Get most rented books", "Get most active clients",
                               "Get most rented authors", "Undo", "Redo"]

    def run(self) -> None:
        """
        Clears the console window and displays the user interface,
        then asks for input and calls the handler function
        """
        while True:
            for i in range(100):
                print()

            for i in range(len(self.__menu_options)):
                print((" " if i < 10 else "") + str(i) + ". " + self.__menu_options[i])
            print()

            option = Menu.get_input("Option: ")

            if option == 0:
                print("INFO: Quitting.\n")
                input("Press <ENTER> to continue.")

                return None

            self.handle_menu_option(option)

    def handle_menu_option(self, option: int) -> None:
        """
        Handles the given menu option using the list of complex numbers
        :param option: The menu option that was selected by the user
        """
        try:
            if option == 1:
                book_id = Menu.get_input("Book ID: ")
                title = input("Title: ")
                author = input("Author: ")

                undo_action = partial(self.__book_service.create, book_id, title, author)
                redo_action = partial(self.__book_service.delete, book_id)
                self.__stack_service.add_to_undo_stack((undo_action, redo_action))

                self.__book_service.create(book_id, title, author)
                print("INFO: You have added a new book to the repository.")
            elif option == 2:
                book_id = Menu.get_input("Book ID: ")
                book = self.__book_service.search_book_by_id(book_id)

                undo_action = partial(self.__book_service.delete, book_id)
                redo_action = partial(self.__book_service.create, book_id, book.get_title(), book.get_author())
                cascade_list = self.__rental_service.filter_rentals(None, book_id)
                self.__stack_service.add_to_undo_stack((undo_action, redo_action, cascade_list))

                self.__book_service.delete(book_id)
                print("INFO: You have deleted a book from the repository.")
            elif option == 3:
                book_id = Menu.get_input("Book ID: ")
                title = input("New Title: ")
                author = input("New Author: ")
                book = self.__book_service.search_book_by_id(book_id)

                undo_action = partial(self.__book_service.update, book_id, title, author)
                redo_action = partial(self.__book_service.update, book_id, book.get_title(), book.get_author())
                self.__stack_service.add_to_undo_stack((undo_action, redo_action))

                self.__book_service.update(book_id, title, author)
                print("INFO: You have updated the book with new information.")
            elif option == 4:
                print(self.__book_service.list())
            elif option == 5:
                client_id = Menu.get_input("Client ID: ")
                name = input("Name: ")

                undo_action = partial(self.__client_service.create, client_id, name)
                redo_action = partial(self.__client_service.delete, client_id)
                self.__stack_service.add_to_undo_stack((undo_action, redo_action))

                self.__client_service.create(client_id, name)
                print("INFO: You have added a new client to the repository.")
            elif option == 6:
                client_id = Menu.get_input("Client ID: ")
                client = self.__client_service.search_client_by_id(client_id)

                undo_action = partial(self.__client_service.delete, client_id)
                redo_action = partial(self.__client_service.create, client_id, client.get_name())
                cascade_list = self.__rental_service.filter_rentals(client_id, None)
                self.__stack_service.add_to_undo_stack((undo_action, redo_action, cascade_list))

                self.__client_service.delete(client_id)
                print("INFO: You have deleted a client from the repository.")
            elif option == 7:
                client_id = Menu.get_input("Client ID: ")
                name = input("New Name: ")
                client = self.__client_service.search_client_by_id(client_id)

                undo_action = partial(self.__client_service.update, client_id, name)
                redo_action = partial(self.__client_service.update, client_id, client.get_name())
                self.__stack_service.add_to_undo_stack((undo_action, redo_action))

                self.__client_service.update(client_id, name)
                print("INFO: You have updated the client with new information.")
            elif option == 8:
                print(self.__client_service.list())
            elif option == 9:
                rental_id = Menu.get_input("Rental ID: ")
                book_id = Menu.get_input("Book ID: ")
                client_id = Menu.get_input("Client ID: ")

                undo_action = partial(self.__rental_service.create_rental, rental_id, book_id, client_id)
                redo_action = partial(self.__rental_service.remove_rental, rental_id)
                self.__stack_service.add_to_undo_stack((undo_action, redo_action))

                self.__rental_service.create_rental(rental_id, book_id, client_id)
                print("INFO: You have added a rental to the repository.")
            elif option == 10:
                rental_id = Menu.get_input("Rental ID: ")
                rental = self.__rental_service.search_rental_by_id(rental_id)

                undo_action = partial(self.__rental_service.return_rental, rental_id)
                redo_action = partial(self.__rental_service.return_rental, rental_id, rental.get_returned_date())
                self.__stack_service.add_to_undo_stack((undo_action, redo_action))

                self.__rental_service.return_rental(rental_id)
                print("INFO: You have ended a book rental.")
            elif option == 11:
                print(self.__rental_service.list())
            elif option == 12:
                book_id = Menu.get_input("Book ID: ")
                book = self.__book_service.search_book_by_id(book_id)
                print(book)
            elif option == 13:
                title = input("Title: ")
                books = self.__book_service.search_book_by_title(title)
                for book in books:
                    print(book)
            elif option == 14:
                author = input("Author: ")
                books = self.__book_service.search_book_by_author(author)
                for book in books:
                    print(book)
            elif option == 15:
                client_id = Menu.get_input("Client ID: ")
                client = self.__client_service.search_client_by_id(client_id)
                print(client)
            elif option == 16:
                name = input("Name: ")
                clients = self.__client_service.search_client_by_name(name)
                for client in clients:
                    print(client)
            elif option == 17:
                result = self.__rental_service.get_most_rented_books()
                print(result if len(result) > 0 else "INFO: There are no rented books in the repository.")
            elif option == 18:
                result = self.__rental_service.get_most_active_clients()
                print(result if len(result) > 0 else "INFO: There are no active clients in the repository.")
            elif option == 19:
                result = self.__rental_service.get_most_rented_authors()
                print(result if len(result) > 0 else "INFO: There are no rented authors in the repository.")
            elif option == 20:
                self.__stack_service.undo_operation()
                print("INFO: You have undone the previous operation.")
            elif option == 21:
                self.__stack_service.redo_operation()
                print("INFO: You have redone the previously undone operation.")
        except (BookException, ClientException, RentalException, RepositoryException) as e:
            print(f"ERROR: {e}")
        except StackException as e:
            print(f"ERROR: {e}")
        except ValueError:
            print("ERROR: Invalid parameter type!")
        except IndexError:
            print("ERROR: Invalid index reached!")

        print()
        input("Press <ENTER> to continue.")

    @staticmethod
    def get_input(prompt: str) -> int:
        """
        Gets an integer input from the user
        :param prompt: the prompt that is shown to the user for input
        :return: a valid integer
        """
        while True:
            try:
                value = int(input(prompt))
                return value
            except ValueError:
                print()
                print("ERROR: Invalid input!")
