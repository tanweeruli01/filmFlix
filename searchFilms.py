from connect import *
import logging
import time

logging.basicConfig(filename=r"file.log", level=logging.DEBUG)

# create subroutine
def search():
    try:
        field = input("Would you like to search by filmID, title, yearReleased, rating, duration or genre? ")
        if field == "filmID":
            idInput = input("Enter filmID: ")
        
            dbCursor.execute(f"SELECT * FROM tblFilms WHERE filmID = {idInput}")
            row = dbCursor.fetchone()
            if row == None:
                print(f"No films with the ID {idInput} in this table.")
                logging.warning(f"On {time.asctime()}, in {__name__} file, user entered {idInput} as {field}")
            else: 
                for aRecord in row:
                    print(aRecord)
        elif field == "title" or field == "yearReleased" or field == "rating" or field == "duration" or field == "genre":
            searchInput = input(f"Enter search field for {field}: ")

            dbCursor.execute(f"SELECT * FROM tblFilms WHERE {field} LIKE '%{searchInput}%'")
            rows = dbCursor.fetchall()
            if not rows:
                print(f"No records with the field {field} matching '{searchInput}' in the table. ")
                logging.warning(f"On {time.asctime()}, in {__name__} file, user entered {searchInput} as {field}")
            else:
                for records in rows:
                    print(records)
        else:
            print(f"Invalid search field {field}")
    except sql.OperationalError as e:
        print(f"No database or table found: {e}")

if __name__ == "__main__":
    search()

