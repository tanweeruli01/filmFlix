from connect import *

# create a subroutine
def insert_films():
    #create an empty list
    tblFilms = []
    # ask for user input (filmID, title, yearReleased, rating. duration, genre)
    #MemberID is not required because it is auto increment field and does not require input
    title = input("Enter title of the film: ")
    yearReleased = int(input("Enter the year of release: "))
    rating = input("Enter rating of the film: ")
    duration = int(input("How long is the film(minutes): "))
    genre = input("What kind of genre is the film: ")

    # append data 
    tblFilms.append(title)
    tblFilms.append(yearReleased)
    tblFilms.append(rating)
    tblFilms.append(duration)
    tblFilms.append(genre)

    try:
        dbCursor.execute("INSERT into tblFilms VALUES(NULL, ?, ?, ?, ?, ?)", tblFilms) #Values from the list
        # #or
        # #values directly from variables 
        dbCon.commit() # make changes permanent
        print(f"{title} inserted into the Table")
    except sql.OperationalError as e:
        dbCon.rollback()
        print(f"Insert failed {e}")
if __name__ == "__main__":
    insert_films() 