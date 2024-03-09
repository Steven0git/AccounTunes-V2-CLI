from .Design import Art
from .Engine import Engine
import sqlite3 as sql
import os
import time

class Connect:
    """
    This class handles the connection to the database.

    Methods:
        __init__(db: str)
            Initializes the Connect object and establishes a connection to the database.

        cursor()
            Returns a cursor object for executing SQL commands on the connected database.
    """

    def __init__(self, db=None):
        self.engine = Engine()
        self.art = Art()
        self.conn = None  # Initialize self.conn
        self.db = db if db else self._prompt_database_path()
        
    def cursor(self):  # Correct method name to lowercase
        time.sleep(1)
        if os.path.exists(self.db):
            self.art.Header("AccountingApp V2")
            self.art.Loading("Connecting Into Database...", 2)
            self.conn = sql.connect(self.db)
            print()
            self.art.ColorPrint("Successfully Connected Into Database!", "green")
            print()
            time.sleep(1)
            self.art.Loading("Cursoring data....", 3)
            self.art.ColorPrint("Done!\n", 'green')
            time.sleep(1)
            return self.conn.cursor()  # Return the cursor object
        else:
            raise FileNotFoundError(self.art.ColorPrint("File Not Found!", "red"))

    def _prompt_database_path(self):
         return self.engine.fprompt("Enter Database Name: ", "db")
 
    def close_connection(self):
        """
        Closes the connection to the database.
        """
        self.conn.close()