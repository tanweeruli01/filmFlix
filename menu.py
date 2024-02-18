import readFilms, addFilm, deleteFilms, searchFilms, updateFilms


def read_file():
    try:
        with open ("menuOptions.txt") as fileRead:
            fr = fileRead.read()
        return fr
    except FileNotFoundError as nf:
        print(f"Check {nf}")

#create the function menu
def films_menu():
    options = 0 #initialise the option variable with an integer value
    optionsList = ["1", "2", "3", "4", "5", "6",]

    #assign the read_file() function to the menuChoices variable
    menuChoices = read_file()

    #create while loop to repeat the code within the body of the while condition
    while options not in optionsList:
        print(menuChoices) #call/invoke read_file() function to the menuChoices variable

        # re-assign the value of the option varibale with the input function
        options = input("Enter an option from the menu choice above: ")

        # check if the input from the option variable matches any of the options in the optionList
        if options not in optionsList:
            # if the condition is true execute the code below
            print(f"{options} is not a valid choice! ")
    return options
print(films_menu())

mainProgram = True #boolean variable to toggle true or false

while mainProgram: #while true
    #assign the members_menu() function to the mainMenu variable 
    mainMenu = films_menu()
    #use matchcase
    match mainMenu: 
        case "1": #if case value  equals/matches the string value 1 then
            readFilms.read_films() #call readMembers function from the readMembers.py file
        case "2":
            addFilm.insert_films()
        case "3":
            updateFilms.update_films()
        case "4":
            deleteFilms.delete_film()
        case "5":
            searchFilms.search()
        case _:
            #reassign the value of mainProgram to False
            mainProgram = False
input("Press enter to exit the program: ")


    