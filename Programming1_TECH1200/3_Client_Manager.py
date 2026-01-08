"""
program that reads data from a file, processes it, and writes
the results to a new file. The program should implement control flow, loops, functions, and classes
to manipulate data stored in lists and dictionaries. You are also required to use modules to handle
file input and output.

code: list of dictionaries where each dictionary represents a customer and contains
their name, age, email, and phone number.
"""


# Creating a function for data validation as it will be used later in client creation and modification
def client_validation(current_name=None, current_age=None, current_email=None, current_phone=None):
    while True:
        n_name = input(f"Enter a name (current name: {current_name}): ").strip() if current_name else input("Enter name: ").strip()
        # When modifying, if we get no value we keep current value.
        if not n_name and current_name:
            n_name = current_name
        elif n_name.replace(" ", "").isalpha():
            n_name = n_name.title()
            break
        else:
            print("Invalid input. Please write letters and spaces only.")

    while True:
        n_age = input(f"Enter age (current age: {current_age}): ").strip() if current_age else input("Enter age: ").strip()
        # When modifying, if we get no value we keep current value.
        if not n_age and current_age:
            n_age = current_age
        elif n_age.isdigit() and int(n_age) > 0:
            n_age = int(n_age)
            break
        else:
            print("Invalid input. Please write a positive numeric value.")

    while True:
        n_email = input(f"Enter email (current email: {current_email}): ").strip() if current_email else input("Enter email: ").strip()
        # When modifying, if we get no value we keep current value.
        if not n_email and current_email:
            n_email = current_email
        elif "@" in n_email and "." in n_email.split("@")[-1]:
            break
        else:
            print("Invalid input. Please write a valid email address.")

    while True:
        n_phone = input(f"Enter phone (current phone: {current_phone}): ").strip() if current_phone else input("Enter phone: ").strip()
        # When modifying, if we get no value we keep current value.
        if not n_phone and current_phone:
            n_phone = current_phone
        # Cleaning phone number.
        else:
            n_phone = n_phone.replace(" ", "").replace("+", "").replace("-", "")
        # Data validation and formatting.
        #Check if is Australian number
        if n_phone.isdigit() and ((n_phone[:3] == "614" and len(n_phone) == 11) or (n_phone[:2] == "04" and len(n_phone) == 10)):
            #converting to our format "04XX-XXX-XXX"
            if n_phone[:2] == "61":
                n_phone = f"0{n_phone[2:]}"
            n_phone = f"{n_phone[:4]}-{n_phone[4:7]}-{n_phone[7:]}"
            break
        else:
            print("Invalid input. Please write a valid Australian mobile phone number.")
    return n_name, n_age, n_email, n_phone

# Creating a class for each client/customer, initializing 4 objects
# and creating methods to update these objects.
# upd_(update), n_(new)
class Client:
    def __init__(self, name, age, email, phone):
        self.name = name
        self.age = age
        self.email = email
        self.phone = phone

    def upd_name(self, n_name):
        self.name = n_name

    def upd_age(self,n_age):
        self.age = n_age

    def upd_email(self, n_email):
        self.email = n_email

    def upd_phone(self, n_phone):
        self.phone = n_phone

    # The below line of code is to give more information than the memory address provided by default when debugging
    def __repr__(self):
        return f"Client(name={self.name}, age={self.age}, email={self.email}, phone={self.phone})"

# Creating a class with an object for our group of clients,
# and creating methods that allow us to modify that group.
class ClientAdmin:
    def __init__(self):
        self.clients = []

    def add_client(self):
        print("Add a new client: ")
        name, age, email, phone = client_validation()
        new_client = Client(name, age, email, phone)
        self.clients.append(new_client)
        print(f"Client {name} has been added. Stepping into the next menu...")

    def find_client(self, name):
        for client in self.clients:
            if client.name == name:
                return client
        print("Client not found")


    # Using list comprehension to append customers always the name is different from the one provided
    def remove_client(self, name):
        client = self.find_client(name)
        if client:
            #modifies clients object including all clients but the one to be removed
            self.clients = [client for client in self.clients if client.name != name]
            print(f"Client {name} has been removed. Stepping into the next menu...")
        else:
            while True:
                try_again = input("To try again press \"1\", if not, press any other key. Then press \"Enter\": ")
                if try_again == "1":
                    deletion_name = input("\nPlease, enter the name of the customer you want to remove (then press \"Enter\"): ")
                    self.remove_client(deletion_name)
                else:
                    print("Stepping into the next menu...")
                    break

    def modify_client(self, name):
        client = self.find_client(name)
        if client:
            print(f"Modifying data for the client: {client.name}")
            #calling validation function
            new_name, new_age, new_email, new_phone = client_validation(
                current_name = client.name,
                current_age = client.age,
                current_email = client.email,
                current_phone = client.phone
            )
            # Updating client data
            client.upd_name(new_name)
            client.upd_age(new_age)
            client.upd_email(new_email)
            client.upd_phone(new_phone)

            print(f"Client{client.name} data has been updated. Stepping into the next menu...")
        else:
            while True:
                try_again = input("To try again press \"1\", if not, press any other key. Then press \"Enter\": ")
                if try_again == "1":
                    modification_name = input("\nPlease, enter the name of the customer to modify (then press \"Enter\"): ")
                    self.modify_client(modification_name)
                else:
                    print("Stepping into the next menu...")
                    break

    # Printing clients
    def display_clients(self):
        try:
            from tabulate import tabulate
            client_display = []
            for client in self.clients:
                client_display.append([client.name, client.age, client.email, client.phone])
            print(tabulate(client_display, headers=["Name", "Age", "Email", "Phone"], tablefmt="grid"))
        except ImportError:
            print("tabulate library not installed, printing in a simpler format: ")
            for client in self.clients:
                print(client.__dict__)



def main():
    import sys
    with open('A3_data_input.txt', 'w') as file:
        file.write("""customer_data = [
 {
 "name": "John Smith",
 "age": 35,
 "email": "johnsmith@gmail.com",
 "phone": "0413-535-124"
 },
 {
 "name": "Jane Doe",
 "age": 28,
 "email": "janedoe@yahoo.com",
 "phone": "0401-655-568"
 },
 {
 "name": "Bob Johnson",
 "age": 42,
 "email": "bjohnson@hotmail.com",
 "phone": "0433-515-912"
 }
]""")
    print("\nWelcome to Kaplan TECH1200, Assessment 3: Coding Assignment Analysis!\n")
    print("***The library \"tabulate\" is recommended for an enhanced user experience.")
    print("   You can install it entering \"pip install tabulate\" in the terminal of your code editor")
    print("   Then you can run the code again to see the difference!")
    while True:
        # Initializing class that administrate clients
        admin = ClientAdmin()

        # Loading the content of the txt with the information provided
        import json

        with open('A3_data_input.txt') as file:
            data_raw = file.read()
            # Cleaning the data to obtain just a list of dictionaries
            data_raw = data_raw.replace("customer_data =", "").strip()
            # loads read from a str, load read from a file. We pass it to json just because
            # it is a better format to work with once we finish the program and export the content.
            client_data = json.loads(data_raw)

        # Converting dictionaries to Client object and adding it to the admin
        for dictionaries in client_data:
            name = dictionaries["name"]
            age = dictionaries["age"]
            email = dictionaries["email"]
            phone = dictionaries["phone"]
            # Initializing class Client
            client = Client(name, age, email, phone)
            admin.clients.append(client)

        # Displaying current clients
        print("\nThese are the current clients:")
        admin.display_clients()

        print("\nAvailable options:")
        print("1. Add a new client")
        print("2. Remove a client")
        print("3. Modify a client")
        print("4. Continue to export screen")
        print("5. If you want to exit the program.")
        while True:
            choice = input("\nWrite your option number, then press \"Enter\": ")
            if choice in ["1","2","3","4","5"]:
                break
            print("Invalid character, please enter 1,2,3 or 4")

        if choice == "1":
            admin.add_client()
        elif choice == "2":
            deletion_name = input("\nPlease, enter the name of the client you want to remove (then press \"Enter\"): ")
            admin.remove_client(deletion_name)
        elif choice == "3":
            # Prompting the user for modifications
            modification_name = input("\nPlease, enter the name of the client to modify (then press \"Enter\"): ")
            admin.modify_client(modification_name)
        elif choice == "4":
            print("Loading export screen...")
        elif choice == "5":
            sys.exit("Program ended in modification stage")

        print("\nAvailable export options:")
        print("1. json")
        print("2. csv")
        print("3. txt")
        print("4. to display the modified list in the program")
        print("5. to exit the program")
        while True:
            choice = input("\nWrite your option number, then press \"Enter\": ")
            if choice in ["1","2","3","4","5"]:
                break
            print("Invalid character, please enter 1,2,3 or 4")

        # Convert Client object inside Admin back into dictionaries
        # Returns a list of dictionaries using in-build function __dict__
        client_data = []
        for client_object in admin.clients:
            client_data.append(client_object.__dict__)

        #paste content assigned to variable "data" in new created output file
        if choice == "1":
            with open('A3_data_output.json', "w") as nfile:
                json.dump(client_data, nfile)

        elif choice == "2":
            import csv
            with open('A3_data_output.csv', "w", newline='') as nfile:
                columns = ["name", "age", "email", "phone"]
                #Creating a DictWriter object
                writer = csv.DictWriter(nfile, fieldnames = columns)
                # Writing column names (header)
                writer.writeheader()
                # Writing data
                writer.writerows(client_data)

        elif choice == "3":
            with open('A3_data_output.txt', "w") as nfile:
                for client in client_data:
                    for key, value in client.items():
                        nfile.write(f"{key}: {value}\n")
                    nfile.write("\n")

        elif choice == "4":
            # Display updated customers
            print("\nThese are the updated clients:")
            admin.display_clients()

        elif choice == "5":
            sys.exit("Program ended in export stage")

        print("\nPress \"1\" to keep using the program")
        print("Press any other key to finalise the program")
        choice = input("Please, enter your choice followed by \"Enter\":")
        if choice != "1":
            sys.exit("End of the program.")





# The program runs main() function when executed, but not when imported
if __name__ == "__main__":
        main()