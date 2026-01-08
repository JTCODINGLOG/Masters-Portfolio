# This list contains 90 of the most-watched movies between 2021 and 2023.
# Columns: id, title of the movie, country of production, viewership, awards, based on real stories(True) or books(False) and year.

table = [
    [1, "Oppenheimer", "USA", 60000000, 10, True, 2023],
    [2, "Barbie", "USA", 50000000, 8, False, 2023],
    [3, "Killers of the Flower Moon", "USA", 25000000, 7, True, 2023],
    [4, "The Killer", "USA", 20000000, 3, True, 2023],
    [5, "Priscilla", "USA", 15000000, 5, True, 2023],
    [6, "Past Lives", "USA", 12000000, 4, False, 2023],
    [7, "Saint Omer", "France", 10000000, 4, True, 2023],
    [8, "The Killer", "USA", 9000000, 3, True, 2023],
    [9, "Afire", "Germany", 8000000, 3, False, 2023],
    [10, "Pacifiction", "Spain/France", 7000000, 3, False, 2023],
    [11, "Spider-Man: Across the Spider-Verse", "USA", 45000000, 6, False, 2023],
    [12, "John Wick: Chapter 4", "USA", 40000000, 4, False, 2023],
    [13, "Guardians of the Galaxy Vol. 3", "USA", 55000000, 7, False, 2023],
    [14, "The Super Mario Bros. Movie", "USA/Japan", 50000000, 4, True, 2023],
    [15, "Indiana Jones and the Dial of Destiny", "USA", 32000000, 5, False, 2023],
    [16, "Mission: Impossible – Dead Reckoning Part One", "USA", 37000000, 5, False, 2023],
    [17, "The Marvels", "USA", 28000000, 3, False, 2023],
    [18, "Elemental", "USA", 27000000, 4, False, 2023],
    [19, "The Flash", "USA", 23000000, 2, False, 2023],
    [20, "Transformers: Rise of the Beasts", "USA", 34000000, 4, False, 2023],
    [21, "Dune: Part Two", "USA", 24000000, 6, True, 2023],
    [22, "The Hunger Games: The Ballad of Songbirds & Snakes", "USA", 22000000, 4, True, 2023],
    [23, "The Nun II", "USA", 17000000, 2, False, 2023],
    [24, "Five Nights at Freddy's", "USA", 16000000, 2, False, 2023],
    [25, "Aquaman and the Lost Kingdom", "USA", 31000000, 3, False, 2023],
    [26, "Wonka", "USA", 29000000, 3, True, 2023],
    [27, "Napoleon", "USA", 35000000, 6, True, 2023],
    [28, "The Exorcist: Believer", "USA", 18000000, 3, True, 2023],
    [29, "A Haunting in Venice", "USA", 19000000, 3, True, 2023],
    [30, "The Equalizer 3", "USA", 21000000, 4, False, 2023],
    [31, "Top Gun: Maverick", "USA", 75000000, 8, False, 2022],
    [32, "Avatar: The Way of Water", "USA", 65000000, 9, False, 2022],
    [33, "Black Panther: Wakanda Forever", "USA", 50000000, 7, False, 2022],
    [34, "Jurassic World Dominion", "USA", 60000000, 4, False, 2022],
    [35, "Doctor Strange in the Multiverse of Madness", "USA", 55000000, 5, False, 2022],
    [36, "Minions: The Rise of Gru", "USA", 49000000, 3, False, 2022],
    [37, "The Batman", "USA", 58000000, 6, False, 2022],
    [38, "Thor: Love and Thunder", "USA", 52000000, 4, False, 2022],
    [39, "Puss in Boots: The Last Wish", "USA", 42000000, 2, False, 2022],
    [40, "The Woman King", "USA", 30000000, 6, True, 2022],
    [41, "Elvis", "USA", 28000000, 7, True, 2022],
    [42, "Everything Everywhere All at Once", "USA", 25000000, 9, False, 2022],
    [43, "Nope", "USA", 31000000, 5, False, 2022],
    [44, "Lightyear", "USA", 26000000, 3, False, 2022],
    [45, "Sonic the Hedgehog 2", "USA", 35000000, 3, False, 2022],
    [46, "Bullet Train", "USA", 32000000, 4, False, 2022],
    [47, "The Menu", "USA", 23000000, 4, False, 2022],
    [48, "The Fabelmans", "USA", 20000000, 7, True, 2022],
    [49, "Glass Onion: A Knives Out Mystery", "USA", 22000000, 3, False, 2022],
    [50, "The Black Phone", "USA", 27000000, 4, False, 2022],
    [51, "Prey", "USA", 24000000, 2, False, 2022],
    [52, "Smile", "USA", 18000000, 2, False, 2022],
    [53, "Don't Worry Darling", "USA", 21000000, 3, False, 2022],
    [54, "The Northman", "USA", 16000000, 5, False, 2022],
    [55, "Babylon", "USA", 15000000, 3, False, 2022],
    [56, "Uncharted", "USA", 28000000, 4, False, 2022],
    [57, "Turning Red", "USA", 14000000, 2, False, 2022],
    [58, "Where the Crawdads Sing", "USA", 13000000, 2, True, 2022],
    [59, "Amsterdam", "USA", 17000000, 2, True, 2022],
    [60, "Black Adam", "USA", 30000000, 3, False, 2022],
    [61, "Spider-Man: No Way Home", "USA", 80000000, 10, False, 2021],
    [62, "No Time to Die", "USA/UK", 70000000, 5, False, 2021],
    [63, "Dune", "USA", 55000000, 9, True, 2021],
    [64, "Shang-Chi and the Legend of the Ten Rings", "USA", 45000000, 4, False, 2021],
    [65, "The Suicide Squad", "USA", 40000000, 3, False, 2021],
    [66, "Eternals", "USA", 42000000, 3, False, 2021],
    [67, "Venom: Let There Be Carnage", "USA", 50000000, 3, False, 2021],
    [68, "The Matrix Resurrections", "USA", 37000000, 2, False, 2021],
    [69, "Black Widow", "USA", 48000000, 4, False, 2021],
    [70, "Free Guy", "USA", 32000000, 3, False, 2021],
    [71, "Encanto", "USA", 29000000, 5, False, 2021],
    [72, "The French Dispatch", "USA", 16000000, 4, False, 2021],
    [73, "A Quiet Place Part II", "USA", 38000000, 3, False, 2021],
    [74, "The Green Knight", "USA", 20000000, 3, True, 2021],
    [75, "Cruella", "USA", 21000000, 4, True, 2021],
    [76, "The Last Duel", "USA", 17000000, 4, True, 2021],
    [77, "House of Gucci", "USA", 25000000, 3, True, 2021],
    [78, "The Harder They Fall", "USA", 18000000, 2, True, 2021],
    [79, "Don't Look Up", "USA", 24000000, 4, False, 2021],
    [80, "The Tomorrow War", "USA", 22000000, 3, False, 2021],
    [81, "Jungle Cruise", "USA", 20000000, 3, False, 2021],
    [82, "Luca", "USA", 19000000, 2, False, 2021],
    [83, "The Power of the Dog", "USA", 14000000, 5, False, 2021],
    [84, "Ghostbusters: Afterlife", "USA", 23000000, 3, False, 2021],
    [85, "West Side Story", "USA", 12000000, 6, True, 2021],
    [86, "King Richard", "USA", 10000000, 7, True, 2021],
    [87, "The King's Man", "USA", 18000000, 3, False, 2021],
    [88, "In the Heights", "USA", 16000000, 4, True, 2021],
    [89, "Coda", "USA", 9000000, 8, True, 2021],
    [90, "The Tragedy of Macbeth", "USA", 11000000, 3, True, 2021]
]
# function that prompts the user about filtering the table
def election():
    trigger = True
    while trigger == True:
        print("""
Available filters:
1-First letter of the title.
2-Country of production.
3-Views.
4-Number of awards.
5-Script origin.
6-Year.
7-Number of words in the title.
              """)
        filter_choice = input("Please, enter the number associated to your choice.\nRemember to press \"Enter\" key to confirm your choice\n")
        for i in range(1, 8):
            if str(i) == filter_choice:
                trigger = False
                return int(filter_choice)

# function to know different countries in the table(matrix) that has a specific configuration
def countries(matrix):
    countries = []
    countries.append(matrix[0][2])
    for row in matrix:
        if row[2] in countries:
            continue
        else:
            countries.append(row[2])
    return countries

# function to know maximum("max") or minimum("min") number in a specific column(int) of a table(matrix)
def extremes(matrix, maxmin, column):
    mm_number = matrix[0][column]
    for row in matrix:
        if maxmin == "max":
            if row[column] > mm_number:
                mm_number = row[column]
        elif maxmin == "min":
            if row[column] < mm_number:
                mm_number = row[column]
    return mm_number

# function that returns a modified table using a range in a specific column.
# This function was created to avoid repetition as 3 filters where under a similar code
def filter_range(table_og, selection, table_mod):
    while True:
        filter_choice_0 = input("Please enter first number of the range (must be equal or bigger than minimum number above & smaller or equal than maximum number) and press \"Enter\" key: ")
        if filter_choice_0.isdigit() and extremes(table_og, "max", selection) >= int(filter_choice_0) >= extremes(table_og, "min", selection):
            filter_choice_0 = int(filter_choice_0)
            break
    while True:
        filter_choice_1 = input("Please enter the last number of the range (must be equal or bigger than first range number & smaller than maximum number above) and press \"Enter\" key: ")
        if filter_choice_1.isdigit() and (filter_choice_0 <= int(filter_choice_1) <= extremes(table_og, "max", selection)):
            filter_choice_1 = int(filter_choice_1)
            break
    for row in table_og:
        if row[selection] in range(filter_choice_0, (filter_choice_1 + 1)):
            table_mod.append(row)
    return table_mod

# This is a function that filter the database based on the user choice.
# The function can work with a different databases always it follows the same format for each column.
# This function includes all the functions defined above to facilitate subprocesses.
# Every part of the conditional applies a different filter
def filter(movies):
    filtered_movies = []
    choice = election()
    if choice == 1:
        trigger = True
        while trigger == True:
            filter_choice_0 = input("Please enter a single letter and press \"Enter\" key: ")
            if filter_choice_0.isalpha() and len(filter_choice_0) == 1:
                for row in movies:
                    if row[choice][0] == filter_choice_0.upper():   
                        filtered_movies.append(row)
                trigger = False
    
    elif choice == 2:
        trigger = True
        while trigger == True:
            print("Available countries: \n", countries(movies), "\n")
            filter_choice_0 = input("Please input one of the above countries as displayed and press \"Enter\" key: ")
            if filter_choice_0 in countries(movies):
                for row in movies:
                    if row[choice] == filter_choice_0:
                        filtered_movies.append(row)
                trigger = False
    
    elif choice == 3:
        trigger = True
        while trigger == True:
            print("To filter views, we will search in a range:\n")
            print("The less popular film has", extremes(movies, "min", choice), "views.\nThe more popular film has", extremes(movies, "max", choice), "views.\n")
            filter_range(movies, choice, filtered_movies)
            trigger = False
    
    elif choice == 4:
        trigger = True
        while trigger == True:
            print("To filter for the awards, we will search for a range:\n")
            print("The less awarded film has", extremes(movies, "min", choice),"awards.\nThe more awarded film has", extremes(movies, "max", choice), "awards.\n")
            filter_range(movies, choice, filtered_movies)
            trigger = False

    elif choice == 5:
        trigger = True
        while trigger == True:
            while True:
                filter_choice_0 = input("To filter through the origin of the story, please enter letter \"B\" for book-based movie or \"S\" if the movie is based on a real story and press \"Enter\" key\n")
                if filter_choice_0 in ["S", "B"]:
                    if filter_choice_0.upper() == "S":
                        filter_choice_0 = True
                    elif filter_choice_0.upper() == "B":
                        filter_choice_0 = False
                    break
            for row in movies:
                if row[choice] == filter_choice_0:
                    filtered_movies.append(row)
            trigger = False
    
    elif choice == 6:
        trigger = True
        while trigger == True:
            print("To filter by year, we will search for a range:\n")
            print("The earliest year is", extremes(movies, "min", choice), ".\nThe oldest year is", extremes(movies, "max", choice), ".\n")
            filter_range(movies, choice, filtered_movies)
            trigger = False
    
    elif choice == 7:
        trigger = True
        while trigger == True:
            movies_s = []
            for movie in movies:
                movies_s.append(movie[:])
            for row in movies_s:
                row[1] = len(row[1].split())
            print("To filter by words, we will search for a range:\n")
            print("The movie title with less words has", extremes(movies_s, "min", 1), "words.\nThe movie title with more words has", extremes(movies_s, "max", 1), "words.\n")
            filter_range(movies_s, 1, filtered_movies)
            for row in filtered_movies:
                for line in movies:
                    if row[0] == line[0]:
                        row[1] = line[1]
                        break
            trigger = False

    header = ["Id", "Title", "Country of production", "Viewership", "Awards, Based on real stories(True) or books(False)", "Year"]
    filtered_movies.insert(0, header)
    
    return filtered_movies
        

# while loop to give the choice to the users to use the program for as long as they want
while True:
    print("This program will print a table after filtering a database with Hollywood movies between 2021 and 2023:")
    for row in filter(table):
        print(row)
    rep = input("\nPlease, input \"Yes\" to continue using the program or any other key to exit\nRemember to press \"Enter\" to confirm your choice\n")
    if rep.upper() != "YES":
        break


# EXTRA - It does not count for the assessment as the concept is not from the first 7 weeks of the course:
# If we wanted to give the user the choice of applying the function filter over itself so that he can filter
# over the previously filtered data we could replace in the filter function "return filtered_movies" for the code below:
# reiteration = input ("Please, input Yes (then press \"Enter\") to apply another filter over the current selection
# or any other key to pass to the next stage: ")
# if reiteration in ["YES", "Yes", "yes"]:
#     return filter(filtered_movies)
# else:
#     return filtered_movies
