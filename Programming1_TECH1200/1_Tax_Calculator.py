
# Using input to print a welcome message while asking the user to start/exit the program.
user_choice = input("""
"Welcome to your favourite Tax Calculator developed for the first assessment of KBI TECH1200  by Javier Tejeda!"

Instructions:
-Enter any key or combination of keys to initiate the program.
-Write 'exit' to stop using the program (it can be done at any time during the program).

***Please, note that the tax % applied is not real.
""")

# This while-loop allows the user to re-initiate or exit the program when it completes 'a loop'.
# In every stage the user is asked for input, the user can decide to exit the program.
# Since some code like sys.exit(), try, raise is not allowed I have to use conditional and loops several times.
while user_choice != "exit":
    # Asking for the following inputs: employee name, hours and hourly rate.
    # Data validation is deployed with loops and conditionals
    # The last conditional in every case allows the user to exit the program every time is prompted
    # In this code, char.isalpha() or char == " " will be True if the character is either a letter or a space.
    # If "it is not a char.isalpha() or char == " "" (same than if "it is a number or some other character") is True, the error message will be printed.
    # If all characters in the string are either letters or spaces, the "else:" associated with the for loop will be executed, breaking the outer while loop.
    while True:
        employee_name = input("Please, write employee's name: ")
        if employee_name == "exit":
            break
        for char in employee_name:
            if not (char.isalpha() or char == " "):
                print("Incorrect: User needs to input alphabetical values\n")
                break
        else:
            break
    if employee_name == "exit":
        break

    while True:
        weekly_hours = input("Please, provide the amount of hours the employee worked a week: ")
        if weekly_hours == "exit" or (weekly_hours.isdigit() and float(weekly_hours) > 0):
            break
        print("Incorrect: User needs to input a positive integer\n")
    if weekly_hours == "exit":
        break

    while True:
        hourly_rate = input("Please, provide the hourly rate of the employee: ")
        if hourly_rate == "exit" or (hourly_rate.isnumeric() and float(hourly_rate) > 0):
            break
        print("Incorrect: User needs to input a positive integer\n")
    if hourly_rate == "exit":
        break

    # Calculating gross and net income, tax and superannuation deductions.
    # Input function saves values in variables with string format. We use float for mathematical purposes.
    gross_income = float(weekly_hours) * float(hourly_rate)
    income_tax_deduction = gross_income * 0.2
    superannuation_deduction = gross_income * 0.1
    net_income = gross_income - income_tax_deduction - superannuation_deduction

    # Representing output in an organised way using nested lists.
    Output_table = [
        ["Employee Name: ", employee_name],
        ["Hours Worked per Week: ", weekly_hours],
        ["Hourly Rate: ", hourly_rate],
        ["Gross Income: ", gross_income],
        ["Income Tax Deduction: ", income_tax_deduction],
        ["Superannuation Deduction: ", superannuation_deduction],
        ["Net Income: ", net_income]
    ]
    # Finding the longest lenght of the elements in the "first column".
    length = 0
    for output in Output_table:
        if len(output[0]) > length:
            length = len(output[0])
    # Printing every row including the perfect gap between "first and second column" to make it look nice.
    print("\n")
    for output in Output_table:
        print(output[0] + (" " * (length - len(output[0])) + str(output[1])))

    # Including the first prompt inside the loop allows the user to repeat the program or exit it when the loop ends.
    user_choice = input("""
    Thanks for participating!
    Please, enter any key to re-initiate the program 
    or write 'exit' to stop using the program at any time
    """)


# The whole program is a loop, when all the data is corrected we need to ask the user if he wants to exit or start again
