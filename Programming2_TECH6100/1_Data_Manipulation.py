# Welcome message
print("\nWelcome to Techgenius data manipulation and analysis library:")

# choice is the "menu function":
# it asks for input to the user
# the user can choose program functionalities or exit
# each functionality redirects back to this function when it finishes
def choice():
    choice = None
    while choice not in ("1", "2", "3", "4"):
        choice = input("""
Please, enter numbers 1,2,3 or 4 to execute one of the below options:
1 - Calculate Statistics
2 - Merge Dictionaries
3 - Format string
4 - EXIT\n""")

    if choice == "1":
        return Task1()
    if choice == "2":
        return Task2()
    if choice == "3":
        return Task3()
    if choice == "4":
        return exit("You have exited the program. Thank you for using Techgenius library.")

# Function that returns mean, standard deviation and median
def get_stats(*args):
    # handling output and print
    # calculate mean
    mean = sum(args) / len(args)
    # calculate median
    # first we need to sort the args to find the middle value
    ordered_args = sorted(args)
    try:
        # // rounds the result to the nearest integer
        median = ordered_args[(len(args)-1)//2]
    except TypeError:
        n1 = ordered_args[len(args)//2]
        n2 = ordered_args[(len(args)-2)//2]
        median = (n1 + n2)/2
    # calculate standard deviation
    stdev = 0
    for number in args:
        stdev += (number - mean)**2
    stdev = round((stdev / len(args))**0.5, 2)
    # return results
    return mean, median, stdev

# Function that holds the input and structure and of choice 1.
def Task1():
    # handling input
    while True:
        try:
            nlist = input("\nPlease, enter a list of numbers separated by commas or spaces to calculate mean, median, and standard deviation:\n")
            nlist = nlist.replace(",", " ")
            nlist = nlist.split()
            for i in range(len(nlist)):
                nlist[i] = float(nlist[i])
            break
        except ValueError:
            print("Error: input must be numerical values, commas and spaces\n")
    # get the statistics using previously defined function
    # because I have a list of numbers I need to unpack it
    mean, median, stdev = get_stats(*nlist)
    print(f"List: {nlist}\nMean: {mean}\nMedian: {median}\nStandard deviation: {stdev}")

    return choice()

# Function that iterates over the dictionaries provided and merge them
def merge_dict(**kwargs):
    print("Merging the following dictionaries:")
    for dictionary in kwargs.values():
        print(dictionary)
    merged_dictionary = {}
    for dictionary in kwargs.values():
        merged_dictionary.update(dictionary)
    return merged_dictionary

# Function that holds the input and structure and of choice 2
def Task2():
    # prompt for amount of dictionaries
    while True:
        try:
            ndict = int(input("How many dictionaries do you wish to merge? "))
            if ndict > 1:
                break
            else:
                print("Please, enter a number equal or bigger than 2. You cannot merge just 1 dictionary.")
        except ValueError:
            print("Please enter a non-decimal numerical value")
    dictionaries = {}
    # prompt for key and values
    for i in range(ndict):
        print(f"Let's collect data for dictionary {i+1}:")
        dic ={}
        while True:
                # key input
                while True:
                    dictkey = input("Enter key: ")
                    # check key
                    repeated = False
                    for dictionary in dictionaries.values():
                        if dictkey in dictionary:
                            repeated = True
                            print("\nThis key has already been used in previous dictionaries, please enter a non-repeated key\n")
                    for key in dic:
                        if key == dictkey:
                            repeated = True
                            print("\nThis key has already been used in this dictionary, please enter a non-repeated key\n")
                    if repeated == False:
                        break
                # value input
                dictvalue = input ("Enter value: ")
                dict[dictkey] = dictvalue
                # Check if user wants to keep adding values
                cont_dict = input(f"Do you want to keep adding key-values for Dictionary {i+1}?(Y/N)\n")
                if cont_dict.upper() in ["NO", "N", "NOPE"]:
                    dictionaries[f"dict{i + 1}"] = dic
                    break
    merged_dictionary = merge_dict(**dictionaries)
    print(f"The merged dictionary is: {merged_dictionary}")

    return choice()

# Function that formats the strings provided
def create_string(template, *args):
    return template.format(*args)

# Function that holds the input and structure and of choice 3
def Task3():
    # handling input
    while True:
        user_template = input("Please, enter you string with placeholders '{}': ")
        if "{}" in user_template:
            break
        print("No '{}' entered")
    while True:
        placeholders = input("Please, enter placeholders. Make sure you separate them by commas: ")
        cb_count = user_template.count("{}")
        placeholders = placeholders.split(",")
        p_count = len(placeholders)
        if p_count == cb_count:
            break
        print(f"The number of placeholders: {p_count} is different than the number of curly brackets: {cb_count}")
    # handling output and print
    formatted_string = create_string(user_template, *placeholders)
    print(f"This is the formatted string: {formatted_string}")
    # return choice
    return choice()
# Calling the choice function
choice()


