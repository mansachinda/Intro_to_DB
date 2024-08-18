# A program that connects to the alx_book_store database with exception handling

import mysql.connector

try:

    myDb = mysql.connector.connect(
        host = 'hostname',
        username = 'root',
        passwd = 'alxisawesome',
    )

    myCursor = myDb.cursor()

    myCursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
    print("Database 'alx_book_store' created successfully!")
    myDb.close()

except mysql.connector.Error as err:
    print(f"Something went wrong: {err}")
