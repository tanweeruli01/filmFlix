from connect import *

# create subroutine
def update_films():
    #use filmID is a primary key and a unique field to update a record

    #the id of the record to be updated
    idField = input("Enter the filmID to update a record: ")
    #the field selected for the update
    fieldName = input("Enter the field (title, release year, rating, duration or genre) to update: ").title()

    #the value to be entered in the field
    fieldValue = input(f"Enter the value for the {fieldName}: ")
    print(fieldValue)

    # add quotes to field Value
    fieldValue = "'"+fieldValue+"'"
    print(fieldValue)

    try: #UPDATE members SET Firstname = "James" WHERE MemberID = 1/2/3/4...
        dbCursor.execute(f"UPDATE tblFilms SET {fieldName} = {fieldValue} WHERE filmID = {idField}")
        dbCon.commit()
        print(f"{idField} updated in the films table")

    except sql.OperationalError as e:
        print(f"Update failed: {e}")

if __name__ == "__main__":
    update_films()