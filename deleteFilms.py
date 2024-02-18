from connect import *

# create subroutine
def delete_film():

    try:
        #use filmID: is a primary key and a unique field to update a record
        #the id of the record to be updated
        idField = input("Enter the filmID to delete a record: ")   

        #select a record using a MemberID from the table 
        dbCursor.execute(f"SELECT * FROM tblFilms WHERE filmID = {idField}")

        row = dbCursor.fetchone() #use the fetchone() to fetch the selected record  
        
        #None; a singleton object to check/signal if the value is absent
        if row == None: #row is the record returned based on the specific MemberID
            print(f"No record with filmID {idField} exists.")

        else:
            dbCursor.execute(f"DELETE FROM tblFilms WHERE filmID = {idField}")
            dbCon.commit()
            print(f"filmID {idField} has been deleted successfully.")

    except sql.OperationalError as e:
        print(f"No database or table found: {e}")

if __name__ == "__main__":
    delete_film()


