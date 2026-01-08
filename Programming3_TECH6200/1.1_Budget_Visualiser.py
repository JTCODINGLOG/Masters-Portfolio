"""
APPLICATION THAT HELPS YOU TO UNDERSTAND YOUR FINANCIAL SITUATION

I took this idea from the Commonwealth Bank mobile application
The idea is to use several built-in functions to make the code more efficient
Advanced functions used: any, zip, filter, lambda, sorted.
In some scenarios, an alternative using reduce is provided...
...and it would require importing that function as represented below:
from functools import reduce
"""


# For reusability, we define a function to exit the program
# If the input is exit, then it executes 'exit()' function to end the program
def end(inp):
    if inp.lower() == "exit":
        print("Ending the program. Have a nice day!")
        exit()


# To allow program repetition we use a while loop
while True:
    print("Welcome to your favourite budget visualiser: ")
    print("-Type 'exit' to stop the program")
    print("-Leave any or both fields blank to generate the bank statement")

    # Initialising input containers (lists)
    tr_name = []
    tr_amount = []

    # In this step the program asks for transactions name and amount
    # It will keep prompting until the user decides to stop
    while True:
        transaction_name = input("\nPlease, input the name of a transaction: ").strip()
        end(transaction_name)
        transaction_amount = input("Please, input a positive/negative AUD amount for the above transaction: ").strip()
        end(transaction_amount)

        # The generator returns True if the first field is empty, then iterates and checks...
        # ...on the other field.
        # 'Any' will return True if at least one of the fields is an empty string
        # If True, the while loop is broken and the codes jump to line 61
        # The expected output is that Input request will stop if any input field is empty
        if any(field == "" for field in [transaction_name, transaction_amount]):
            print("Loading statement...\n")
            break

        try:
            # In this step the input is normalized and formatted with float
            transaction_fl_amount = float(transaction_amount)
            # Although an option was to do it later using map and lambda,...
            # ...tr_amount = list(map(lambda x: float(x), tr_amount))...
            # ...doing formatting before allows the program to validate data earlier.

            # In this step the data is loaded into the containers using '.append()'
            # '.append()' modifies the original list 'tr_name' adding 'transaction_name'...
            # ...to the end of the list
            tr_name.append(transaction_name)
            tr_amount.append(transaction_fl_amount)
        except ValueError:
            print("Not valid amount. You must enter a numeric value.")
            continue

    # Checking if amount of inputs are enough
    if not tr_name or not tr_amount:
        print("We have not received enough inputs to generate a statement")
    else:
        # Joining name and amount to create a list of transactions
        # In this step a list of tuples is created with zip
        # 'zip()' allows to combine multiple lists or other iterables into one iterable of tuples
        # 'zip()' iterates over the iterables and stops when the shortest input iterable is exhausted
        # 'zip()' returns an iterable (object in the memory). To get a list, 'list()' is needed.
        tr = list(zip(tr_name, tr_amount))

        # Generating information about the most noticeable incomes and expenses.
        # Filtering positive amounts of the transaction list 'tr'
        # In this step filter is used over 'tr' list, and the function that applies the test...
        # ...is a 'lambda' function that executes a condition. In this case lambda function returns True ...
        # ...if the second element in each tuple (tr_amount) is bigger than 0...
        # ...therefore we filter pulling out elements that do not pass the test, the ones that return False.
        # Filter creates an object which also is an iterator, that is why we convert it into a list.
        # The expected value of 'incomes' is a list of tuples whose second element is positive.
        incomes = list(filter(lambda x: x[1] > 0, tr))
        # Filtering of negative amounts
        # Here it is the same procedure with different logic, we just keep amounts lower than 0.
        # The expected value of 'incomes' is a list of tuples whose second element is negative.
        expenses = list(filter(lambda x: x[1] < 0, tr))

        # In this step, 'incomes' and 'expenses' variables are sorted.
        # 'sorted()' function returns a sorted list of the specified iterable object.
        # The key is a function that decides the order and that returns None as default.
        # In these cases we want to order by amount, and the lambda function allows...
        # ...to use the second element of each tuple as key, the one corresponding with the amount.
        # -To order in descending order for incomes using 'reverse=True'. Largest to smallest.
        # -To order in ascending order for expenses. Default 'reverse' is False, that means Smallest to Largest.
        # Then we select the last 3 tuples slicing the list '[:3]'
        # The expected outputs are the top 3 incomes and expenses out of all transactions.
        top_3_incomes = sorted(incomes, key=lambda x: x[1], reverse=True)[:3]
        top_3_expenses = sorted(expenses, key=lambda x: x[1])[:3]

        # Calculate total incomes and expenses
        total_incomes = sum(x[1] for x in incomes)
        total_expenses = sum(x[1] for x in expenses)
        # Reduce has not been used because of efficiency matters:
        # -Sum is a build in function. A summing loop that runs at C-level speed.
        # -Reduce calls lambda in each interation, which is Python-level code and...
        # ...that means that there are more processes behind, compared to 'simple arithmetic'
        # I.e., total_income = reduce(lambda a, x: a + x[1], incomes)

        # Calculate balance
        # Now the idea is to give a quick heads up to the user to see if...
        # ...the account is in positive or negative numbers calculating the total amount.
        # Remember expenses are negative, that is why they are added.
        balance = total_incomes + total_expenses
        # This could have been done using reduce or sum, but it is less efficient:
        # With our option it is just needed to add/sum 2 numbers.
        # Reduce: total = reduce(lambda a, x: a + x[1], tr)
        # This function uses lambda function and iteration so the running time is higher than a simple sum.
        # Sum: sum(tr_amount)
        # This is just a sum of more than 2 numbers, which is the minimum for a sum.

        # Printing results:
        # Printing a congrats message or a 'watch out' message depending on the balance
        if balance > 1000:
            print("Congratulations! you are saving a decent amount of money")
        elif balance < -500:
            print("Watch out your finances! You might have to pay high interest rate")
        print(f"The account balance is: AUD {balance}")

        # Printing previously calculated top incomes and expenses
        print("\nTop 3 incomes:")
        for name, amount in top_3_incomes:
            print(f"{name.title()}: AUD {amount}")
        print("\nTop 3 expenses:")
        for name, amount in top_3_expenses:
            print(f"{name.title()}: AUD {amount}")
    # Giving the user the choice of repeating the process or exiting the program
    again = input("Please, press any key to analyse more transactions or 'exit' to leave: ").strip()
    end(again)
    print("\n")
