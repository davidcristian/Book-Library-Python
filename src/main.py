#!/usr/bin/env python3

import os
import configparser

from repository import (
    BookRepository, BookRepositoryText, BookRepositoryBinary,
    ClientRepository, ClientRepositoryText, ClientRepositoryBinary,
    RentalRepository, RentalRepositoryText, RentalRepositoryBinary,
)

from service import BookService, ClientService, RentalService, StackService
from ui import Menu


# Program entry point
def main() -> None:
    parser = configparser.RawConfigParser()
    parser.read("settings.properties")
    config_key = "default"

    data_type = parser.get(config_key, "repository")

    try:
        extension = parser.get(config_key, f"{data_type}_extension")
    except configparser.NoOptionError:
        extension = ""

    rentals_file = os.path.realpath(parser.get(config_key, "rentals_file") + extension)
    books_file = os.path.realpath(parser.get(config_key, "books_file") + extension)
    clients_file = os.path.realpath(parser.get(config_key, "clients_file") + extension)

    if data_type == "text":
        rental_repo = RentalRepositoryText(rentals_file)
        book_repo = BookRepositoryText(books_file)
        client_repo = ClientRepositoryText(clients_file)
    elif data_type == "binary":
        rental_repo = RentalRepositoryBinary(rentals_file)
        book_repo = BookRepositoryBinary(books_file)
        client_repo = ClientRepositoryBinary(clients_file)
    else:  # Default to in-memory
        rental_repo = RentalRepository()
        book_repo = BookRepository()
        client_repo = ClientRepository()

    rental_service = RentalService(rental_repo, book_repo, client_repo)
    book_service = BookService(book_repo, rental_service)
    client_service = ClientService(client_repo, rental_service)
    stack_service = StackService(rental_repo)

    menu = Menu(rental_service, book_service, client_service, stack_service)
    menu.run()


# Execute the main function
# if this file is ran directly
if __name__ == "__main__":
    main()
