### 4. Library
Write an application for a book library. The application will store:
- **Book**: `book_id`, `title`, `author`
- **Client**: `client_id`, `name`
- **Rental**: `rental_id`, `book_id`, `client_id`, `rented_date`, `returned_date`

Create an application to:
1. Manage clients and books. The user can add, remove, update, and list both clients and books.
2. Rent or return a book. A client can rent an available book. A client can return a rented book at any time. Only available books (those which are not currently rented) can be rented.
3. Search for clients or books using any one of their fields (e.g. books can be searched for using id, title or author). The search must work using case-insensitive, partial string matching, and must return all matching items.
4. Create statistics:
    - Most rented books. This will provide the list of books, sorted in descending order of the number of times they were rented.
    - Most active clients. This will provide the list of clients, sorted in descending order of the number of book rental days they have (e.g. having 2 rented books for 3 days each counts as 2 x 3 = 6 days).
    - Most rented author. This provides the list of book authors, sorted in descending order of the number of rentals their books have.
5. Unlimited undo/redo functionality. Each step will undo/redo the previous operation performed by the user. Undo/redo operations must cascade and have a memory-efficient implementation (no superfluous list copying).

### Iterable Data Structure

Create a Python module that contains an iterable data structure, a sort method and a filter method, together with complete PyUnit unit tests (100% coverage). The module must be reusable in other projects.

## What you will need to do
- Implement an iterable data structure. Study the [`__setItem__`](https://docs.python.org/3/reference/datamodel.html#object),`__getitem__`, `__delItem__`, `__next__` and `__iter__` Python methods.
- Implement a sorting algorithm that was not/will not be studied during the lecture or seminar (no bubble sort, cocktail sort, merge sort, insert sort, quicksort). You can use one of shell sort, comb sort, bingo sort, gnome sort, or other sorting method. Prove that you understand the sorting method implemented. The sort function will accept two parameters: the list to be sorted as well as a comparison function used to determine the order between two elements.
- Implement a filter function that can be used to filter the elements from a list. The function will use 2 parameters: the list to be filtered, and an acceptance function that decided whether a given value passes the filter.
