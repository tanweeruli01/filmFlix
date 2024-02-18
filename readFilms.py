from connect import *

#create subroutine
def read_films():
    try:
        dbCursor.execute("SELECT * FROM tblFilms")

        # fetchall(): fetches all the selected records
        rows = dbCursor.fetchall() #row holds all fetched records

        #loop through all the records in the row variable 
        for aRecord in rows:
            # print all record
            print(aRecord)
    except sql.OperationalError as e:
        print(f"Films not found {e}")

if __name__ == "__main__":
    read_films()