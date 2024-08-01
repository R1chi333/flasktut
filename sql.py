import pyodbc
import textwrap

def insertData(first_name, last_name, age, email):

    server = 'localhost, 1433'
    database = 'Flask Tutorial'
    username = 'sa'  
    password = 'FlaskTut101'  
    # ^ should probably put this in a env file lol

    # Define the connection string
    cnxn = pyodbc.connect(
        f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password}'
    )

    # Create the Cursor. Thingy that actually executes your queries 
    cursor = cnxn.cursor()
    # define an insert query with place holders for the values.
    insert_query = textwrap.dedent('''
        INSERT INTO People (FirstName, LastName, Age, Email)
        VALUES (?, ?, ?, ?);
    ''') 
    cursor.execute(insert_query, (first_name, last_name, age, email))

    # commit the inserts.
    cnxn.commit()

    # grab all the rows from the table
    cursor.execute('SELECT * FROM People')    

    for row in cursor:
        print(row)
        return row
    cursor.close()
    cnxn.close()


    #-----------------------------------------------------------------------------------------------------------------------------

def getData():
    server = 'localhost, 1433'
    database = 'Flask Tutorial'
    username = 'sa'  
    password = 'FlaskTut101'  

    cnxn = pyodbc.connect(
        f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password}'
    )
    cursor = cnxn.cursor()

    cursor.execute('SELECT * FROM People')
    rows = cursor.fetchall()

    # Get column names from cursor description
    columns = [desc[0] for desc in cursor.description]

    # Highlighted Conversion Part
    # Convert rows to list of dictionaries
    data = [dict(zip(columns, row)) for row in rows]
    data.reverse()
    cursor.close()
    cnxn.close()    
    return data

# if __name__ == '__main__':
#     data = getData()
#     for row in data:
#         print(data)


#for driver in pyodbc.drivers():
#    print(driver)
#Check what drivers you have ^