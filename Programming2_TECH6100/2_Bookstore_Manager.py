# Importing ABC and abstract method to implement abstraction in classes
from abc import ABC, abstractmethod

# Importing datetime to create duedate
from datetime import datetime

# Importing random and string to create password generator
import random
import string

# Importing re to use it in email validation
import re


# Main is shown in here to provide an easy understanding of the code structure
# Conventionally it usually goes below the class definitions
def main():
    # Creating object for class BookstoreSystem that provides function for every option
    system = BookstoreSystem()
    print("\nWelcome to  Bookiverse, your favourite online bookstore manager.")
    while True:
        print("\nPlease, enter numbers 1 to 9 to execute one of the below options:")
        print("1. Add Book")
        print("2. Remove Book")
        print("3. Add User")
        print("4. Remove User")
        print("5. Create Order")
        print("6. Remove Order")
        print("7. Search Tool")
        print("8. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            system.add_book()
        elif choice == "2":
            system.remove_book()
        elif choice == "3":
            system.add_user()
        elif choice == "4":
            system.remove_user()
        elif choice == "5":
            system.create_order()
        elif choice == "6":
            system.remove_order()
        elif choice == "7":
            system.search()
        elif choice == "8":
            print("Exiting the bookstore manager...")
            break
        else:
            print("Invalid option, please try again.")


# Parent class Book
# Books attributes mean to be protected, they are internal
class Book(ABC):
    def __init__(self, title, author, isbn, price, quantity):
        self._title = title
        self._author = author
        # In this case ISBN is used as an id, but it is not unique for each particular book like in real life.
        # This way we can group several books that are the same under the same "id".
        self._isbn = isbn
        self._price = price
        self._quantity = quantity
        self._type = self.__class__.__name__
        # self._status = "available"
        # self._dueDate = None

    # Using property to access class attributes easily later
    @property
    def title(self):
        return self._title

    @property
    def author(self):
        return self._author

    @property
    def isbn(self):
        return self._isbn

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, new_price):
        if new_price > 0:
            self._price = new_price
        else:
            print("Price must be greater than zero")

    @property
    def quantity(self):
        return self._quantity

    @quantity.setter
    def quantity(self, new_quantity):
        if new_quantity >= 0:
            self._quantity = new_quantity
        else:
            print("Quantity must be a positive number")

    @property
    def type(self):
        return self._type

    # Using this decorator for abstraction as the method might be different in the child classes
    # In each child __repr__ is fulfilled and it is not "abstract" anymore
    @abstractmethod
    def __repr__(self):
        pass


# Using inheritance to implement book classification with Book as a parent
# Fiction child class inherits book class and allows to add a subtype of fiction book
# Sci-Fi child class has not been created as it is a subclass of Fiction
class Fiction(Book):
    def __init__(self, title, author, isbn, price, quantity, subtype):
        super().__init__(title, author, isbn, price, quantity)
        self._subtype = subtype

    # Keep using the decorator to maintain consistency along the code
    @property
    def subtype(self):
        return self._subtype

    def __repr__(self):
        return str({
            "title": self.title,
            "author": self.author,
            "isbn": self.isbn,
            "price": self.price,
            "quantity": self.quantity,
            # combining type and subtype
            "type": f"{self.type} ({self.subtype})"
        })


# NonFiction child class inherits book class
class NonFiction(Book):
    def __repr__(self):
        return str({
            "title": self.title,
            "author": self.author,
            "isbn": self.isbn,
            "price": self.price,
            "quantity": self.quantity,
            "type": self.type
        })


# Biography child class inherits book class and adds person as attribute
class Biography(Book):
    def __init__(self, title, author, isbn, price, quantity, person):
        super().__init__(title, author, isbn, price, quantity)
        self._person = person

    @property
    def person(self):
        return self._person

    def __repr__(self):
        return str({
            "title": self.title,
            "author": self.author,
            "isbn": self.isbn,
            "price": self.price,
            "quantity": self.quantity,
            "type": self.type,
            "biography about": self.person
        })


# Business child class inherits book class
class Business(Book):
    def __repr__(self):
        return str({
            "title": self.title,
            "author": self.author,
            "isbn": self.isbn,
            "price": self.price,
            "quantity": self.quantity,
            "type": self.type
        })


# Science child class inherits book class
class Science(Book):
    def __init__(self, title, author, isbn, price, quantity, field):
        super().__init__(title, author, isbn, price, quantity)
        self._field = field

    @property
    def field(self):
        return self._field

    def __repr__(self):
        return str({
            "title": self.title,
            "author": self.author,
            "isbn": self.isbn,
            "price": self.price,
            "quantity": self.quantity,
            "type": self.type,
            "field": self.field
        })


# Cooking child inherits book class and add cuisine type attribute
class Cooking(Book):
    def __init__(self, title, author, isbn, price, quantity, cuisine):
        super().__init__(title, author, isbn, price, quantity)
        self._cuisine = cuisine

    @property
    def cuisine(self):
        return self._cuisine

    def __repr__(self):
        return str({
            "title": self.title,
            "author": self.author,
            "isbn": self.isbn,
            "price": self.price,
            "quantity": self.quantity,
            "type": self.type,
            "cuisine": self.cuisine
        })


# GraphicNovel inherits book class
class GraphicNovel(Book):
    def __repr__(self):
        return str({
            "title": self.title,
            "author": self.author,
            "isbn": self.isbn,
            "price": self.price,
            "quantity": self.quantity,
            "type": self.type
        })


# Mystery child inherits book class
class Mystery(Book):
    def __repr__(self):
        return str({
            "title": self.title,
            "author": self.author,
            "isbn": self.isbn,
            "price": self.price,
            "quantity": self.quantity,
            "type": self.type
        })


# Parent abstract class User
class User(ABC):
    def __init__(self, user_id, username, email, password):
        self._user_id = user_id
        self._username = username
        self._email = email
        # private attribute
        self.__password = password

    @property
    def user_id(self):
        return self._user_id

    @property
    def username(self):
        return self._username

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, new_email):
        self._email = new_email

    @property
    def password(self):
        return self.__password

    def set_password(self, new_password):
        self.__password = new_password

    # Using this decorator as the method might be different in the different child classes
    @abstractmethod
    def __repr__(self):
        pass


# Child class Buyer
class Buyer(User):
    def __repr__(self):
        return str({
            "Buyer_id": self.user_id,
            "Buyer_name": self.username,
            "Buyer_mail": self.email
        })


# Child class manager
class Manager(User):
    def __repr__(self):
        return str({
            "Manager_id": self.user_id,
            "Manager_name": self.username,
            "Manager_email": self.email
        })


# Class Order to generate future "order transaction" objects
class Order:
    _count_id = 1

    def __init__(self, user, book, quantity):
        self._order_id = self._count_id
        Order._count_id += 1
        self._user = user
        self._book = book
        self._quantity = quantity
        self._order_date = datetime.now()

    @property
    def order_id(self):
        return self._order_id

    @property
    def user(self):
        return self._user

    @property
    def book(self):
        return self._book

    @property
    def quantity(self):
        return self._quantity

    @quantity.setter
    def quantity(self, new_quantity):
        self._quantity = new_quantity

    def __repr__(self):
        return str({
            "order_id": self.order_id,
            "user": self.user.username,
            "book": self.book.title,
            "ISBN": self.book.isbn,
            "quantity": self.quantity,
            # using library to display date and time
            "order_date": self._order_date.strftime("%Y-%m-%d %H:%M:%S")
            })


# BookstoreSystem class where functions that help managing the system are created as methods
class BookstoreSystem:
    def __init__(self):
        # As we do not have a db we use lists to store class objects
        self.books = []
        self.users = []
        self.orders = []

    # Method to create and add a book into "BookstoreSystem.books" (self.books)
    def add_book(self):
        print("Adding a new book:")
        # Use of .strip to clear space at the beginning or the end of the strings
        # Adding some data validation
        while True:
            # Allowing the user to exit for every input is asked
            title = input("Enter the title (or 'exit' to cancel): ").strip()
            if title.lower() == "exit":
                return
            if title:
                break
            print("Empty field, please try again.")

        while True:
            author = input("Enter the author (or 'exit' to cancel): ").strip()
            if author.lower() == "exit":
                return
            if author:
                break
            print("Empty field, please try again.")

        while True:
            try:
                isbn = input("Enter the ISBN (or 'exit' to cancel): ").strip()
                if isbn.lower() == "exit":
                    return
                # ISBN are usually numbers separated by "-"
                isbn = int(isbn.replace("-", ""))
                if not isbn:
                    print("Empty field, please try again.")
                # Checking if isbn is repeated in our list of books
                elif any(book.isbn == isbn for book in self.books):
                    print("A book with the same ISBN already exists, please try again.")
                else:
                    break
            except ValueError:
                print("The ISBN is not correct")

        while True:
            try:
                price = input("Enter the price (or 'exit' to cancel): ").strip()
                if price.lower() == "exit":
                    return
                price = float(price)
                if price > 0:
                    break
                print("Please, enter a price greater than 0.")
            except ValueError:
                print("Invalid price, please enter a valid number.")

        while True:
            try:
                quantity = input("Enter the quantity (or 'exit' to cancel): ").strip()
                if quantity.lower() == "exit":
                    return
                quantity = int(quantity)
                if quantity > 0:
                    break
                print("Quantity must be positive.")
            except ValueError:
                print("Invalid quantity. Please enter a whole number.")

        predefined_types = ["Fiction", "NonFiction", "Biography", "Business", "Science", "Cooking", "GraphicNovel", "Mystery"]
        while True:
            book_type = input(f"Enter one of the following book types (or 'exit' to cancel):\n{predefined_types} ").strip()
            if book_type.lower() == "exit":
                return
            if book_type in predefined_types:
                break
            print("Invalid book type, please enter a valid type.")

        # Create appropriate book object
        if book_type == "Fiction":
            subtype = input("Enter fiction subtype: ").strip()
            new_book = Fiction(title, author, isbn, price, quantity, subtype)
        elif book_type == "NonFiction":
            new_book = NonFiction(title, author, isbn, price, quantity)
        elif book_type == "Biography":
            person = input("Enter person the biography is about: ").strip()
            new_book = Biography(title, author, isbn, price, quantity, person)
        elif book_type == "Business":
            new_book = Business(title, author, isbn, price, quantity)
        elif book_type == "Science":
            new_book = Science(title, author, isbn, price, quantity, field)
        elif book_type == "Cooking":
            cuisine = input("Enter cuisine type: ").strip()
            new_book = Cooking(title, author, isbn, price, quantity, cuisine)
        elif book_type == "GraphicNovel":
            new_book = GraphicNovel(title, author, isbn, price, quantity)
        # Case book_type == "Mystery":
        else:
            new_book = Mystery(title, author, isbn, price, quantity)

        self.books.append(new_book)
        print("Book added successfully.")

    # Method to remove an already created book object from "BookstoreSystem.books" list (self.books)
    def remove_book(self):
        print("\nRemoving a book:")
        if not self.books:
            print("There are no books to remove.")
            return
        while True:
            try:
                isbn = input("Enter a ISBN to delete a book (or 'exit' to cancel): ").strip()
                if isbn.lower() == "exit":
                    return
                isbn = int(isbn.replace("-", ""))
                if not isbn:
                    print("Empty field, please try again.")
                    continue
                book_found = False
                for b in self.books:
                    if b.isbn == isbn:
                        book = b
                        self.books.remove(book)
                        print(f"{book.title} has been removed from the store.")
                        book_found = True
                        break
                if book_found:
                    break
                else:
                    print("Book not found.")
            except ValueError:
                print("The ISBN is not correct")

    # Method to create and add user object into "BookstoreSystem.users" list (self.users)
    def add_user(self):
        print("\nAdding a new user:")
        while True:
            username = input("Enter username: ").strip()
            if username:
                break
            print("Username field is empty.")

        while True:
            email = input("Enter user's email:").strip()
            if email.lower() == "exit":
                return
            # If email does not match email format:
            # Characters except "@" + "@" + characters except "@" + "." + characters except "@"
            if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
                print("Invalid email format.")
                continue
            if any(u.email == email for u in self.users):
                print("Email already exists. Please try another one.")
                continue
            break

        #  Creating user_id
        user_id = len(self.users) + 1
        # Password generator
        # Includes alphabetical, numerical and punctuation characters
        characters = string.ascii_letters + string.digits + string.punctuation
        # Selects random character from the "characters" list
        # Populates string (initially empty) in 16 iterations with that character
        password = ''.join(random.choice(characters) for _ in range(16))
        # Creating object
        new_user = Buyer(user_id, username, email, password)
        self.users.append(new_user)
        print("User added successfully.")

    # Method to remove an already created user object from "BookstoreSystem.users" list (self.users)
    def remove_user(self):
        print("\nRemoving User:")
        while True:
            user_id = input("Enter the ID of the user (or 'exit' to cancel): ").strip()
            if user_id.lower() == "exit":
                return
            try:
                user_id = int(user_id)
                user_found = False
                for u in self.users:
                    if u.user_id == user_id:
                        user = u
                        self.users.remove(user)
                        print(f"User {user.username} with id {user_id} has been removed")
                        user_found = True
                        break
                if user_found:
                    break
                else:
                    print("User not found")
            except ValueError:
                print("Invalid user_id")

    # Method to create a transaction order object and store it in "BookstoreSystem.orders" list (self.orders)
    def create_order(self):
        print("\nCreating Order:")
        # Checking if there are saved books and users
        if not self.books:
            print("No books available.")
            return
        if not self.users:
            print("No users available.")
            return

        # Checking that user exists
        while True:
            try:
                user_id = input("Enter the user ID (or 'exit' to cancel): ").strip()
                if user_id.lower() == "exit":
                    return
                user_id = int(user_id)
            except ValueError:
                print("Invalid user ID.")
                continue
            user = next((u for u in self.users if u.user_id == user_id), None)
            if user:
                break
            else:
                print("User not found.")

        # Checking that isbn is correct and book exists
        while True:
            try:
                isbn = input("Enter book ISBN (or 'exit' to cancel): ").strip()
                if isbn.lower() == "exit":
                    return
                isbn = int(isbn.replace("-", ""))
            except ValueError:
                print("Invalid ISBN")
                continue
            book = next((b for b in self.books if b.isbn == isbn), None)
            if book:
                break
            else:
                print("Book not found.")

        while True:
            try:
                quantity = input("Enter the quantity (or 'exit' to cancel): ").strip()
                if quantity.lower() == "exit":
                    return
                quantity = int(quantity)
                if quantity <= 0:
                    print("Quantity must be positive.")
                    continue
            except ValueError:
                print("Invalid quantity.")
                continue

            # Checking if that amount of books is available
            if quantity > book.quantity:
                print("Not enough stock.")
            else:
                break

        new_order = Order(user, book, quantity)
        # Subtracting the ordered quantity from the book object stored in self.books to keep stock levels updated
        book.quantity -= quantity
        self.orders.append(new_order)
        print("Order placed successfully.")

    # Method to cancel a transaction order object, removing it from "BookstoreSystem.orders" list
    def remove_order(self):
        print("\nRemoving order:")
        if not self.orders:
            print("No orders to remove.")
            return
        # Showing orders so that it is easier to find the order
        for order in self.orders:
            print(f"Order ID {order.order_id}: {order}")

        while True:
            try:
                order_number = input("Enter order number to remove: (or 'exit' to cancel): ").strip()
                if order_number.lower() == "exit":
                    return
                order_number = int(order_number)
                # Searching order by id
                removed = next((o for o in self.orders if o.order_id == order_number), None)
                if removed:
                    self.orders.remove(removed)
                    # Updating the stock(quantity) of books in the correspondent list, self.books
                    for b in self.books:
                        if b.isbn == removed.book.isbn:
                            b.quantity += removed.quantity
                            break
                    print(f"Order ID {order_number} has been removed.")
                    break
                else:
                    print("Order ID not found.")
            except ValueError:
                print("Invalid input")

    # Method to search in any of the three "db" list of objects of the program:
    # Searching every object in these lists: BookstoreSystem.books, BookstoreSystem.users, BookstoreSystem.orders
    def search(self):
        print("\nSearch tool:")
        keyword = input("Enter keyword to search in books, users, or orders: ").strip().lower()
        found = False

        for book in self.books:
            if keyword in book.title.lower() or keyword in book.author.lower():
                print("Book:", book)
                found = True

        for user in self.users:
            if keyword in user.username.lower():
                print("User:", user)
                found = True

        for order in self.orders:
            if keyword in str(order).lower():
                print("Order:", order)
                found = True

        if not found:
            print("No results found.")


# Running the program
if __name__ == "__main__":
    main()
