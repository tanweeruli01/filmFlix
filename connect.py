import sqlite3 as sql #import the standard sqlite3 module

try:
    #To use the module we start by creating the database connection (variable to hold the folder/file)
    #using the connect function from the sqlite3 module
    with sql.connect("filmflix.db") as dbCon:
        # once the connection and/or dbfile is created
        # create a cursor object(variable) and call it curser method
        dbCursor = dbCon.cursor() #use to execute sql statement
        print("Connection Successful")

except sql.OperationalError as e: #raise sqlerror
    # handle the exception/error raised
    print(f"Connection failed: {e}") 


