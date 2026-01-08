# Asssessment 3: CRM System

# Library used to manage formats
import re

# Library used to round down age
import math

# Library used to calculate age
from datetime import datetime

# Library used for password encryption
import hashlib

# Library used to manage json files
import json

# Library used to develop the testing module
import unittest

# Library used to delete file after testing
import os

# USER DATA MANAGEMENT
# Defining password encryption
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

# Creating file to store program user data
USER_DATA_FILE = "pusers.json"


# Function to save program users
def save_pusers(pusers):
    # Creating dictionary with users stored in it
    data = {}
    for username in pusers:
        user = pusers[username]
        data[username] = {"username": user.username, "password": user.password}
    # Opening the file with w mode
    with open(USER_DATA_FILE, 'w') as file:
        json.dump(data, file, indent=3)

# Function to load program users
def load_pusers():
    try:
        # Opening the file in read mode
        with open(USER_DATA_FILE, 'r') as file:
            raw_data = json.load(file)
            pusers = {}
            for username in raw_data:
                user_info = raw_data[username]
                puser = Puser(user_info["username"], user_info["password"])
                pusers[username] = puser
            return pusers
    # Handeling file error
    except (FileNotFoundError, json.JSONDecodeError):
        return {}

# Function to load customers
def load_customers_from_json(manager, filename="customers.json"):
    try:
        with open(filename, 'r') as file:
            customer_data = json.load(file)
            for data in customer_data:
                customer = Customer(
                    customer_id=data["Customer ID"],
                    customer_name=data["Name"],
                    customer_email=data["Email"],
                    customer_phone=data["Phone"],
                    customer_address=data["Address"],
                    customer_birthday=data["Birthday"]
                )
                manager.customer_container.append(customer)
    except FileNotFoundError:
        # No file means if there are no customers yet
        pass




# DEFINING CLASSES

# Creating custom exception class for input validation
class InputValidationError(Exception):
    def __init__(self, message):
        # It is modified with new information everytime is called
        super().__init__(message)


# Puser (Program User) Class
class Puser:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    # Methods to edit Puser
    def edit_puser(self, n_username=None, n_password=None):
        if n_username:
            self.username = n_username
        if n_password:
            self.password = n_password


# Defining Customer Class
class Customer:
    def __init__(self, customer_id, customer_name, customer_email, customer_phone, customer_address, customer_birthday):
        self.customer_id = customer_id
        self.customer_name = customer_name
        self.customer_email = customer_email
        self.customer_phone = customer_phone
        self.customer_address = customer_address
        self.customer_birthday = customer_birthday

    # Method to store the object method in a dictionary
    def to_dict(self):
        return {
            "Customer ID": self.customer_id,
            "Name": self.customer_name,
            "Email": self.customer_email,
            "Phone": self.customer_phone,
            "Address": self.customer_address,
            "Birthday": self.customer_birthday,
            # Age is calculated in the next method
            "Age": self.age()
        }

    # Method to calculate age in Format DD-MM-YYYY
    def age(self):
        try:
            # Checking format
            birthday = datetime.strptime(self.customer_birthday, "%d-%m-%Y")
            # Obtaining today's date
            today = datetime.today()
            # Subtracting dates and extracting days from the object
            # Dividing by 365.25 for the leap years
            # Rounding down to know the age
            age = math.floor(float(today - birthday).days /365.25)
            return age
        except Exception:
            return "Invalid Birthday"


# Defining CustomerManager Class
class CustomerManager:
    def __init__(self):
        # The attribute is a list where we will store customer objects
        self.customer_container = []

    # The methods of CustomerManager serve to implement functionalities
    # Adding customers with append
    def add_customer(self, customer):
        # Checking if customer_ID exists
        if self.find_customers(customer.customer_id):
            # Using custom exception class defined before
            raise InputValidationError("This customer already exists.")
        # Checking if email already exists
        emails = {customer.customer_email for customer in self.customer_container}
        if customer.customer_email in emails:
            raise InputValidationError("A customer with identical email already exists.")
        self.customer_container.append(customer)

    # Removing customers with remove
    def remove_customer(self, customer_id):
        results = self.find_customers(customer_id)
        customer = results[0]
        if customer:
            self.customer_container.remove(customer)
        else:
            raise InputValidationError("This customer has not been found")

    # Dynamically finding customers
    def find_customers(self, search_by):
        results = []
        # Customer range age finder
        # Identifying date input through the format
        # Identifying input contains 2 dates
        if "-" in search_by and len(search_by.split("-")) == 2:
            try:
                min_age, max_age = map(int, search_by.split("-"))
                for customer in self.customer_container:
                    age = customer.age()
                    if isinstance(age, int) and min_age <= age <= max_age:
                        # Appending customers withing the specified range
                        results.append(customer)
                return results
            # If it is not a date try other search kinds
            except ValueError:
                return []
        # Other find cases
        for customer in self.customer_container:
            # Making the search a bit more flexible and uniform thanks to .lower() and in
            if (search_by.lower() in customer.customer_id.lower() or
                search_by.lower() in customer.customer_name.lower() or
                search_by.lower() in customer.customer_email.lower() or
                search_by.lower() in customer.customer_phone.lower() or
                search_by.lower() in customer.customer_address.lower() or
                search_by.lower() in customer.customer_birthday.lower() or
                # find specific age
                str(customer.age()) == search_by):
                results.append(customer)
        return results

    # Editing customers attributes
    def edit_customer(self, customer_id, customer_name = None, customer_email = None, customer_phone = None, customer_address = None, customer_birthday = None):
        results = self.find_customers(customer_id)
        # Find customer returns a list, not a single object
        customer = results[0]
        if not customer:
            raise InputValidationError("This customer has not been found")
        if customer_name:
            customer.customer_name = customer_name
        if customer_email:
            customer.customer_email = customer_email
        if customer_phone:
            customer.customer_phone = customer_phone
        if customer_address:
            customer.customer_address = customer_address
        if customer_birthday:
            customer.customer_birthday = customer_birthday

    def display_customers(self):
        return self.customer_container

    # Exporting with Json: used for exporting and internal customer saving
    def json_export(self, customers=None, filename="customers_export.json"):
        if customers is None:
            customers = self.customer_container
        with open(filename, 'w') as file:
            # Using dump to convert the customer_container (list of dicts) into JSON
            # List comprehension explanation: for each customer(c) in the customer container...
            # ...todict is called and the resulting dictionary is added to the list
            json.dump([customer.to_dict() for customer in customers], file, indent=3)


# DEFINING VALIDATION HELPERS: Because inputs are validated often.

# General input behaviour helper: it prompts again if user is wrong and allow user to exit whenever wants
def safe_input(prompt, validator=None, field_name="Input", allow_exit=True, allow_blank=False):
    while True:
        value = input(prompt)
        # Return None when user wants to exit
        if allow_exit and value.strip().lower() == "exit":
            print("Exiting input.")
            return None
        # Accepting empty string to 'skip' (thought for edit customer)
        if allow_blank and value == "":
            return ""
        try:
            # Return value when is valid
            check_empty(value, field_name)
            if validator:
                validator(value)
            return value
        except InputValidationError as e:
            print(f"{e}")
        except Exception as e:
            print(f"Unexpected error: {e}")


# Password validation
def check_password(password):
    if ((len(password) < 8) or
        (not re.search("[A-Z]", password)) or
        (not re.search("[a-z]", password)) or
        (not re.search("[0-9]", password)) or
        (not re.search("[@#\\$%\\^&\\*!\\?\\+\\=]", password))):
        raise InputValidationError("Invalid password. It must contain, uppercase, lowercase, number and special character.")

# Email validation
def check_email(email):
    if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
        raise InputValidationError("Invalid email format.")

# Phone validation
def check_phone(phone):
    if not phone.isdigit():
        raise InputValidationError("Phone must be numeric.")

# Not-empty validation
def check_empty(value, field):
    if not value:
        raise InputValidationError(f"{field} cannot be empty.")

# Birthday validation
def check_birthday(birthday):
    try:
        datetime.strptime(birthday, "%d-%m-%Y")
    except ValueError:
        raise InputValidationError("Birthday has to follow DD-MM-YYYY format.")

# Address validation

# Developing command line interfaces for menus and submenus

# INITIAL INTERFACE: ACCESS TO THE SYSTEM
def cli_log(pusers=None):
    # Loading users from the file
    if pusers is None:
        pusers = load_pusers()
    while True:
        print("\n___Welcome to TECH6100 CRM System___")
        print("1: Sign up")
        print("2: Log in")
        print("3: Exit")
        choice = input("Please, Choose an option: ")

        # Signing program user in
        if choice == '1':
            try:
                # Applying the safe_input helper
                username = safe_input("Please, enter username (or 'exit' to leave): ", field_name="Username")
                if username is None:
                    continue
                password = safe_input("Please, enter password (or 'exit' to leave): ", validator=check_password, field_name="Password")
                if password is None:
                    continue
                if username in pusers:
                    print("This user already exists.")
                else:
                    # Encrypting password
                    hashed_password = hash_password(password)
                    # Creating and storing new user
                    pusers[username] = Puser(username, hashed_password)
                    # Saving user
                    save_pusers(pusers)
                    print("User account created.")
                    # Logs in once the user creates the account
                    cli_intro(pusers[username], pusers)
            except InputValidationError as e:
                print("Error:", e)
        # Loging in the program
        elif choice == '2':
            username = safe_input("Please, enter username (or 'exit' to leave): ", field_name="Username")
            if username is None:
                continue
            password = safe_input("Please,enter password (or 'exit' to leave): ", validator=check_password, field_name="Password")
            if password is None:
                continue
            hashed_password = hash_password(password)
            if username in pusers and pusers[username].password == hashed_password:
                print("Login has been successful!")
                cli_intro(pusers[username], pusers)
            else:
                print("Invalid credentials.")
        # Exiting the program
        elif choice == '3':
            print("Thank you! See you soon!")
            break
        else:
            print("Invalid option.")

# ROOT INTERFACE: DIVIDES FUNCTIONALITIES, PROGRAM USER, CUSTOMERS
def cli_intro(current_user, pusers):
    manager = CustomerManager()
    while True:
        print(f"\n___CRM Initial Menu___")
        print("1. Customer Menu")
        print("2. My Profile")
        print("3. Log Out")
        print("4. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            cli_customer_menu(manager)
        elif choice == '2':
            result = cli_profile(current_user, pusers)
            if result == 'delete':
                break
        elif choice == '3':
            break
        elif choice == '4':
            print("Exiting program.")
            exit()
        else:
            print("Invalid option.")


# PROFILE INTERFACE: MANAGE PROGRAM USER ACCOUNT
def cli_profile(puser, pusers):
    while True:
        print(f"\n___{puser.username} Profile___")
        print("1: View Profile")
        print("2: Edit Password")
        print("3: Delete Profile")
        print("4: Exit")
        choice = input("Please, choose an option: ")

        try:
            if choice == '1':
                print(f"Username: {puser.username}")
                # Masking password for security reasons
                print(f"Password: {'*' * len(puser.password)}")

            elif choice == '2':
                new_password = safe_input("Enter new password (or 'exit' to cancel): ", validator=check_password, field_name="Password")
                if new_password is None:
                    return
                hashed = hash_password(new_password)
                puser.edit_puser(n_password=hashed)
                save_pusers(pusers)
                print("Password has been updated.")

            elif choice == '3':
                confirm = input("Are you sure you want to delete your profile? (yes/no): ").lower()
                if confirm == 'yes':
                    del pusers[puser.username]
                    save_pusers(pusers)
                    print("Your profile has been deleted.")
                    # This will indicate cli_intro to return to cli_log
                    return 'delete'
                else:
                    print("Deletion cancelled.")

            elif choice == '4':
                break

            else:
                print("Invalid option.")

        except InputValidationError as e:
            print("Validation Error:", e)
        except Exception as e:
            print("Unexpected error:", e)

# CRM INTERFACE: MANAGES CUSTOMERS
def cli_customer_menu(manager):
    # Loading existing customers from json file (if exists in the same path than python file)
    load_customers_from_json(manager)

    while True:
        print("\n___CRM Menu___")
        print("1: Add Customer")
        print("2: Edit Customer")
        print("3: Find Customer")
        print("4: Remove Customer")
        print("5: Display All Customers")
        print("6: Export to JSON")
        print("7: Back")
        print("8: Exit")
        choice = input("Please, choose an option: ")

        try:
            # Adding customer
            if choice == '1':
                cid = safe_input("Enter Customer ID (or 'exit'): ", field_name="Customer ID")
                if cid is None: return

                name = safe_input("Enter Name (or 'exit'): ", field_name="Name")
                if name is None: return

                email = safe_input("Enter Email (or 'exit'): ", validator=check_email, field_name="Email")
                if email is None: return

                phone = safe_input("Enter Phone (or 'exit'): ", validator=check_phone, field_name="Phone")
                if phone is None: return

                address = safe_input("Enter Address (or 'exit'): ", field_name="Address")
                if address is None: return

                birthday = safe_input("Enter Birthday (DD-MM-YYYY, or 'exit'): ", validator=check_birthday,
                                      field_name="Birthday")
                if birthday is None: return

                manager.add_customer(Customer(cid, name, email, phone, address, birthday))
                print("Customer added.")
                # Updating json file
                manager.json_export(filename="customers.json")
            # Editing customer
            elif choice == '2':
                cid = safe_input("Please, enter Customer ID to edit (or 'exit'): ", field_name="Customer ID")
                if cid is None:
                    return

                customer = manager.find_customers(cid)
                if customer:
                    customer = customer[0]  # Extract the single customer object from list

                    print(f"Editing customer: {customer.customer_name}")

                    name = safe_input(
                        f"Please, enter new name (press Enter to keep '{customer.customer_name}', or 'exit'): ",
                        field_name="Name", allow_blank=True
                    )
                    if name is None: return
                    if name == "": name = customer.customer_name

                    email = safe_input(
                        f"Please, enter new email (press Enter to keep '{customer.customer_email}', or 'exit'): ",
                        validator=check_email, field_name="Email", allow_blank=True
                    )
                    if email is None: return
                    if email == "": email = customer.customer_email

                    phone = safe_input(
                        f"Please, enter new phone (press Enter to keep '{customer.customer_phone}', or 'exit'): ",
                        validator=check_phone, field_name="Phone", allow_blank=True
                    )
                    if phone is None: return
                    if phone == "": phone = customer.customer_phone

                    address = safe_input(
                        f"Please, enter new address (press Enter to keep '{customer.customer_address}', or 'exit'): ",
                        field_name="Address", allow_blank=True
                    )
                    if address is None: return
                    if address == "": address = customer.customer_address

                    birthday = safe_input(
                        f"Please, enter new birthday (press Enter to keep '{customer.customer_birthday}', or 'exit'): ",
                        validator=check_birthday, field_name="Birthday", allow_blank=True
                    )
                    if birthday is None: return
                    if birthday == "": birthday = customer.customer_birthday

                    manager.edit_customer(cid, name, email, phone, address, birthday)
                    print("Customer updated.")
                    # Updating json file
                    manager.json_export(filename="customers.json")
                else:
                    print("Customer not found.")
            # Finding customer
            elif choice == '3':
                search_by = input("Please, enter value to search by (ID, name, email, phone, address, birthdate, age or age range(I.e., 20-30): ").strip()
                matches = manager.find_customers(search_by)

                if matches:
                    for customer in matches:
                        # Exporting from json file
                        print(json.dumps(customer.to_dict(), indent=3))

                    # Creating the export choice for the customer
                    export_choice = input(
                        "Do you want to export these results to a JSON file? (yes/no): ").strip().lower()
                    if export_choice == 'yes':
                        filename = input("Please, enter filename (I.e., 'filename.json') or press Enter for default: ").strip()
                        if not filename:
                            # Creating unique default filename using current date and time
                            timestamp = datetime.now().strftime("%d%m%Y_%H%M%S")
                            filename = f"Customers_{timestamp}.json"
                        else:
                            # If user is missing .json
                            if not filename.endswith(".json"):
                                filename += ".json"
                        # Reusing the exporting function for this case
                        manager.json_export(matches, filename)
                        print(f"Results exported to {filename}")
                else:
                    print("Customer has not been found.")
            # Removing customer
            elif choice == '4':
                cid = input("Please,enter Customer ID to remove: ")
                manager.remove_customer(cid)
                print("Customer removed.")
                manager.json_export(filename="customers.json")
            # Displaying customer
            elif choice == '5':
                customers = manager.display_customers()
                if not customers:
                    print("No customers to display.")
                else:
                    for customer in customers:
                        print(json.dumps(customer.to_dict(), indent=3))
            # Exporting customer
            elif choice == '6':
                manager.json_export(filename="customers_export.json")
                print("Exported to customers_export.json")
            # Back to previous menu
            elif choice == '7':
                break
            # Exit
            elif choice == '8':
                print("Exiting program.")
                return
            else:
                print("Invalid option.")

        except InputValidationError as e:
            print("Validation Error:", e)
        except Exception as e:
            print("Unexpected error:", e)
        finally:
            print("Returning to menu.")


# TESTING UNIT:
# At first, random tests were considered...
# ...but the own nature of random inputs limits the effectiveness of the testing unit...
# ...this is because we might not know why it fails as inputs have been randomly created.
def run_tests():
    class CRM_Test(unittest.TestCase):
        def setUp(self):
            self.manager = CustomerManager()
            self.customer = Customer(
                customer_id="001",
                customer_name="Javier T",
                customer_email="javier@kaplan.com",
                customer_phone="0401846855",
                customer_address="10 William Street Perth",
                customer_birthday="01-01-2000"
            )
            self.manager.add_customer(self.customer)

        def test_add_customer(self):
            self.assertIn(self.customer, self.manager.customer_container)

        def test_duplicate_customer_id(self):
            with self.assertRaises(InputValidationError):
                duplicate = Customer(
                    # Same ID
                    customer_id="001",
                    customer_name="Stanley",
                    customer_email="Stanley@kaplan.com",
                    customer_phone="0444333222",
                    customer_address="15 Something Street East Perth",
                    customer_birthday="24-05-1993"
                )
                self.manager.add_customer(duplicate)

        def test_duplicate_email(self):
            with self.assertRaises(InputValidationError):
                duplicate = Customer(
                    customer_id="002",
                    customer_name="Stanley",
                    # Same email
                    customer_email="javier@kaplan.com",
                    customer_phone="0444333222",
                    customer_address="15 Something Street East Perth",
                    customer_birthday="24-05-1993"
                )
                self.manager.add_customer(duplicate)

        def test_find_customer_by_name(self):
            results = self.manager.find_customers("Javier")
            self.assertGreaterEqual(len(results), 1)

        def test_edit_customer(self):
            self.manager.edit_customer("001", customer_name="Javi T", customer_phone="0999999999")
            customer = self.manager.find_customers("001")[0]
            self.assertEqual(customer.customer_name, "Javi T")
            self.assertEqual(customer.customer_phone, "0999999999")

        def test_remove_customer(self):
            self.manager.remove_customer("001")
            self.assertNotIn(self.customer, self.manager.customer_container)

        def test_invalid_email_format(self):
            with self.assertRaises(InputValidationError):
                check_email("invalid_email")

        def test_invalid_password(self):
            with self.assertRaises(InputValidationError):
                check_password("password")

        def test_valid_password(self):
            try:
                check_password("P@ssw0rd!")
            except InputValidationError:
                self.fail("check_password raised an unexpected exception")

        def test_invalid_birthday_format(self):
            with self.assertRaises(InputValidationError):
                check_birthday("1991-01-01")

        def test_valid_birthday_format(self):
            try:
                check_birthday("01-01-1991")
            except InputValidationError:
                self.fail("check_birthday raised an unexpected exception")

        # Checking export file works well
        def test_json_exp(self):
            # Checking if more than one entry can be managed
            self.manager.add_customer(Customer(
                customer_id="002",
                customer_name="Stanley",
                customer_email="Stanley@kaplan.com",
                customer_phone="0444333222",
                customer_address="15 Something Street East Perth",
                customer_birthday="24-05-1993"
            ))
            # Export to a test file
            test_filename = "test_exp.json"
            # Exporting file
            self.manager.json_export(filename=test_filename)

            # Loading exported file
            with open(test_filename, 'r') as file:
                exported_data = json.load(file)

            # Manually prepare the expected dictionary
            expected_data = [customer.to_dict() for customer in self.manager.customer_container]

            # Comparing dictionaries
            self.assertEqual(exported_data, expected_data)

            # Deleting test file to clean memory
            if os.path.exists(test_filename):
                os.remove(test_filename)

    # Loading tests
    suite = unittest.defaultTestLoader.loadTestsFromTestCase(CRM_Test)
    # Improving verbosity: displaying name of the test and if it passed or failed
    unittest.TextTestRunner(verbosity=2).run(suite)

# RUNNING THE PROGRAM!!!
if __name__ == "__main__":
    # WANT TO PERFORM TEST UNIT?: Change "TESTING" value to "True"
    TESTING = False

    if TESTING:
        run_tests()
    else:
        cli_log()