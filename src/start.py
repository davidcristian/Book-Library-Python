#!/usr/bin/env python3

import pathlib
import configparser

from src.ui.Menu import Menu
from src.repository.BookRepository import BookRepository
from src.repository.BookRepository import BookRepositoryText
from src.repository.BookRepository import BookRepositoryBinary
from src.repository.ClientRepository import ClientRepository
from src.repository.ClientRepository import ClientRepositoryText
from src.repository.ClientRepository import ClientRepositoryBinary
from src.repository.RentalRepository import RentalRepository
from src.repository.RentalRepository import RentalRepositoryText
from src.repository.RentalRepository import RentalRepositoryBinary

from src.services.BookService import BookService
from src.services.ClientService import ClientService
from src.services.RentalService import RentalService
from src.services.StackService import StackService


# Program entry point
def main():
    config_file = configparser.RawConfigParser()
    config_file.read('settings.properties')
    config = config_file['DEFAULT']

    main_path = str(pathlib.Path(__file__).parent.resolve()) + '\\resources\\'
    data_type = config['repository']

    rentals_file = main_path + config['rentals'].strip().lower().replace('"', '')
    books_file = main_path + config['books'].strip().lower().replace('"', '')
    clients_file = main_path + config['clients'].strip().lower().replace('"', '')

    if data_type == 'textfiles':
        rental_repo = RentalRepositoryText(rentals_file)
        book_repo = BookRepositoryText(books_file)
        client_repo = ClientRepositoryText(clients_file)
    elif data_type == 'binaryfiles':
        rental_repo = RentalRepositoryBinary(rentals_file)
        book_repo = BookRepositoryBinary(books_file)
        client_repo = ClientRepositoryBinary(clients_file)
    else:  # Default to inmemory
        rental_repo = RentalRepository()
        book_repo = BookRepository()
        client_repo = ClientRepository()

    rental_service = RentalService(rental_repo, book_repo, client_repo, preload=data_type == 'inmemory')
    book_service = BookService(book_repo, rental_service, preload=data_type == 'inmemory')
    client_service = ClientService(client_repo, rental_service, preload=data_type == 'inmemory')
    stack_service = StackService(rental_repo)

    menu = Menu(rental_service, book_service, client_service, stack_service)
    menu.display_menu()


# Execute the main function
# if this file is ran directly
if __name__ == "__main__":
    main()
